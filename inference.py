"""# Testing"""

test_images = []
with open('./test_order.txt','r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        split_line = line.split(' ')
        img_name = split_line[0]
        test_images.append(img_name)

classes = []
with open('./2021VRDL_HW1_datasets/classes.txt') as f:
  for line in f.readlines():
      line = line.strip('\n')
      classes.append(line)

class TestDataset(Dataset):

    def __init__(self, data, labels, train, transform = None):
        self.df = data
        self.labels = labels
        self.train = train
        self.transform = transform

    def __getitem__(self,index): #data_loader會自動傳遞index變數，當index=N時，就是回傳資料集中第n筆資料

        image = cv2.imread('./2021VRDL_HW1_datasets/testing_images/' + self.df[index])
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_tensor = self.transform(image = image)
        return image_tensor['image'], self.df[index]

    def __len__(self):
        return len(self.df)

test_set = TestDataset(test_images, None, train=False, transform = val_transform)
test_loader = DataLoader(test_set, batch_size = 1)
# -------------- init model --------------
model = densenet_model()
model_name = 'CNN_model'
model.load_state_dict(torch.load('./' + model_name + '0.pkl'))
model.eval()
prediction = []
for img in test_loader:
    images, img_name = img
    node_2, logits = model(images)
    topv, topi = logits.topk(1) 
    for predict in topi.tolist():
      prediction.append([img_name[0], classes[predict[0]]])
np.savetxt('answer.txt', prediction, fmt='%s')

