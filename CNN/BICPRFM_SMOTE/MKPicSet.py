
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
    def Addtest(self,picdir= "./TraingData10/"):
        NArray = []
        NArray2 =[]
        for dirPath, dirNames, fileNames in os.walk(picdir):
           for f in fileNames:                        
                ans=[0,0]
                ans[int(dirPath[len(picdir):])]+=1
                if ans[0] == 1:
                    data=pd.read_csv('./TraingData10/0/unpur.csv')
                    for i in range(0,1144):
                        NArray = np.array(data)
                        self.MainTraingData.append([NArray[i],ans])
                        #self.MainTraingData.append([np.float(n) for n in NArray[i]],ans])
#                    print("dafdfdf = ",NArray[0])                        
                        #print ("array pic:",NArray[1660],"The Pic's Ans:",ans)
                else:
                    data=pd.read_csv('./TraingData10/1/pur.csv')
                    for j in range(0,1144):
                            NArray2 = np.array(data)
                            self.MainTraingData.append([NArray2[j],ans])
                #self.add(str(os.path.join(dirPath, f)),ans,x_size,y_size)
                #print ("add pic:",os.path.join(dirPath, f),"The Pic's Ans:",ans)
        
    def show(self):
        self.MainTraingData[1]
#        print ("ANS",self.MainTraingData[1])                                           #print data of PIC Set                                       
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
