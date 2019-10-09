import pandas as pd
import numpy as np
import tensorflow as tf

rnn_unit=10       #隱藏數量(自訂)
input_size=7 #BICPRFM
output_size=1 #YN
lr=0.0001         #學習率
#——————————————————import data ——————————————————————
f=open('2018_data_all_log.csv')
df=pd.read_csv(f)     #讀入資料
data=df.iloc[:,3:11].values  #取第3-10列(取頭不取尾)
tf.reset_default_graph()


#獲取訓練集 (做標準化)
def get_train_data(batch_size=10,time_step=5,train_begin=0,train_end=6630):
    batch_index=[]
    data_train=data[train_begin:train_end]
    normalized_train_data=(data_train-np.mean(data_train,axis=0))/np.std(data_train,axis=0)  #標準化
    train_x,train_y=[],[]   #訓練集
    for i in range(len(normalized_train_data)-time_step):
       if i % batch_size==0:
           batch_index.append(i)
#       x=normalized_train_data[i:i+time_step,:7]
       x=data_train[i:i+time_step,:7]
       y=data_train[i:i+time_step,7,np.newaxis]
       train_x.append(x.tolist())
       train_y.append(y.tolist())
    batch_index.append((len(normalized_train_data)-time_step))
    return batch_index,train_x,train_y


#測試集
def get_test_data(time_step=5,test_begin=6630):
    data_test=data[test_begin:]
    mean=np.mean(data_test,axis=0)
    std=np.std(data_test,axis=0)
    normalized_test_data=(data_test-mean)/std  #標準化
    size=(len(normalized_test_data)+time_step-1)//time_step  #有size個sample
    test_x,test_y=[],[]
    for i in range(size-1):
       x=normalized_test_data[i*time_step:(i+1)*time_step,:7]
       y=data_test[i*time_step:(i+1)*time_step,7]
       test_x.append(x.tolist())
       test_y.extend(y)
    test_x.append((normalized_test_data[(i+1)*time_step:,:7]).tolist())
    test_y.extend((data_test[(i+1)*time_step:,7]).tolist())
#    print(test_x)
    return mean,std,test_x,test_y


#——————————————————定義神經網絡變量——————————————————
#輸入層  輸出層權重  bias

weights={
         'in':tf.Variable(tf.random_normal([input_size,rnn_unit])),
         'out':tf.Variable(tf.random_normal([rnn_unit,1]))
        }
biases={
        'in':tf.Variable(tf.constant(0.1,shape=[rnn_unit,])),
        'out':tf.Variable(tf.constant(0.1,shape=[1,]))
       }

#——————————————————定義lstm——————————————————
def lstm(X):
    
    batch_size=tf.shape(X)[0]
    time_step=tf.shape(X)[1]
    
    w_in=weights['in']
    b_in=biases['in']
    input=tf.reshape(X,[-1,input_size])  #需要将tensor转成2维进行计算，计算后的结果作为隐藏层的输入
    input_rnn=tf.matmul(input,w_in)+b_in
    input_rnn=tf.reshape(input_rnn,[-1,time_step,rnn_unit])  #将tensor转成3维，作为lstm cell的输入
    
    cell=tf.nn.rnn_cell.BasicLSTMCell(rnn_unit)
    init_state=cell.zero_state(batch_size,dtype=tf.float32)
    
    output_rnn,final_states=tf.nn.dynamic_rnn(cell, input_rnn,initial_state=init_state, dtype=tf.float32)
    output=tf.reshape(output_rnn,[-1,rnn_unit]) 
    w_out=weights['out']
    b_out=biases['out']
    
    pred=tf.matmul(output,w_out)+b_out
    return pred,final_states

#————————————————訓練模型————————————————————

def train_lstm(batch_size=10,time_step=5,train_begin=0,train_end=6630):
    X=tf.placeholder(tf.float32, shape=[None,time_step,input_size])
    Y=tf.placeholder(tf.float32, shape=[None,time_step,output_size])
    batch_index,train_x,train_y=get_train_data(batch_size,time_step,train_begin,train_end)
    with tf.variable_scope("sec_lstm"):
        pred,final_states=lstm(X)
    loss=tf.reduce_mean(tf.square(tf.reshape(pred,[-1])-tf.reshape(Y, [-1])))
    train_op=tf.train.RMSPropOptimizer(lr).minimize(loss)
    saver=tf.train.Saver(tf.global_variables(),max_to_keep=15) #保存模型

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for i in range(1):     #迭代次數
            for step in range(len(batch_index)-1):
                _,loss_=sess.run([train_op,loss],feed_dict={X:train_x[batch_index[step]:batch_index[step+1]],Y:train_y[batch_index[step]:batch_index[step+1]]})
            if i % 25 == 0:
                print("Number of iterations:",i," loss:",loss_)
            
        print("model_save: ",saver.save(sess,'model_save2\\modle.ckpt'))
        print("The train has finished")
        print("train_x[0]",train_x[0])
        print("train_x_lenth",len(train_x[0]))


#————————————————預測模型————————————————————
def prediction(time_step=5):
    X=tf.placeholder(tf.float32, shape=[None,time_step,input_size])
    mean,std,test_x,test_y=get_test_data(time_step)
    with tf.variable_scope("sec_lstm",reuse=True):
        pred,_=lstm(X)
    saver=tf.train.Saver(tf.global_variables())
    with tf.Session() as sess:
        
        module_file = tf.train.latest_checkpoint('model_save2')
        saver.restore(sess, module_file)
        test_predict=[]
        for step in range(len(test_x)-1):
          prob=sess.run(pred,feed_dict={X:[test_x[step]]})
          predict=prob.reshape((-1))
          test_predict.extend(predict)
        test_y=np.array(test_y)
        test_predict=np.array(test_predict)     
        test_predict_2 = []
        for ans in test_predict:
            if ans >= 0.5:
                test_predict_2.append(1)
            else:
                test_predict_2.append(0)
        test_predict = test_predict_2
        acc=1-sum(np.abs(test_predict-test_y[:len(test_predict)]))/len(test_predict)  #偏差程度
        print("The accuracy of this predict:",acc)


train_lstm(10,5,0,6630)
prediction()