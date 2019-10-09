
# coding: utf-8

# In[1]:


#from Pic2NpArray import ResizeAndConToNumpyArray as tna
from PIL import Image
import random
import os
import csv
import pandas as pd
import numpy as np



class PicSet:
    def __init__(self):
        self.MainTraingData = []                                            #PIC Set
        self.RandomData = []                                                #PIC Set with Random
        self.PushIndex = 0                                                  #record of output  
        ####


    def add(self,PicDir,ans=-1,x_size=28,y_size=28):                        #add pic's data to PIC Set
        data = Image.open(PicDir)                                           #read a pic from dir
        NArray = tna(data,x_size,y_size)                                    #resize pic
        #print('picdir is',PicDir)
        #data=pd.read_csv(PicDir) 
        #NArray = np.array(data)
        #print('NArray is',PicDir)
        self.MainTraingData.append([NArray,ans])                            #add data of pic and Ans to Set
        ####
    def AddDir(self,picdir= "./TraingData1/",x_size=28,y_size=28):
        for dirPath, dirNames, fileNames in os.walk(picdir):
            for f in fileNames:                        
                ans=[0,0,0,0,0,0,0,0,0,0]
                ans[int(dirPath[len(picdir):])]+=1
                self.add(str(os.path.join(dirPath, f)),ans,x_size,y_size)
                #print ("add pic:",os.path.join(dirPath, f),"The Pic's Ans:",ans)
        ####
    def Addtest(self,picdir= "./TraingData100/"):
        NArray = []
        NArray1 =[]
        NArray2 =[]
        NArray3 =[]
        NArray4 =[]
        NArray5 =[]
        NArray6 =[]
        NArray7 =[]
        NArray8 =[]
        NArray9 =[]
        NArray10 =[]
        NArray11 =[]
        NArray12 =[]
        NArray13 =[]
        NArray14 =[]
        NArray15 =[]
        NArray16 =[]
        NArray17 =[]
        NArray18 =[]
        NArray19 =[]
        NArray20 =[]
        NArray21 =[]
        NArray22 =[]
        NArray23 =[]
        NArray24 =[]
        NArray25 =[]
        NArray26 =[]
        NArray27 =[]
        NArray28 =[]
        NArray29 =[]
        for dirPath, dirNames, fileNames in os.walk(picdir):
            for f in fileNames:                        
                ans=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                ans[int(dirPath[len(picdir):])]+=1
                if ans[0] == 1:
                    data=pd.read_csv('./TraingData1000/0/item0.csv')
                    for i0 in range(0,59):
                        NArray = np.array(data)
                        self.MainTraingData.append([NArray[i0],ans]) 
#                    print("dafdfdf = ",NArray[0])                        
                        #print ("array pic:",NArray[1660],"The Pic's Ans:",ans)
                elif ans[1] == 1:
                    data=pd.read_csv('./TraingData1000/1/item1.csv')
                    for i1 in range(0,4):
                            NArray1 = np.array(data)
                            self.MainTraingData.append([NArray1[i1],ans])
                #self.add(str(os.path.join(dirPath, f)),ans,x_size,y_size)
                #print ("add pic:",os.path.join(dirPath, f),"The Pic's Ans:",ans)
                elif ans[2] == 1:
                    data=pd.read_csv('./TraingData1000/2/item2.csv')
                    for i2 in range(0,22):
                            NArray2 = np.array(data)
                            self.MainTraingData.append([NArray2[i2],ans])
                elif ans[3] == 1:
                    data=pd.read_csv('./TraingData1000/3/item3.csv')
                    for i3 in range(0,13):
                            NArray3 = np.array(data)
                            self.MainTraingData.append([NArray3[i3],ans])
                elif ans[4] == 1:
                    data=pd.read_csv('./TraingData1000/4/item4.csv')
                    for i4 in range(0,25):
                            NArray4 = np.array(data)
                            self.MainTraingData.append([NArray4[i4],ans])
                elif ans[5] == 1:
                    data=pd.read_csv('./TraingData1000/5/item5.csv')
                    for i5 in range(0,5):
                            NArray5 = np.array(data)
                            self.MainTraingData.append([NArray5[i5],ans])
                elif ans[6] == 1:
                    data=pd.read_csv('./TraingData1000/6/item6.csv')
                    for i6 in range(0,1):
                            NArray6 = np.array(data)
                            self.MainTraingData.append([NArray6[i6],ans])
                elif ans[7] == 1:
                    data=pd.read_csv('./TraingData1000/7/item7.csv')
                    for i7 in range(0,7):
                            NArray7 = np.array(data)
                            self.MainTraingData.append([NArray7[i7],ans])
                elif ans[8] == 1:
                    data=pd.read_csv('./TraingData1000/8/item8.csv')
                    for i8 in range(0,4):
                            NArray8 = np.array(data)
                            self.MainTraingData.append([NArray8[i8],ans])
                elif ans[9] == 1:
                    data=pd.read_csv('./TraingData1000/9/item9.csv')
                    for i9 in range(0,10):
                            NArray9 = np.array(data)
                            self.MainTraingData.append([NArray9[i9],ans])
                elif ans[10] == 1:
                    data=pd.read_csv('./TraingData1000/10/item10.csv')
                    for i10 in range(0,6):
                            NArray10 = np.array(data)
                            self.MainTraingData.append([NArray10[i10],ans])
                elif ans[11] == 1:
                    data=pd.read_csv('./TraingData1000/11/item11.csv')
                    for i11 in range(0,25):
                            NArray11 = np.array(data)
                            self.MainTraingData.append([NArray11[i11],ans])
                elif ans[12] == 1:
                    data=pd.read_csv('./TraingData1000/12/item12.csv')
                    for i12 in range(0,106):
                            NArray12 = np.array(data)
                            self.MainTraingData.append([NArray12[i12],ans])
                elif ans[13] == 1:
                    data=pd.read_csv('./TraingData1000/13/item13.csv')
                    for i13 in range(0,32):
                            NArray13 = np.array(data)
                            self.MainTraingData.append([NArray13[i13],ans])
                elif ans[14] == 1:
                    data=pd.read_csv('./TraingData1000/14/item14.csv')
                    for i14 in range(0,24):
                            NArray14 = np.array(data)
                            self.MainTraingData.append([NArray14[i14],ans])
                elif ans[15] == 1:
                    data=pd.read_csv('./TraingData1000/15/item15.csv')
                    for i15 in range(0,24):
                            NArray15 = np.array(data)
                            self.MainTraingData.append([NArray15[i15],ans])
                elif ans[16] == 1:
                    data=pd.read_csv('./TraingData1000/16/item16.csv')
                    for i16 in range(0,18):
                            NArray16 = np.array(data)
                            self.MainTraingData.append([NArray16[i16],ans])
                elif ans[17] == 1:
                    data=pd.read_csv('./TraingData1000/17/item17.csv')
                    for i17 in range(0,34):
                            NArray17 = np.array(data)
                            self.MainTraingData.append([NArray17[i17],ans])
                elif ans[18] == 1:
                    data=pd.read_csv('./TraingData1000/18/item18.csv')
                    for i18 in range(0,25):
                            NArray18 = np.array(data)
                            self.MainTraingData.append([NArray18[i18],ans])
                elif ans[19] == 1:
                    data=pd.read_csv('./TraingData1000/19/item19.csv')
                    for i19 in range(0,45):
                            NArray19 = np.array(data)
                            self.MainTraingData.append([NArray19[i19],ans])
                elif ans[20] == 1:
                    data=pd.read_csv('./TraingData1000/20/item20.csv')
                    for i20 in range(0,29):
                            NArray20 = np.array(data)
                            self.MainTraingData.append([NArray20[i20],ans])
                elif ans[21] == 1:
                    data=pd.read_csv('./TraingData1000/21/item21.csv')
                    for i21 in range(0,33):
                            NArray21 = np.array(data)
                            self.MainTraingData.append([NArray21[i21],ans])
                elif ans[22] == 1:
                    data=pd.read_csv('./TraingData1000/22/item22.csv')
                    for i22 in range(0,29):
                            NArray22 = np.array(data)
                            self.MainTraingData.append([NArray22[i22],ans])
                elif ans[23] == 1:
                    data=pd.read_csv('./TraingData1000/23/item23.csv')
                    for i23 in range(0,3):
                            NArray23 = np.array(data)
                            self.MainTraingData.append([NArray23[i23],ans])
                elif ans[24] == 1:
                    data=pd.read_csv('./TraingData1000/24/item24.csv')
                    for i24 in range(0,33):
                            NArray24 = np.array(data)
                            self.MainTraingData.append([NArray24[i24],ans])
                elif ans[25] == 1:
                    data=pd.read_csv('./TraingData1000/25/item25.csv')
                    for i25 in range(0,4):
                            NArray25 = np.array(data)
                            self.MainTraingData.append([NArray25[i25],ans])
                elif ans[26] == 1:
                    data=pd.read_csv('./TraingData1000/26/item26.csv')
                    for i26 in range(0,5):
                            NArray26 = np.array(data)
                            self.MainTraingData.append([NArray26[i26],ans])
                elif ans[27] == 1:
                    data=pd.read_csv('./TraingData1000/27/item27.csv')
                    for i27 in range(0,27):
                            NArray27 = np.array(data)
                            self.MainTraingData.append([NArray27[i27],ans])
                elif ans[28] == 1:
                    data=pd.read_csv('./TraingData1000/28/item28.csv')
                    for i28 in range(0,24):
                            NArray28 = np.array(data)
                            self.MainTraingData.append([NArray28[i28],ans])
                else: 
                    ans[29] == 1
                    data=pd.read_csv('./TraingData1000/29/item30.csv')
                    for i29 in range(0,16):
                            NArray29 = np.array(data)
                            self.MainTraingData.append([NArray29[i29],ans])
        
    def show(self):
        print (self.MainTraingData[1])                                           #print data of PIC Set                                       
        ####

    def random(self,index=-1):                                              #upset the index of the set
        self.RandomData = self.MainTraingData                               #copy a set with MainTraingData
        random.shuffle(self.RandomData)                                     #upset the set
        if index == -1:
            return self.RandomData
        else:
            return self.RandomData[index]
        ####


    def batch(self,Num):
        if self.RandomData == []:                                           #if haven't upset pic set, initial Random array
            self.random()
        q_set=[]                                                            #data of pic
        a_set=[]                                                            #Answer of pic
        if self.PushIndex+Num>len(self.RandomData):                         #confirm the number of pics is enough
            print ("ERROR : Pic Set only have "+str(len(self.RandomData))+" pics")
            return 
        for i in self.RandomData[self.PushIndex:self.PushIndex+Num]:
            q_set.append(i[0])
            a_set.append(i[1])
        self.PushIndex += Num
        #print("push",self.PushIndex)
        return q_set,a_set
        ####
    def reset(self):
        self.RandomData = []                                                #PIC Set with Random
        self.PushIndex = 0                                                  #record of output  
        
        ####
'''
MP = PicSet()
MP.add('TraingData/0/1.jpg',1)
MP.add('TraingData/0/6.jpg',2)
MP.add('TraingData/0/11.jpg',3)
MP.add('TraingData/0/16.jpg',4)
MP.add('TraingData/0/21.jpg',5)
MP.add('TraingData/0/26.jpg',6)
MP.add('TraingData/0/31.jpg',7)
MP.add('TraingData/0/36.jpg',8)
MP.add('TraingData/0/41.jpg',9)
a1,a2 = MP.batch(3)
print a2
a1,a2 = MP.batch(3)
print a2
a1,a2 = MP.batch(3)
print a2
####


MP = PicSet()
MP.AddDir('./TraingData/')
a1,a2 = MP.batch(3)
print a2
a1,a2 = MP.batch(3)
print a2
a1,a2 = MP.batch(3)
print a2
a1,a2 = MP.batch(3)
print a2
a1,a2 = MP.batch(3)
print a2

'''

