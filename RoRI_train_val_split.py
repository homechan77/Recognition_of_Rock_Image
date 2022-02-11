import os
import pandas as pd
from sklearn.model_selection import train_test_split
import shutil

def train_valid_split(img_dir, anno_dir, test_size):
    trainlist = os.listdir(img_dir)
    
    Rock_class = []
    id_num = []
    img_filepath = []
    anno_filepath = []
    
    for i in trainlist:
        listsplit = i.split('_')
        Rock_class.append(listsplit[0])
        
        bf_id = list(listsplit[2])
        del bf_id[-4:]
        af_id = "".join(bf_id)
        id_num.append(af_id)
        
        img_filepath.append(img_dir+'/'+listsplit[0]+'_train_'+str(af_id)+'.jpg')
        anno_filepath.append((anno_dir+'/'+listsplit[0]+'_train_'+str(af_id)+'.txt'))
        
    dfdf = pd.DataFrame({'Class':Rock_class, 'Id':id_num, 'Img_filepath':img_filepath, 'Anno_filepath':anno_filepath})
    
    train_df, val_df = train_test_split(dfdf, test_size=test_size, stratify=dfdf['Class'], random_state=None)
    
    return dfdf, train_df, val_df

imgtrain = './RoRI_test/images/train'
annotrain = './RoRI_test/labels/train'
dfdf, train_df, val_df = train_valid_split(imgtrain, annotrain, 0.2)

for index, row in val_df.iterrows():
    valimg = row['Img_filepath']
    valanno = row['Anno_filepath']
    if os.path.exists(valimg):
        shutil.move(valimg, './RoRI_test/images/val')
    if os.path.exists(valanno):
        shutil.move(valanno, './RoRI_test/labels/val')
        