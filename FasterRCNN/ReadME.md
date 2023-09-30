# Faster RCNN Tensorflow implementation on the Dataset

# Setting up the Environment
1. create a new conda environment and activate it (recommend to use python 3.7)
   ```
   conda create -n faster-rcnn-project python=3.7
   ```
3. clone this git repository inside the project location
4. install required packages into the current environment
   ```
   pip install -r requirement.txt
   ```

# Preparing the Dataset
5. Create a folder **dataset** and within that folder create two subfolders **train** and **val** and save the training and validation images in the two folders respectively.
6. Add annotation files of the form OpenImage-v6 to the two folders **train** and **val** under the **labels** folder.
7. Run the **dataset-preparation-frcnn** script (make sure to adjust the dataset location).
8. **train.csv**, **val.csv**, **annotations.txt**, and **annotations-val.txt** files will be automatically created in the working directory.

# Training the Dataset
9. cd to the **FasterRCNN** folder and clone the keras-frcnn repository inside it.
   ```
   git clone https://github.com/kbardool/keras-frcnn.git
   ```
10. cd to the cloned repository: ```cd tf-keras-frcnn```
11. Copy the **train.csv**, **val.csv**, **annotations.txt** files inside this folder
12. Train the model by selecting suitable hyperparameters. The editable paramaters are listed below
 ![parameters](https://github.com/oshani-jayawardane/Mammogram-Dataset/assets/66548835/5e3b94e9-3de9-47aa-a9b4-2bcfd239f7c1)

Example: 
```
python train_frcnn.py -p annotations.txt -o simple --num_epochs 5  
```
