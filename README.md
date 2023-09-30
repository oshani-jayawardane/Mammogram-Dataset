# Mammogram-Dataset
Breast Mammogram Dataset with Annotations

PNG images of 496 Breast Mammograms collected from local hospitals in Sri Lanka are presented in the dataset.
The dataset is already divided into a train and validation set of 80-20 ratio randomly. 

Annotations are done according to the following four classes:
1. Benign Mass
2. Malignant Mass
3. Benign Calcification
4. Malignant Calcification

The bounding box annotations of the lesions are presented in:
1. Yolo 1.1 format
2. Coco 1.1 format
3. PASCAL VOC format
4. OpenImages v6 format

Segmentation Polygon Mask annotations are presented in:
1. VGG format

To Pre-process data before training, ```preprocess.py``` could be used
Here is a sample pre-processing pipeline used during benchmarking

![pre-process](https://github.com/oshani-jayawardane/Mammogram-Dataset/assets/66548835/d2b4cc70-f1d3-4b72-bb9b-8c8a946f946b)

