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
5. Create two folders **train_images** and **val_images** and save the training and validation images in the two folders respectively.
6. Add annotation files of the form OpenImage-v6 to the two folders **train** and **val** under the **labels** folder.
7. Run the **dataset-preparation-frcnn** script (make sure to adjust the dataset location).
8. **train.csv**, **val.csv**, **annotations.txt**, and **annotations-val.txt** files will be automatically created in the working directory.

# Training the Dataset
10. cd to the **FasterRCNN** folder and clone the keras-frcnn repository inside it.
   ```
   git clone https://github.com/kbardool/keras-frcnn.git
   ```
11. cd to the cloned repository: ```cd tf-keras-frcnn```
12. Train the model selecting suitable hyperparameters. The editable paramaters are listed below
13. 
Example: ```python train_frcnn.py -o simple -p annotate.txt```
 

