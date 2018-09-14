```python
# -*- encoding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from threading import Thread

ACCOUNTS = {
    "account": "password"
#    ,"account2":"password2"
}


BUY_URL = 'https://detail.tmall.com/item.htm?spm=a230r.1.14.6.7a2f134b5Xo9h5&id=44425281296&cm_id=140105335569ed55e27b&abbucket=16'

LOGIN_URL = 'https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F'
# 登录成功手动确认URL
LOGIN_SUCCESS_CONFIRM = 'https://www.taobao.com/'
# 开始自动刷新等待抢购按钮出现的时间点,提前3分钟
BEGIN_GO = '2018-09-14 09:50:00'

cookie=''

# 进到购买页面后提交订单
def payOrder(driver, user):
    time.sleep(1)
    while BUY_URL == driver.current_url:
        print(user + ' 当前页面还在商品详情！！！')
        time.sleep(3)

    while True:
        try:
            submitOrder = driver.find_element_by_link_text('确认付款')
            submitOrder.click()
            print(user + ' 手动输入密码 点击支付吧！！！') # 由于没输入密码，上句无法执行，本句也不执行
            break
        except Exception as e:
            print(e)
            print(user + ' 没输入支付密码无法自动完成支付！！！！！')
            time.sleep(3)  # 到了订单提交页面提交不了订单一直等待
            print(user + ' 先不支付了')
            break
    while True:
        time.sleep(3)
        print(user + ' 进入睡眠3s')
        # pass
        break
    print(user + ' \033[31;1msuccess\033[0m')

# 提交订单
def submitOrder(driver, user):
    time.sleep(1)
    nowUrl = driver.current_url  # 确认订单信息页面,提交订单
    while True:
        try:
            tryAgain = driver.find_element_by_link_text('再试一次')
            tryAgain.click()
            print(user + ':再试一次点击')
            pass
        except:
            print(user + ' 跳转进入提交订单(确认订单信息)页面，10s后自动点击\033[31;1m提交订单\033[0m, 然后跳转到支付页面！')
            time.sleep(10)
            submit_order = driver.find_element_by_link_text('提交订单')
            submit_order.click()
            time.sleep(1)  # 排队中
            pass
        if nowUrl != driver.current_url:  # 跳到支付页面，此时确认订单信息页面 ！= 支付页面
            print(user + ' 正在跳转到支付页面......')
            break
    payOrder(driver, user)


# 登录成功去到购买页面
def goToBuy(driver, user):
    driver.get(BUY_URL)  # 自动登录BUY_URL页面
    print(user + ' 正在打开某一指定商品购买页面......')
    # 转换成抢购时间戳
    timeArray = time.strptime(BEGIN_GO, "%Y-%m-%d %H:%M:%S")

    timestamp = time.mktime(timeArray)
    # 未发现购买按钮
    no_found_buy = True
    while True:
        if time.time() > timestamp:  # 到了抢购时间
            try:
                buyButton = driver.find_element_by_link_text('立即购买')
                no_found_buy = False
                print(user + ' \033[31;1m立即购买\033[0m按钮找到了！！！')
                # 点击摩卡金
                # driver.find_element_by_xpath('//*[@id="pro-skus"]/dl[1]/div/ul/li[2]/div/a/p/span').click()
                # 点击6gb+128gb
                # driver.find_element_by_xpath('//*[@id="pro-skus"]/dl[3]/div/ul/li[2]/div/a/p/span').click()
                print(user + ' 自动勾选商品属性! ! !')

                type1=driver.find_element_by_link_text("黑色-圆线")
                type1.click()

                type2=driver.find_element_by_link_text("0.25M")
                type2.click()

                print(user + ' 10s后自动点击\033[31;1m立即购买\033[0m，正在跳到提交订单页面......')
                time.sleep(10)
                buyButton.click()
                break
            except:
                if no_found_buy:
                    time.sleep(0.3)
                    if BUY_URL == driver.current_url:  # 还在当前页面自动刷新
                        driver.get(BUY_URL)
                        pass
                    else:
                        print(user + '手动点击了申购')
                        break
                else:
                    print(user + ' 点击不了申购！！！！！！需要手动点击！！！！！')
                    time.sleep(0.5)
                    if BUY_URL != driver.current_url:
                        print(user + ' 手动点击了申购')
                        break
                    pass
        else:
            time.sleep(15)
            print(user + '睡眠15s，未到脚本开启时间：' + BEGIN_GO)
    submitOrder(driver, user)


# 登录商城,登陆成功后跳转至抢购页面
def loginMall(user, pwd):
    driver = webdriver.Chrome()
    driver.get(LOGIN_URL)            # 打开LOGIN_URL页面
    # 需要手动输入密码或者扫码登录，未写自动登录的代码
    print(user + ' 请扫码或输入密码登录： ')
    while True:
        time.sleep(1)
        # print('未输入密码，我在隔1秒循环1次，等输入密码后跳转')
        # 当前url driver.current_url='https://www.taobao.com/'时说明登录成功跳转到了首页
        if LOGIN_SUCCESS_CONFIRM == driver.current_url:
            print(user + ' \033[31;1m登录成功！\033[0m')
            break
    goToBuy(driver, user)


if __name__ == "__main__":
    # 账号密码
    data = ACCOUNTS
    # 构建线程
    threads = []
    for account, pwd in data.items():
        t = Thread(target=loginMall, args=(account, pwd,))
        threads.append(t)
        # 启动所有线程
    for thr in threads:
        time.sleep(2)
        thr.start()


```
```
account 请扫码或输入密码登录： 
account 登录成功！
account 正在打开某一指定商品购买页面......
account 立即购买按钮找到了！！！
account 自动勾选商品属性! ! !
account 10s后自动点击立即购买，正在跳到提交订单页面......
account 跳转进入提交订单(确认订单信息)页面，10s后自动点击提交订单, 然后跳转到支付页面！
account 正在跳转到支付页面......
Message: no such element: Unable to locate element: {"method":"link text","selector":"确认付款"}
  (Session info: chrome=69.0.3497.81)
  (Driver info: chromedriver=2.40.565498 (ea082db3280dd6843ebfb08a625e3eb905c4f5ab),platform=Windows NT 10.0.17134 x86_64)

account 没输入支付密码无法自动完成支付！！！！！
account 先不支付了
account 进入睡眠3s
account success
```
