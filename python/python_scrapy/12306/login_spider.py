"""
转自  https://github.com/Light-City/12306_spider

login_spider           # 登陆类 用于12306全局登陆与管理
    downloadCode       # 用于下载验证码
    verifi_Code        # 用于验证验证码是否输入成功
    main_Login         # 用于账户登陆
    get_Tk             # 登陆不成功的uamtk获取
    tk_Auth            # uamtk验证
    Login              # 真实登陆的跳转页面
    main               # 对上述代码的调用
ticker_spider
	get_StationName_En    # 获取出发站(抵达站)的字母简写
    search_Ticket       # 余票查询
    get_StationName     # 获取真实的中文表示的站点
    print_TicketInfo    # 打印余票查询结果
"""

"""
登录流程:
先执行downloadCode下载验证码，然后手动输入验证码坐标验证，然后输入账号密码登录，
然后获取并验证uamtk码，最后确实登录成功
接着search 余票信息，进行打印输出，适当加美化

涉及url较多:
code_url   = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.3090638747642678'
verifi_url = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
url_uamtk  = 'https://kyfw.12306.cn/passport/web/auth/uamtk'
uamauthclient_url = "https://kyfw.12306.cn/otn/uamauthclient"
login_url  = 'https://kyfw.12306.cn/passport/web/login'
login_url  = 'https://kyfw.12306.cn/otn/index/initMy12306'
"""


import requests

class login_spider(object):
    def __init__(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
        }
        sess = requests.Session()
        self.headers=headers
        self.sess = sess

    def downloadCode(self):
        # 此处本地如果已经有 img_code.jpg 先删掉，不然不是最新的验证码
        # TODO code_url 最后的小数部分在不断刷新，可以优化先获取小数部分，得到最新的验证码 不太明白它的原理，code_url不变但是每次图片都不一样
        code_url = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.3090638747642678'
        #  verify=False 参数必须
        res = self.sess.get(code_url, headers=self.headers, verify=False)
        print(res)  # <Response [200]>
        # print(res.text)
        # print(res.text.encode("utf8"))
        # print(res.text.encode("utf8").decode("utf8"))
        # print(res.json())
        if res.status_code == 200:
            with open('img_code.jpg', "wb") as f:
                f.write(res.content)
                print("验证码下载成功")
                return True
        else:
            print("图片下载失败,正在重试....")
            self.downloadCode()

    def verifi_Code(self):
        """
        先执行downloadCode下载验证码，然后手动输入验证码坐标验证，然后输入账号密码登录，
        然后获取并验证uamtk码，最后确实登录成功
        接着search 余票信息，进行打印输出，适当加美化
        :return: true or false
        """
        verifi_url = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
        verifi_axis = ['36,46','109,44','181,47','254,44','33,112','105,116','186,116','253,115']
        # 此处输入0-7数字即可，多张图片验证时连着输入
        axis = input("请输入验证码坐标>> ") # axis  is <class 'str'>
        verifi_list = []
        for point in axis:  # 遍历字符串
            verifi_list.append(verifi_axis[int(point)])
        # 比如输入14，则verifi_list = ['109,44','33,112']
        # axis_pos =  "109,44,33,112"  构造成提交的验证码表单的answer需要的格式
        axis_pos = ','.join(verifi_list)
        post_data = {
            "answer": axis_pos,
            "login_site": "E",
            "rand": "sjrand",
        }
        res = self.sess.post(url=verifi_url, headers=self.headers, data=post_data, verify=False)
        print(res) # <Response [200]>
        print(res.text.encode("utf8").decode("utf8")) # b'{"result_message":"验证码校验成功","result_code":"4"}'
        print(res.json()) # {'result_message': '验证码校验成功', 'result_code': '4'}
        res_json = res.json()
        if not res_json['result_code']=='4':
            print("验证失败")
            return False
        print(res_json)  # {'result_message': '验证码校验成功', 'result_code': '4'}
        return True

    def get_Tk(self):
        url_uamtk = 'https://kyfw.12306.cn/passport/web/auth/uamtk'
        data_uamtk = {"appid":"otn"}
        res = self.sess.post(url_uamtk, headers=self.headers, data=data_uamtk, verify=False)
        print(res) # <Response [200]>
        print(res.text.encode("utf8").decode("utf8"))
        # b'{"result_message":"验证通过","result_code":0,"apptk":null,"newapptk":"z4XfduPj4Ru5m4EMu-nBiJS3MJbl3rKmLvJjkgubq2q0"}'
        res_json = res.json()
        data_verifi = {"tk":res_json["newapptk"]}
        print(data_verifi)
        # {'tk': 'z4XfduPj4Ru5m4EMu-nBiJS3MJbl3rKmLvJjkgubq2q0'}
        return data_verifi

    def tk_Auth(self):
        uamauthclient_url = "https://kyfw.12306.cn/otn/uamauthclient"
        res = self.sess.post(uamauthclient_url, headers=self.headers, data=self.get_Tk(), verify=False)
        print(res) #<Response [200]>
        print(res.text.encode("utf8").decode("utf8"))
        #b'{"apptk":"z4XfduPj4Ru5m4EMu-nBiJS3MJbl3rKmLvJjkgubq2q0","result_code":0,"result_message":"验证通过","username":"你的姓名"}'

    def main_Login(self):  # 功能：预登陆，得到uamtk码。后续真正登录需要验证这个uamtk
        username = input("请输入您的12306账号: ")
        password = input("请输入您的12306密码: ")
        login_url = 'https://kyfw.12306.cn/passport/web/login'
        data_post = {
            "username": username,
            "password": password,
            "appid": "otn"
        }
        res = self.sess.post(login_url, headers=self.headers, data=data_post, verify=False)
        print(res.json())
        # {'result_message': '登录成功', 'result_code': 0, 'uamtk': 'ABYFVGHQsa9xtOD9ERFfaAG2NNcoOj5wotpeGgfsq2q0'}

    def login(self):
        login_url = 'https://kyfw.12306.cn/otn/index/initMy12306'
        res = self.sess.get(login_url, headers=self.headers, verify=False)
        print(res)

    def main(self):
        self.downloadCode()
        res = self.verifi_Code()
        if res==True:
            self.main_Login()
            self.tk_Auth()   # todo tk 与 uamtk 的区别
            self.login()
        else:
            print("验证失败！")
# 测试登陆 作为其他模块导入时，注释掉
# ls = login_spider()
# ls.main()
