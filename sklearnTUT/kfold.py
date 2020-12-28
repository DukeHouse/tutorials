'''
Author: DukeHouse
Date: 2020-12-28 12:30:32
LastEditors: DukeHouse
LastEditTime: 2020-12-28 12:35:33
Description: Do not edit
Sample output: Do not edit
'''
import numpy as np
from sklearn.model_selection import StratifiedKFold,KFold

X=np.array([
    [1,2,3,4],
    [11,12,13,14],
    [21,22,23,24],
    [31,32,33,34],
    [41,42,43,44],
    [51,52,53,54],
    [61,62,63,64],
    [71,72,73,74]
])
 
y=np.array([1,1,0,0,1,1,0,0])


# kfolder = KFold(n_splits=4,random_state=1)
kfolder = KFold(n_splits=4)
for train, test in kfolder.split(X,y):
    print('Train: %s | test: %s' % (train, test),'\n')

#依照标签的比例来抽取数据，本案例集标签0和1的比例是1：1
#因此在抽取数据时也是按照标签比例1：1来提取的
sfolder = StratifiedKFold(n_splits=4)
for train, test in sfolder.split(X,y):
    print('Train: %s | test: %s' % (train, test))