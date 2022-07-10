# Classification of birds

## Reference：

Focal Loss: https://github.com/clcarwin/focal_loss_pytorch
Focal loss is a loss function proposed in the article “Focal Loss for Dense Object Detection” to decay simple samples. The aim of focal loss is to perform down-weighting for inliers (easy examples), because it hopes to train hard examples as much as possible during the training process and ignore those easy examples. It is an improvement of the standard Cross Entropy Loss. The function is as below.
Setting γ > 0 reduces the relative loss for well-classified samples, putting more focus on hard, misclassified examples. 

##Brief introduction：

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

## Model architecture：Transfer learning－Densenet161
Use the pretrained weights, but unfreeze the layers. 
Change the original fully connected layer－
Add a Fully Connected Layer with 1024 output channels
Apply batch normalization
Choose ReLU as the activation function
Add Dropout layer for 0.3 probability to reduce overfitting
Finally add a Fully Connected Layer with 200 output channels, because there are 200 classes


## Hyperparameters：

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

### Loss curve：

Fold 0
![train loss](https://user-images.githubusercontent.com/77607182/139598076-cd8bbbbd-8a38-41e9-a171-5148344eb81f.jpeg)

 
Fold 1
![train loss](https://user-images.githubusercontent.com/77607182/139598119-96d4ca4e-2b9a-44bb-9000-91eae28886da.jpeg)
 
Fold 2
![train loss](https://user-images.githubusercontent.com/77607182/139598135-509d02eb-1ca7-42b1-9db7-232467fced2a.jpeg)
 
Fold 3
![train loss](https://user-images.githubusercontent.com/77607182/139598143-b4efae96-897b-4dfe-9cfc-54a1281f4602.jpeg)
 
Fold 4
![train loss](https://user-images.githubusercontent.com/77607182/139598151-897b0978-b131-45e8-b532-e0441f847cdc.jpeg)
 
### Accuracy curve

Fold 0 
 ![train_acc](https://user-images.githubusercontent.com/77607182/139598114-a5466432-aafe-420b-a0cd-fbf098ffe165.jpeg)

Fold 1
 ![train_acc](https://user-images.githubusercontent.com/77607182/139598121-156fe8f1-a63a-4924-a646-fc75f92248a3.jpeg)

Fold 2
![train_acc](https://user-images.githubusercontent.com/77607182/139598140-5d77a739-479d-48cb-8fcc-671064fdecf3.jpeg)
 
Fold 3
![train_acc](https://user-images.githubusercontent.com/77607182/139598146-c5fd23a9-e6ad-4fea-a117-b2dbad879300.jpeg)
 
Fold 4
![train_acc](https://user-images.githubusercontent.com/77607182/139598158-d7b5e596-714a-41a4-88bf-f09a52d84cb7.jpeg)
 
