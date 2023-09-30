# Mammogram-Dataset
Breast Mammogram Dataset with Annotations

PNG images of 496 Breast Mammograms collected from local hospitals in Sri Lanka are presented in the dataset.
The dataset is already divided into a train and validation set of 80-20 ratio randomly. 

Annotations are done according to the following four classes:

<table border="1">
  <tr>
    <th></th>
    <th>Malignant Mass</th>
    <th>Benign Calcification</th>
    <th>Benign Mass</th>
    <th>Malignant Calcification</th>
  </tr>
  <tr>
    <td>Train Set</td>
    <td>245</td>
    <td>174</td>
    <td>155</td>
    <td>79</td>
  </tr>
  <tr>
    <td>Test Set</td>
    <td>62</td>
    <td>47</td>
    <td>42</td>
    <td>17</td>
  </tr>
</table>

<img src="https://github.com/oshani-jayawardane/Mammogram-Dataset/assets/66548835/59dbbfc7-921d-420d-a383-3195f3028e58" alt="Class Distribution Chart" width="800px">

The bounding box annotations of the lesions are presented in:
1. Yolo 1.1 format
2. Coco 1.1 format
3. PASCAL VOC format
4. OpenImages v6 format

Segmentation Polygon Mask annotations are presented in:
1. VGG format

Bounding Box annotations example:
<img src="https://github.com/oshani-jayawardane/Mammogram-Dataset/assets/66548835/96c72078-5279-4c72-b855-d8d617ad7f4e" alt="BBox annotation example" width="300px">

To Pre-process data before training, ```preprocess.py``` could be used
Here is a sample pre-processing pipeline used during benchmarking

![pre-process](https://github.com/oshani-jayawardane/Mammogram-Dataset/assets/66548835/d2b4cc70-f1d3-4b72-bb9b-8c8a946f946b)

