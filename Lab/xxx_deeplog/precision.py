import pandas as pd


# read real_raw data 1000万
df_real_raw = pd.read_csv(r'D:/data analysis/200nodes/file/pattern_abnormal.log', header=None, sep=' ',
                          names=['log_key', 'abnormal'])
# 取 1000000+seq_len 之后的行  所有列
df_real_bef_rm = df_real_raw.iloc[1000010:, :]
print(df_real_bef_rm.shape)  # (    , 2)

df_real = df_real_bef_rm[~(df_real_bef_rm["log_key"].isin([30]) | df_real_bef_rm["log_key"].isin([31]) |
                           df_real_bef_rm["log_key"].isin([32]) | df_real_bef_rm["log_key"].isin([33]) |
                           df_real_bef_rm["log_key"].isin([34]))]
print(df_real.shape)  # (    , 2)
# 重置索引 从0开始
df_real_label = df_real.reset_index(drop=True)  # .iloc[:match_num,:][ "abnormal"]
print(df_real_label.shape)  # (    , 2)
#############################################
seq_len = 10
# 需要匹配的行数
match_num = (df_real_label.shape[0] - (seq_len + 1))
print("match_num  "+ str(match_num))  # 289904
##############################################
# read test result data
# 测试模型时已经去掉了log_key 30-34 不需要处理
# 跳过前几行 后几行 skiprows, skipfooter
df_result_label = pd.read_csv(r'D:/data analysis/DeepLog-master/result/anamoly_bsg.txt', header=None,
                        names=["pattern", "top_1", "top_2", "top_3", "abnormal"],
                        index_col=None, skiprows=[0, 1], skipfooter=1,
                        engine='python')  # sep=r'(\d+)(.*)({.*})(.*)(\d))'
print(df_result_label.shape)  # (289904, 5)
# print(df_result_label)
##############################################
# 比较 df_real 的前match_num行 和 df_result 的全部行 的abnormal列
# 取到 df_real 的前match_num行 的abnormal列
tp = 0
fp = 0
fn = 0
rem = 0
#
for i in range(match_num):
    # tp
    # .iloc[i, :]["abnormal"]   定位到某行某列
    if df_real_label.iloc[i, :]["abnormal"] == 1 and df_result_label.iloc[i, :]["abnormal"] == 1:
        tp += 1
    if df_real_label.iloc[i, :]["abnormal"] == 0 and df_result_label.iloc[i, :]["abnormal"] == 1:
        fp += 1
    if df_real_label.iloc[i, :]["abnormal"] == 1 and df_result_label.iloc[i, :]["abnormal"] == 0:
        fn += 1
    if df_real_label.iloc[i, :]["abnormal"] == 0 and df_result_label.iloc[i, :]["abnormal"] == 0:
        rem += 1

print("tp  " + str(tp) + "  fp  " + str(fp) + "  fn  " + str(fn) + "  rem  " + str(rem))
print("total  "+ str(tp + fp + fn + rem))

precision = round(tp / (tp + fp), 2)
print("precision  " + str(precision))
recall = round(tp / (tp + fn), 2)
print("recall  " + str(recall))
f_measure = 2 * precision * recall / (precision + recall)
print("f_measure  " + str(f_measure))

"""
(290000, 2)
(289915, 2)
(289915, 2)
match_num  289904
(289904, 5)
tp  1704  fp  29625  fn  8375  rem  250200
total  289904
precision  0.05
recal  0.17
f_measure  0.07727272727272727
"""
