import numpy as np
from sklearn import svm
import pandas as pd

df = pd.read_csv('train_SMOTE_ALL.csv')
dft = pd.read_csv('test_SMOTE_ALL.csv')

training_data  = df.iloc[1:,0:27]
training_label = df.iloc[1:,28]

#---------------------------
# 測試資料及標籤
#---------------------------
testing_data  = dft.iloc[:,0:27]
testing_label = dft.iloc[:,28]


#***********************************************
# 建立自動分類機器人
#***********************************************
svm_linear = svm.SVC(kernel='linear', C=1.0)
svm_linear.fit(training_data, training_label)

#---------------------------
# 分類機器人測試
#---------------------------
print('正確:', testing_label)
print('-'*60)

predict = svm_linear.predict(testing_data)
print('預測:', predict)
print('-'*60)

#---------------------------
# 和正確資料比對
#---------------------------
results = testing_label == predict
print('比對:', results)
print('-'*60)

#---------------------------
# 正確率
#---------------------------
print('正確率:', round(np.sum(results)/len(results), 5))
print('-'*60)