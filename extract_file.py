import os
import shutil

train_dir = './train_label/'
test_dir = './test_label/'
vgg_train_dir = './vgg/total_train/'
vgg_test_dir = './vgg/total_test/'

traind = os.listdir(train_dir)
testd = os.listdir(test_dir)
vgg_traind = os.listdir(vgg_train_dir)
vgg_testd = os.listdir(vgg_test_dir)


for i in traind:
    for j in vgg_traind:
        if i[:-4] == j[:-4]:
            shutil.copy((vgg_train_dir + j), './RoRI_test/images/train')
            
            
for m in testd:
    for n in vgg_testd:
        if m[:-4] == n[:-4]:
            shutil.copy((vgg_test_dir + n), './RoRI_test/images/test')