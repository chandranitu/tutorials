import numpy as np
import pandas as pd
import os
#print(os.listdir("../input"))

from fastai.imports import *
from fastai.transforms import *
from fastai.conv_learner import *
from fastai.model import *
from fastai.dataset import *
from fastai.sgdr import *
from fastai.plots import *

PATH = "/home/hadoop/hadoop/hadoop_working/DataScience/5.MachineLearning/8.DeepLearning/code/mobiles/"
TMP_PATH = "/home/hadoop/hadoop/hadoop_working/DataScience/5.MachineLearning/8.DeepLearning/code/mobile/tmp/tmp"
MODEL_PATH = "/home/hadoop/hadoop/hadoop_working/DataScience/5.MachineLearning/8.DeepLearning/code/mobile/tmp/model"
sz=224

torch.cuda.is_available()
torch.backends.cudnn.enabled

os.listdir(PATH)
fnames = np.array([f'train/{f}' for f in sorted(os.listdir(f'{PATH}train'))])
print(fnames[0])
labels = np.array([(0 if '0' in fname[-5] else 1) for fname in fnames])
for i in range(len(labels)):
    print(labels[i])


img = plt.imread(f'{PATH}{fnames[0]}')
plt.imshow(img)

img.shape

arch = resnet34
data = ImageClassifierData.from_names_and_array(
    path = PATH,
    fnames = fnames,
    y = labels,
    classes = ['0','1'],
    test_name = 'test',
    tfms = tfms_from_model(arch,sz)
)
learn = ConvLearner.pretrained(arch, data, precompute=True, tmp_name=TMP_PATH, models_name=MODEL_PATH)
learn.fit(0.01, 5)

data.val_y

data.classes

log_preds = learn.predict()
log_preds.shape

log_preds[:10]

preds = np.argmax(log_preds, axis=1)
probs = np.exp(log_preds[:,1])

def rand_by_mask(mask): return np.random.choice(np.where(mask)[0], 4, replace=False)
def rand_by_correct(is_correct): return rand_by_mask((preds == data.val_y)==is_correct)

def plots(ims, figsize=(12,6), rows=1, titles=None):
    f = plt.figure(figsize=figsize)
    for i in range(len(ims)):
        sp = f.add_subplot(rows, len(ims)//rows, i+1)
        sp.axis('Off')
        if titles is not None: sp.set_title(titles[i], fontsize=16)
        plt.imshow(ims[i])
        
def load_img_id(ds, idx): return np.array(PIL.Image.open(PATH+ds.fnames[idx]))

def plot_val_with_title(idxs, title):
    imgs = [load_img_id(data.val_ds,x) for x in idxs]
    title_probs = [probs[x] for x in idxs]
    print(title)
    return plots(imgs, rows=1, titles=title_probs, figsize=(16,8))


plot_val_with_title(rand_by_correct(True), "Correctly classified")

plot_val_with_title(rand_by_correct(False), "Incorrectly classified")

def most_by_mask(mask, mult):
    idxs = np.where(mask)[0]
    return idxs[np.argsort(mult * probs[idxs])[:4]]

def most_by_correct(y, is_correct): 
    mult = -1 if (y==1)==is_correct else 1
    return most_by_mask(((preds == data.val_y)==is_correct) & (data.val_y == y), mult)
    
plot_val_with_title(most_by_correct(0, True), "Most correct non-shattered phones")
plot_val_with_title(most_by_correct(1, True), "Most correct shattered phone")
plot_val_with_title(most_by_correct(0, False), "Most incorrect non-shattered phones")
plot_val_with_title(most_by_correct(1, False), "Most incorrect shattered phones")
most_uncertain = np.argsort(np.abs(probs -0.5))[:4]
plot_val_with_title(most_uncertain, "Most uncertain predictions")
learn = ConvLearner.pretrained(arch, data, precompute=True, tmp_name=TMP_PATH, models_name=MODEL_PATH)
lrf=learn.lr_find()
learn.sched.plot_lr()
