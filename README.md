# Visual-DL

## To reproduce the submission file:

Step1: Install albumentations package 

Step2: Load in the training images and correspond them with their labels

Step3: Split the data for 5-fold cross validation

Step4: Create Dataset and DataLoader for both training sets and validation sets, also calculate the mean and standard deviation of the training dataset for normalization. Moreover, do some augmentation.
<img width="415" alt="image" src="https://user-images.githubusercontent.com/77607182/139598172-a9dd0139-8829-4f51-9d48-32b23537f040.png">


Step5: Train the model for 80 epochs per fold with Densenet model and SGD optimizer, also, set the loss function to focal loss. Save the weights only if the validation accuracy raises. After training, we can get the loss curve and the accuracy curve as below.

Step6: Load in the testing images and the txt file for detailed classes.

Step7: Create Dataset and DataLoader for testing set. Then, load the weights that is saved previously. The homework is done now by saving the answer file.

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
 
