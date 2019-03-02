import pandas as pd
import lstm_model
import logkey_analomy_detect
import process_data
import time
from keras.utils import np_utils
import os
import warnings


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Hide messy TensorFlow warnings
warnings.filterwarnings("ignore")  # Hide messy Numpy warnings


def main(row):
    global_start_time = time.time()

    seq_len = 10        # 训练sequence长度
    #split_rate = 0.1     # 划分训练数据和测试数据的比例
    # df1 = df1.sort_values(by='time')
    # df1 = df1.head(3000000)      # 自己机器运行报memery error错，因此用前300000条运行

    print("read data ok")
    data = list(df['log_key'].values)

    X_train, y_train, X_test, y_test, row = process_data.process_data(data, seq_len, row )#, split_rate)   # 对数据格式进行处理，对数据进行划分为训练数据和测试数据
    print("split data ok")
    # one-hot  0 1
    y_train = np_utils.to_categorical(y_train)

    params = {
        'lstm_output_dim': 50,
        'activation_lstm': 'relu',
        'activation_dense': 'relu',
        'activation_last': 'softmax',
        'dense_layer': 1,
        'lstm_layer': 2,
        'nb_epoch': 100
    }
    # 实例化  初始化
    obj_lstm = lstm_model.RNN_network(**params)
    print("initial obj ok ")

    # 调用模型进行训练
    obj_lstm.model(X_train, y_train, X_test, y_test, model_save_path=r'result\model_bsg')
    print("\n train model ok")

    # 调用模型预测
    predict_class, class_pro = obj_lstm.prediction(X_test, model_save_path=r'result\model_bsg')
    print("\npredict_class.shape" + str(predict_class.shape))
    print("\nclass_pro.shape" +str(class_pro.shape))
    print("\npredict model ok")
    print("\npredict time " + str(time.time()-global_start_time))

    top_g = 9
    logkey_analomy_detect.analomy_detec(y_test, class_pro, top_g, outputfile=r'result\anamoly_bsg.txt')     # 异常检测
    #
    print("analomy_detect time " + str(time.time()-global_start_time))

if __name__ == '__main__':
    # read raw data
    df1 = pd.read_csv(r'D:/data analysis/200nodes/file/pattern_abnormal.log', header=None, sep=' ',
                      names=['log_key', 'abnormal'])
    print(df1.shape)  # (1k w, 2)

    df2 = df1.iloc[:1000000, :]
    print(df2.shape)  # (100000, 2)

    # df3 为前100万 去掉 1 去掉 30-34
    df3 = df2[~(df2["log_key"].isin([30]) | df2["log_key"].isin([31]) | df2["log_key"].isin([32]) |
                df2["log_key"].isin([33]) | df2["log_key"].isin([34]) | df2["abnormal"].isin([1]))]
    print("train num  " + str(df3.shape))
    # train 个数
    row = df3.shape[0]
    print("row num  " + str(row))

    # 除去100万后   剩余的   只去掉 30-34
    df4 = df1.iloc[1000000:, :]
    print(df4.shape)
    df5 = df4[~(df4["log_key"].isin([30]) | df4["log_key"].isin([31]) | df4["log_key"].isin([32]) |
                df4["log_key"].isin([33]) | df4["log_key"].isin([34]))]
    print("test num  " + str(df5.shape))
    # 两df append
    df = df3.append(df5)
    print("total num  " + str(df.shape)+ "\n")

    # 传入 df row
    main(row)
