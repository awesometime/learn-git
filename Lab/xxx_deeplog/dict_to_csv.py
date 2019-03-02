import pandas as pd
import os
import json


class TO_CSV():

    def get_file_name(self, file_dir):
        for root, dirs, raw_files in os.walk(file_dir):
            files = []
            for name in raw_files:
                # 只对  SX  开头的文件进行处理
                if name.startswith("SX"):
                    files.append(name)
            return files

    def dict_to_df(self, root_dir, files):
        i = 0
        list_ini = []
        for name in files:
            with open(root_dir + name, encoding='utf-8') as file:
                # 整个文件读成 str 组成的 list
                for line in file.readlines():
                    # loads 成 dict  dict 的键都一样
                    dic = json.loads(line)
                    # 将dict添加到列表list中
                    list_ini.append(dic)
            # print(list_ini)
            # 将键一样的字典组成的list 传入DataFrame 构造DataFrame
            df = pd.DataFrame(list_ini)
            # 打印为处理的原始DataFrame的行列
            print(df.shape)
            # 将列全空的列处理掉
            df = df.dropna(axis=1, how='all')
            # 打印处理后的DataFrame的行列
            print(df.shape)
            df.to_csv(root_dir + name + ".csv")
            i += 1
            print("ok-------------file---{}\n".format(i))
        print('all ok')


def main():
    root_dir = "D:\\date analysis\\12_12\\111\\"
    toto = TO_CSV()
    files = toto.get_file_name(root_dir)
    toto.dict_to_df(root_dir, files)


if __name__ == "__main__":
    main()
