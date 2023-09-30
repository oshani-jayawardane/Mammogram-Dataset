import cv2
import numpy as np
import os

"""
Function list:
    crop(image_path, new_text_path)
    denoise(img)
    trunc_norm(img, thresh_mask, pmin, pmax)
    clahe(img, clipLimit, gridSize)
"""

"""
Additonal Supportive functions:
    get_imageFile(path)
    get_textFile(path)
    read_annotation(textFile)
"""
# Additional supportive functions

def get_imageFile(path):
  path_split = path.split('/')
  element = path_split[-1] # gives ex: 1.png
  return element

def get_textFile(path):
  element = get_imageFile(path)
  element_split = element.split('.') # gives ex: 1
  name = element_split[-2] + '.txt'
  return name

#########################################################################################
# Crop Image
#########################################################################################

def read_annotation(textFile):
  '''
  class, x_center, y_center, width, height

  '''
  # data = np.loadtxt(textFile, usecols=(0, 1, 2, 3, 4))
  data = np.loadtxt(textFile, delimiter=' ', ndmin=1)
  data = np.atleast_2d(data)

  # Extract individual columns
  classValue = data[:, 0]
  x_center = data[:, 1]
  y_center = data[:, 2]
  width = data[:, 3]
  height = data[:, 4]

  return classValue, x_center, y_center, width, height

##################################################################

def crop(image_path, text_path, new_text_path):
  """Crops the breast mammogram to fit the breast region such that the amount of black pixels are reduced.

  Args:
    image: image path

  Returns:
    A NumPy array of the cropped image,
  """

  # image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
  image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
  textFile = get_textFile(image_path)

  image_height = image.shape[0]
  image_width = image.shape[1]

  # get the center coordinates of the bbox
  classValue, x_center, y_center, width, height = read_annotation(text_path)

  abs_x_center = x_center * image_width
  abs_y_center = y_center * image_height

  # Create a mask of the breast region by thresholding the image and applying morphological operations.
  thresh_mask = cv2.threshold(image, 1, 255, cv2.THRESH_BINARY)[1]
  kernel = np.ones((5, 5), np.uint8)
  thresh_mask = cv2.morphologyEx(thresh_mask, cv2.MORPH_CLOSE, kernel)
  thresh_mask = cv2.morphologyEx(thresh_mask, cv2.MORPH_OPEN, kernel)

  # Find contours in the mask and select the largest one
  cnts, _ = cv2.findContours(thresh_mask.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  cnt = max(cnts, key = cv2.contourArea)
  x, y, w, h = cv2.boundingRect(cnt)

  new_x_center = (abs_x_center - x) / w
  new_y_center = (abs_y_center - y) / h
  new_width = (width * image_width) / w
  new_height = (height * image_height) / h

  # Create a list of lines in the desired format
  lines = []
  for i in range(len(classValue)):
    line = f"{int(classValue[i])} {new_x_center[i]:.6f} {new_y_center[i]:.6f} {new_width[i]:.6f} {new_height[i]:.6f}\n"
    lines.append(line)

  try:
    # Write the lines to a text file
    new_text_path = new_text_path + textFile
    with open(new_text_path, 'w') as file:
      file.writelines(lines)

    print("Textfile {} saved to path {}". format(textFile, new_text_path))

  except Exception as e:
    print(f"Could not update text file. \n error: {str(e)}")

  # # Crop the image and the bounding boxes to the breast region.
  cropped_image = image[y:y+h, x:x+w]
  mask = thresh_mask[y:y+h, x:x+w]

  return cropped_image, mask

#########################################################################################
# Denoise and Edge Enhance
#########################################################################################

def denoise(img):
  """
    Denoise image.
    @img : numpy array image
    return: numpy array of denoised image
  """
  kernel_size = 3
  kernel = np.ones((kernel_size,kernel_size),np.uint8)

  # blur = cv2.GaussianBlur(img,(kernel_size,kernel_size),0)

  morph_open = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

  morph_close = cv2.morphologyEx(morph_open, cv2.MORPH_OPEN, kernel)

  # erosion = cv2.erode(img, np.ones((kernel_size, kernel_size), np.uint8), iterations=1)

  dilation = cv2.dilate(morph_close, np.ones((kernel_size, kernel_size), np.uint8), iterations=2)

  return dilation

#########################################################################################
# Truncate and Normalize
#########################################################################################

def trunc_norm(img, mask, min, max):
  """
  Clip and normalize pixels in the breast ROI.
  @img : numpy array image (cropped and denoised image)
  @mask : numpy array mask of the breast
  return: numpy array of the truncated image
  """

  Pmin = np.percentile(img[mask!=0], min)
  Pmax = np.percentile(img[mask!=0], max)
  truncated = np.clip(img,Pmin, Pmax)
  normalized = (truncated - Pmin)/(Pmax - Pmin)
  normalized[mask==0]=0
  
  # return normalized

  return np.array(normalized*255, dtype=np.uint8)

#########################################################################################
# CLAHE for Contrast Enhancement
#########################################################################################

def clahe(img, clip, gridSize):
    """
    Image enhancement.
    @img : numpy array image
    @clip : float, clip limit for CLAHE algorithm
    return: numpy array of the enhanced image
    """

    # Create a CLAHE object
    clahe = cv2.createCLAHE(clipLimit=clip, tileGridSize=(gridSize, gridSize))

    # Apply CLAHE to the image
    # enhanced_image = clahe.apply(img)

    # if the image is normalized
    enhanced_image = clahe.apply(img)

    return enhanced_image
  
# #########################################################################################
# # Pipeline
# #########################################################################################

"""
The Preprocessing Pipeline:
original image ---> crop ---> denoise ---> truncate and normalize ---> enhance using clahe
"""

# def preprocess(image_path, text_path, new_image_path, new_text_path):
#   image_name = get_imageFile(image_path)

#   cropped_image, breast_mask = crop(image_path, text_path, new_text_path)
#   # denoised_image = denoise(cropped_image)
#   normalized_image = trunc_norm(cropped_image, breast_mask, 2, 100)
#   # enhanced_image = clahe(normalized_image, 1.0, 1)

#   final_image = normalized_image

#   try:
#     final_image_path = os.path.join(new_image_path, image_name)
#     cv2.imwrite(final_image_path, final_image)
#     print("image {} saved to path {}".format(image_name, new_image_path))

#   except Exception as e:
#     print(f"Could not update image file. \n error: {str(e)}")