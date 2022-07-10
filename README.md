# Classification of birds

## Reference：

Focal Loss: https://github.com/clcarwin/focal_loss_pytorch

Focal loss is a loss function proposed in the article “Focal Loss for Dense Object Detection” to decay simple samples. The aim of focal loss is to perform down-weighting for inliers (easy examples), because it hopes to train hard examples as much as possible during the training process and ignore those easy examples. It is an improvement of the standard Cross Entropy Loss. The function is as below.
Setting γ > 0 reduces the relative loss for well-classified samples, putting more focus on hard, misclassified examples. 

## Brief introduction：

There are only 3000 images for training. After counting, I found that it’s only 15 images for each class. Obviously, it’s a small-scaled dataset. As a result, I met overfitting problems. In order to deal with the problems, I did some data augmentation, and added Dropout layer in my fully connected layer of my transfer learning model－Densenet161. Also, I added weight decay for L2 regularization in my optimizer－SGD. 
For the training process, I did 5-fold cross validation to valid my training results.

## Methodology：

### Data pre-process：

Transformation for Training（done by Albumentation package）：

Random Resized Crop images to 299*299 pixels

RGB Shift－set the ranges for changing values for the red channel, green channel and blue channel as 15. Also, set the probability as 0.5.

Horizontal Flip－set the probability as 0.5

Shift Scale Rotate－set rotation range as 20, probability as 0.5

Normalization 

----------------------------------------------------------------------------------------------------------------

Transformation for Validation（done by Albumentation package）：

Resized images to 375*375pixels

Center Crop to 299*299 pixels

Normalization

### Model architecture：Transfer learning－Densenet161
Use the pretrained weights, but unfreeze the layers. 
Change the original fully connected layer－
Add a Fully Connected Layer with 1024 output channels
Apply batch normalization
Choose ReLU as the activation function
Add Dropout layer for 0.3 probability to reduce overfitting
Finally add a Fully Connected Layer with 200 output channels, because there are 200 classes


### Hyperparameters：

Learning Rate－0.005

Batch Size－64

Epochs－80

Loss－Focal Loss ( gamma=4 )

Optimizer－SGD ( momentum = 0.9, weight_decay = 1e-5 )


## To reproduce the submission file:

Step1: Install albumentations package.
       
       Download sample_submission.txt on colab and rename it as test_order.txt.
       
       Change the path of os.chdir('/home/u9285752/') to os.chdir('your_path') where the your_path is the path that your files exist.

Step2: Load in the training images and correspond them with their labels

Step3: Split the data for 5-fold cross validation

Step4: Create Dataset and DataLoader for both training sets and validation sets, also calculate the mean and standard deviation of the training dataset for normalization. Moreover, do some augmentation.
<img width="415" alt="image" src="https://user-images.githubusercontent.com/77607182/139598172-a9dd0139-8829-4f51-9d48-32b23537f040.png">


Step5: Train the model for 80 epochs per fold with Densenet model and SGD optimizer, also, set the loss function to focal loss. Save the weights only if the validation accuracy raises. After training, we can get the loss curve and the accuracy curve as below.

Step6: Load in the testing images and the txt file for detailed classes and image orders of submission.

Step7: Create Dataset and DataLoader for testing set. Then, load the weights that is saved previously.(The weights file is too big to upload, so I provide a google drive link for fold0:https://drive.google.com/drive/folders/1FaYXQT4MRJA8A38fXFtqcGu4u3LwpCfb?usp=sharing) The homework is done now by saving the answer file.


## Get the results

### Loss curves for 5 folds：

<img width="265" alt="image" src="https://user-images.githubusercontent.com/77607182/178141325-04128e57-10ab-4c30-b489-cc25f16f3f39.png"><img width="265" alt="image" src="https://user-images.githubusercontent.com/77607182/178141348-7f4f5cee-cf7a-4237-a46f-3619c1225271.png"><img width="265" alt="image" src="https://user-images.githubusercontent.com/77607182/178141350-5e1a116b-c90e-4f97-be4e-d4f290590b6c.png"><img width="265" alt="image" src="https://user-images.githubusercontent.com/77607182/178141359-18c74742-4d13-41dd-87fe-38d5be22132d.png"><img width="265" alt="image" src="https://user-images.githubusercontent.com/77607182/178141361-128b9cf2-91fb-443d-b890-7d5cc71d0f69.png">

### Accuracy curves for 5 folds：

<img width="265" alt="image" src="https://user-images.githubusercontent.com/77607182/178141390-ae2c3cfb-358d-406d-bcfa-0e65e27d515e.png"><img width="265" alt="image" src="https://user-images.githubusercontent.com/77607182/178141397-49d65fab-62f4-4e20-a399-abe782c381a3.png"><img width="265" alt="image" src="https://user-images.githubusercontent.com/77607182/178141400-9b8c27b2-2e57-4bdc-bb1a-7e2c29a5bfa9.png"><img width="265" alt="image" src="https://user-images.githubusercontent.com/77607182/178141402-9968ff69-3e68-44a3-a546-f04b967e8c2b.png"><img width="265" alt="image" src="https://user-images.githubusercontent.com/77607182/178141433-464d9f62-6488-4a55-88f0-cdbe7e20d571.png">


<img width="265" alt="image" src="https://user-images.githubusercontent.com/77607182/178141390-ae2c3cfb-358d-406d-bcfa-0e65e27d515e.png"><img width="265" alt="image" src="https://user-images.githubusercontent.com/77607182/178141397-49d65fab-62f4-4e20-a399-abe782c381a3.png">
