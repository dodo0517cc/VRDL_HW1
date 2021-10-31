# Visual-DL

## To reproduce the submission file:

Step1: Install albumentations package 

Step2: Load in the training images and correspond them with their labels

Step3: Split the data for 5-fold cross validation

Step4: Create Dataset and DataLoader for both training sets and validation sets, also do some augmentation.

Step5: Train the model for 80 epochs per fold with Densenet model and SGD optimizer, also, set the loss function to focal loss. Save the weights only if the validation accuracy raises. After training, we can get the loss curve and the accuracy curve as below.

Step6: Load in the testing images and the txt file for detailed classes.

Step7: Create Dataset and DataLoader for testing set. Then, load the weights that is saved previously. The homework is done now by saving the answer file.

## Get the results

### Loss curve：

Fold 0
 
Fold 1
 
Fold 2
 
Fold 3
 
Fold 4
 
### Accuracy curve

Fold 0 
 
Fold 1
 
Fold 2
 
Fold 3
 
Fold 4
 
