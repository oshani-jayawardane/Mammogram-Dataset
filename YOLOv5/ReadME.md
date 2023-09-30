# Training Dataset on Yolov5x

![result-image](https://github.com/oshani-jayawardane/Mammogram-Dataset/assets/66548835/c2b7913b-e119-4aba-bfda-fede8215f72c)

## Pre-trained weight files

The Dataset was trained on a Yolov5x model. The obtained weights are given as follows:

Yolov5x model weights before preprocessing:
https://drive.google.com/file/d/1-17icIaMHO8T4KlJOGVa0PAV3yFntDhh/view?usp=sharing 

Yolov5x model weights after preprocessing:
https://drive.google.com/file/d/1zZMkmX52RBOUfQDQkknZLU5sWAQms6ua/view?usp=drive_link

## Results comparison

<table>
     <tr>
          <th>Comparison</th>
          <th>Before Preprocessing</th>
          <th>After Preprocessing</th>
        </tr>
     <tr>
          <td>Loss Curves</td>
          <td><img src="https://github.com/oshani-jayawardane/Mammogram-Dataset/assets/66548835/1c901399-852b-46e4-81bf-e9ebc26a1aa2" alt="Before Preprocessing"></td>
          <td><img src="https://github.com/oshani-jayawardane/Mammogram-Dataset/assets/66548835/6fbf9b54-7a2b-4e3d-9abd-baae150024e6" alt="After Preprocessing"></td>
     </tr>
     <tr>
          <td>Confusion Matrix</td>
          <td><img src="![confusion_matrix](https://github.com/oshani-jayawardane/Mammogram-Dataset/assets/66548835/2060aeac-f154-4801-b46b-655736aa704c)
" alt="Before Preprocessing"></td>
          <td><img src="![confusion_matrix](https://github.com/oshani-jayawardane/Mammogram-Dataset/assets/66548835/e0dd7bdc-5aeb-433b-ab55-03e96d4dc7ae)" alt="After Preprocessing"></td>
     </tr>
     <tr>
          <td>Precision-Confidence Curve</td>
          <td><img src="![P_curve](https://github.com/oshani-jayawardane/Mammogram-Dataset/assets/66548835/f037c375-b224-481e-9a6e-d071a730a95d)
" alt="Before Preprocessing"></td>
          <td><img src="![P_curve](https://github.com/oshani-jayawardane/Mammogram-Dataset/assets/66548835/b9f4e12f-be2d-40eb-9bf5-4a082a5ca0fb)
" alt="After Preprocessing"></td>
     </tr>
     <tr>
          <td>Precision-Recall Curve</td>
          <td><img src="![PR_curve](https://github.com/oshani-jayawardane/Mammogram-Dataset/assets/66548835/1906bb69-53ab-41bb-9178-29d8f3a7b4de)
" alt="Before Preprocessing"></td>
          <td><img src="![PR_curve](https://github.com/oshani-jayawardane/Mammogram-Dataset/assets/66548835/b1628a3a-14a6-487a-ae67-66724bce8526)
" alt="After Preprocessing"></td>
     </tr>
     <tr>
          <td>Recall-Confidence Curve</td>
          <td><img src="![R_curve](https://github.com/oshani-jayawardane/Mammogram-Dataset/assets/66548835/16fe2810-b773-4840-a38e-58bd591b7ef1)
" alt="Before Preprocessing"></td>
          <td><img src="![R_curve](https://github.com/oshani-jayawardane/Mammogram-Dataset/assets/66548835/c4df2430-0cf9-4a7f-a88e-aa3952965236)
" alt="After Preprocessing"></td>
     </tr>
     <tr>
          <td>F1-Confidence Curve</td>
          <td><img src="![F1_curve](https://github.com/oshani-jayawardane/Mammogram-Dataset/assets/66548835/42607044-fab9-47cc-9d6d-5dfc7a2df95b)
" alt="Before Preprocessing"></td>
          <td><img src="![F1_curve](https://github.com/oshani-jayawardane/Mammogram-Dataset/assets/66548835/5ccfe819-8fa7-4de5-a767-15792204bb40)
" alt="After Preprocessing"></td>
     </tr>
</table> 

## Training 

Training YOLO - Example
```
!python train.py --cfg /content/yolov5/models/yolov5x.yaml --img 640 --batch-size 16 --epochs 25 --optimizer 'SGD' --data /content/yolov5/data/dataset.yaml --weights yolov5x.pt --cache --device 0
```

Parameter List:

![1](https://github.com/oshani-jayawardane/Mammogram-Dataset/assets/66548835/7b84a46d-ae30-46a9-b346-581d560b4df3)
![2](https://github.com/oshani-jayawardane/Mammogram-Dataset/assets/66548835/ab5647a6-e9ea-4ded-9cdc-502db14a869d)
![3](https://github.com/oshani-jayawardane/Mammogram-Dataset/assets/66548835/90f9de8c-c80e-41b2-a347-8a976439adc4)

