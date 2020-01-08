## 资源

[shell 入门](https://github.com/Snailclimb/JavaGuide/blob/master/%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/Shell.md)

[ C语言中文网 Linux学习教程，Linux入门教程（超详细）](http://c.biancheng.net/linux_tutorial/)

[ Linux命令行与shell脚本编程大全案例 fengyuhetao/shell ](https://github.com/fengyuhetao/shell)

[Advanced Bash-Scripting Guide
An in-depth exploration of the art of shell scripting
Mendel Cooper](http://tldp.org/LDP/abs/html/)，非常详细，非常易读，大量example，既可以当入门教材，也可以当做工具书查阅

[ qinjx Shell脚本编程30分钟入门 文末有其它资料链接 ](https://github.com/qinjx/30min_guides/blob/master/shell.md)

## IF 判断条件总结

> [IF 判断条件总结](https://www.jb51.net/article/56553.htm)
```sh
if [ -f file ]    # 如果 FILE 存在且是一个普通文件则为真
if [-z $2]        # 判断脚本的第2个参数是否为空
2>&1              # 2>&1  表示把 标准错误输出 重定向到 标准输出    https://yanbin.blog/linux-input-output-redirection/
                  # 标准输入(stdin)	0	  标准输出(stdout)	1     标准错误输出(stderr)	2
shift    # 位置参数可以用shift命令左移。比如shift 3表示原来的$4现在变成$1，原来的$5现在变成$2等等，原来的$1、$2、$3丢弃，$0不移动。

$#    # 是传给脚本的参数个数
$0    #  是脚本本身的名字
$1    是传递给该shell脚本的第一个参数
$2    是传递给该shell脚本的第二个参数
$@    是传给脚本的所有参数的列表
$*    是以一个单字符串显示所有向脚本传递的参数，与位置变量不同，参数可超过9个
$$    是脚本运行的当前进程ID号
$?    是显示最后命令的退出状态，0表示没有错误，其他表示有错误

1、字符串判断

str1 = str2　　　　　　当两个串有相同内容、长度时为真 
str1 != str2　　　　　 当串str1和str2不等时为真 
-n str1　　　　　　　 当串的长度大于0时为真(串非空) 
-z str1　　　　　　　 当串的长度为0时为真(空串) 
str1　　　　　　　　   当串str1为非空时为真

2、数字的判断

int1 -eq int2　　　　两数相等为真 
int1 -ne int2　　　　两数不等为真 
int1 -gt int2　　　　int1大于int2为真 
int1 -ge int2　　　　int1大于等于int2为真 
int1 -lt int2　　　　int1小于int2为真 
int1 -le int2　　　　int1小于等于int2为真

3、文件的判断

-r file　　　　　用户可读为真 
-w file　　　　　用户可写为真 
-x file　　　　　用户可执行为真 
-f file　　　　　文件为正规文件为真 
-d file　　　　　文件为目录为真 
-c file　　　　　文件为字符特殊文件为真 
-b file　　　　　文件为块特殊文件为真 
-s file　　　　　文件大小非0时为真 
-t file　　　　　当文件描述符(默认为1)指定的设备为终端时为真

4、复杂逻辑判断

-a 　 　　　　　 与 
-o　　　　　　　 或 
!　　　　　　　　非

5 附 表：

[ -a FILE ]  如果 FILE 存在则为真。  
[ -b FILE ]  如果 FILE 存在且是一个块特殊文件则为真。  
[ -c FILE ]  如果 FILE 存在且是一个字特殊文件则为真。  
[ -d FILE ]  如果 FILE 存在且是一个目录则为真。  
[ -e FILE ]  如果 FILE 存在则为真。  
[ -f FILE ]  如果 FILE 存在且是一个普通文件则为真。  
[ -g FILE ] 如果 FILE 存在且已经设置了SGID则为真。 [ -h FILE ]  如果 FILE 存在且是一个符号连接则为真。  
[ -k FILE ]  如果 FILE 存在且已经设置了粘制位则为真。  
[ -p FILE ]  如果 FILE 存在且是一个名字管道(F如果O)则为真。  
[ -r FILE ]  如果 FILE 存在且是可读的则为真。  
[ -s FILE ]  如果 FILE 存在且大小不为0则为真。  
[ -t FD ]  如果文件描述符 FD 打开且指向一个终端则为真。  
[ -u FILE ]  如果 FILE 存在且设置了SUID (set user ID)则为真。  
[ -w FILE ]  如果 FILE 如果 FILE 存在且是可写的则为真。  
[ -x FILE ]  如果 FILE 存在且是可执行的则为真。  
[ -O FILE ]  如果 FILE 存在且属有效用户ID则为真。  
[ -G FILE ]  如果 FILE 存在且属有效用户组则为真。  
[ -L FILE ]  如果 FILE 存在且是一个符号连接则为真。  
[ -N FILE ]  如果 FILE 存在 and has been mod如果ied since it was last read则为真。  
[ -S FILE ]  如果 FILE 存在且是一个套接字则为真。  
[ FILE1 -nt FILE2 ]  如果 FILE1 has been changed more recently than FILE2, or 如果 FILE1 exists and FILE2 does not则为真。  
[ FILE1 -ot FILE2 ]  如果 FILE1 比 FILE2 要老, 或者 FILE2 存在且 FILE1 不存在则为真。  
[ FILE1 -ef FILE2 ]  如果 FILE1 和 FILE2 指向相同的设备和节点号则为真。  
[ -o OPTIONNAME ]  如果 shell选项 “OPTIONNAME” 开启则为真。  
[ -z STRING ]  “STRING” 的长度为零则为真。  
[ -n STRING ] or [ STRING ]  “STRING” 的长度为非零 non-zero则为真。  
[ STRING1 == STRING2 ]  如果2个字符串相同。 “=” may be used instead of “==” for strict POSIX compliance则为真。  
[ STRING1 != STRING2 ]  如果字符串不相等则为真。 
[ STRING1 < STRING2 ]  如果 “STRING1” sorts before “STRING2” lexicographically in the current locale则为真。  
[ STRING1 > STRING2 ]  如果 “STRING1” sorts after “STRING2” lexicographically in the current locale则为真。  
[ ARG1 OP ARG2 ] “OP” is one of -eq, -ne, -lt, -le, -gt or -ge. These arithmetic binary operators return true if “ARG1” is equal to, not equal to, less than, less than or equal to, greater than, or greater than or equal to “ARG2”, respectively. “ARG1” and “ARG2” are integers.
```

> /dev/null 2>&1
```sh
0:表示键盘输入(stdin)
1:表示标准输出(stdout),系统默认是1 
2:表示错误输出(stderr)

command >/dev/null 2>&1 &  == command 1>/dev/null 2>&1 &
# > 代表重定向  &代表等于

1)command:表示shell命令或者为一个可执行程序
2)>:表示重定向到哪里 
3)/dev/null:表示Linux的空设备文件 
4)2:表示标准错误输出
5)&1:&表示等同于的意思,2>&1,表示2的输出重定向等于于1
6)&:表示后台执行,即这条指令执行在后台运行


1>/dev/null:表示标准输出重定向到空设备文件,也就是不输出任何信息到终端,不显示任何信息。
2>&1:表示标准错误输出重定向等同于标准输出,因为之前标准输出已经重定向到了空设备文件,所以标准错误输出也重定向到空设备文件。


这条命令的意思就是【在后台执行这个程序,并将错误输出2重定向到标准输出1,然后将标准输出1全部放到/dev/null文件,也就是清空】
所以可以看出" >/dev/null 2>&1 "常用来避免shell命令或者程序等运行中有内容输出。

结合 wget使用的例子:
wget -O /dev/null -o /dev/null example.com
#Here -O sends the downloaded file to /dev/null and -o logs to /dev/null instead of stderr.
```

> ${ } 替换
```sh
假设我们定义了一个变量为：
file=/dir1/dir2/dir3/my.file.txt
我们可以用 ${ } 分别替换获得不同的值：
${file#*/}：拿掉第一条 / 及其左边的字符串：dir1/dir2/dir3/my.file.txt
${file##*/}：拿掉最后一条 / 及其左边的字符串：my.file.txt
${file#*.}：拿掉第一个 . 及其左边的字符串：file.txt
${file##*.}：拿掉最后一个 . 及其左边的字符串：txt
${file%/*}：拿掉最后条 / 及其右边的字符串：/dir1/dir2/dir3
${file%%/*}：拿掉第一条 / 及其右边的字符串：(空值)
${file%.*}：拿掉最后一个 . 及其右边的字符串：/dir1/dir2/dir3/my.file
${file%%.*}：拿掉第一个 . 及其右边的字符串：/dir1/dir2/dir3/my

记忆的方法为：

# 是去掉左边(在鉴盘上 # 在 $ 之左边)

% 是去掉右边(在鉴盘上 % 在 $ 之右边)

单一符号是最小匹配﹔两个符号是最大匹配。


${file:0:5}：提取最左边的 5 个字节：/dir1
${file:5:5}：提取第 5 个字节右边的连续 5 个字节：/dir2
我们也可以对变量值里的字符串作替换：
${file/dir/path}：将第一个 dir 提换为 path：/path1/dir2/dir3/my.file.txt
${file//dir/path}：将全部 dir 提换为 path：/path1/path2/path3/my
```

## 10 个实战及面试常用 Shell 脚本编写

注意事项

1）开头加解释器：#!/bin/bash

2）语法缩进，使用四个空格；多加注释说明。

3）命名建议规则：变量名大写、局部变量小写，函数名小写，名字体现出实际作用。

4）默认变量是全局的，在函数中变量local指定为局部变量，避免污染其他作用域。

5）有两个命令能帮助我调试脚本：set -e 遇到执行非0时退出脚本，set-x 打印执行过程。

6）写脚本一定先测试再到生产上。

#### 前言
```shell
num=$(echo "scale=2; 10 / 3" | bc)
echo $num
# 3.33
```


#### 1 获取随机字符串或数字

```shell
#获取随机8位字符串：


#方法1：
 echo $RANDOM |md5sum |cut -c 1-8
471b94f2
#方法2：
 openssl rand -base64 4
vg3BEg==
#方法3：
 cat /proc/sys/kernel/random/uuid |cut -c 1-8
ed9e032c

#获取随机8位数字：


#方法1：
 echo $RANDOM |cksum |cut -c 1-8
23648321
#方法2：
 openssl rand -base64 4 |cksum |cut -c 1-8
38571131
#方法3：
 date +%N |cut -c 1-8
69024815


cksum：打印CRC效验和统计字节

```

#### 2 定义一个颜色输出字符串函数

```shell
#方法1：
function echo_color() {
    if [ $1 == "green" ]; then
        echo -e "\033[32;40m$2\033[0m"
    elif [ $1 == "red" ]; then
        echo -e "\033[31;40m$2\033[0m"
    fi
}
#方法2：
function echo_color() {
    case $1 in
        green)
            echo -e "\033[32;40m$2\033[0m"
            ;;
        red)
            echo -e "\033[31;40m$2\033[0m" 
            ;;
        *) 
            echo "Example: echo_color red string"
    esac
}
echo_color green "output this str in green color or red color"
echo_color red   "output this str in green color or red color"


# function关键字定义一个函数，可加或不加。
```


#### 3 批量创建用户

```shell
#!/bin/bash
DATE=$(date +%F_%T)
USER_FILE=user.txt
echo_color(){
    if [ $1 == "green" ]; then
        echo -e "\033[32;40m$2\033[0m"
    elif [ $1 == "red" ]; then
        echo -e "\033[31;40m$2\033[0m"
    fi
}
# 如果用户文件存在并且大小大于0就备份
if [ -s $USER_FILE ]; then
    mv $USER_FILE ${USER_FILE}-${DATE}.bak
    echo_color green "$USER_FILE exist, rename ${USER_FILE}-${DATE}.bak"
fi
echo -e "User\tPassword" >> $USER_FILE
echo "----------------" >> $USER_FILE
for USER in user{1..10}; do
    if ! id $USER &>/dev/null; then
        PASS=$(echo $RANDOM |md5sum |cut -c 1-8)
        useradd $USER
        echo $PASS |passwd --stdin $USER &>/dev/null
        echo -e "$USER\t$PASS" >> $USER_FILE
        echo "$USER User create successful."
    else
        echo_color red "$USER User already exists!"
    fi
done
```
#### 4 检查软件包是否安装

```shell
#!/bin/bash
if rpm -q sysstat &>/dev/null; then
    echo "sysstat is already installed."
else
    echo "sysstat is not installed!"
fi
```
#### 5 检查服务状态

```shell
#!/bin/bash
PORT_C=$(ss -anu |grep -c 123)
PS_C=$(ps -ef |grep ntpd |grep -vc grep)
if [ $PORT_C -eq 0 -o $PS_C -eq 0 ]; then
    echo "内容" | mail -s "主题" dst@example.com
fi
```
#### 6 检查主机存活状态

```shell
方法1：将错误IP放到数组里面判断是否ping失败三次


#!/bin/bash  
IP_LIST="192.168.18.1 192.168.1.1 192.168.18.2"
for IP in $IP_LIST; do
    NUM=1
    while [ $NUM -le 3 ]; do
        if ping -c 1 $IP > /dev/null; then
            echo "$IP Ping is successful."
            break
        else
            # echo "$IP Ping is failure $NUM"
            FAIL_COUNT[$NUM]=$IP
            let NUM++
        fi
    done
    if [ ${#FAIL_COUNT[*]} -eq 3 ];then
        echo "${FAIL_COUNT[1]} Ping is failure!"
        unset FAIL_COUNT[*]
    fi
done

方法2：将错误次数放到FAIL_COUNT变量里面判断是否ping失败三次


#!/bin/bash  
IP_LIST="192.168.18.1 192.168.1.1 192.168.18.2"
for IP in $IP_LIST; do
    FAIL_COUNT=0
    for ((i=1;i<=3;i++)); do
        if ping -c 1 $IP >/dev/null; then
            echo "$IP Ping is successful."
            break
        else
            # echo "$IP Ping is failure $i"
            let FAIL_COUNT++
        fi
    done
    if [ $FAIL_COUNT -eq 3 ]; then
        echo "$IP Ping is failure!"
    fi
done

方法3：利用for循环将ping通就跳出循环继续，如果不跳出就会走到打印ping失败


#!/bin/bash
ping_success_status() {
    if ping -c 1 $IP >/dev/null; then
        echo "$IP Ping is successful."
        continue
    fi
}
IP_LIST="192.168.18.1 192.168.1.1 192.168.18.2"
for IP in $IP_LIST; do
    ping_success_status
    ping_success_status
    ping_success_status
    echo "$IP Ping is failure!"
done
```
#### 7 监控CPU、内存和硬盘利用率

```shell
1）CPU


借助vmstat工具来分析CPU统计信息。



#!/bin/bash
DATE=$(date +%F" "%H:%M)
IP=$(ifconfig eth0 |awk -F '[ :]+' '/inet addr/{print $4}')  # 只支持CentOS6
MAIL="example@mail.com"
if ! which vmstat &>/dev/null; then
    echo "vmstat command no found, Please install procps package." 
    exit 1
fi
US=$(vmstat |awk 'NR==3{print $13}')
SY=$(vmstat |awk 'NR==3{print $14}')
IDLE=$(vmstat |awk 'NR==3{print $15}')
WAIT=$(vmstat |awk 'NR==3{print $16}')
USE=$(($US+$SY))
if [ $USE -ge 50 ]; then
    echo "
    Date: $DATE
    Host: $IP
    Problem: CPU utilization $USE
    " | mail -s "CPU Monitor" $MAIL
fi

2）内存


#!/bin/bash
DATE=$(date +%F" "%H:%M)
IP=$(ifconfig eth0 |awk -F '[ :]+' '/inet addr/{print $4}')  
MAIL="example@mail.com"
TOTAL=$(free -m |awk '/Mem/{print $2}')
USE=$(free -m |awk '/Mem/{print $3-$6-$7}')
FREE=$(($TOTAL-$USE))
# 内存小于1G发送报警邮件
if [ $FREE -lt 1024 ]; then
    echo "
    Date: $DATE
    Host: $IP
    Problem: Total=$TOTAL,Use=$USE,Free=$FREE
    " | mail -s "Memory Monitor" $MAIL
fi

3）硬盘


#!/bin/bash
DATE=$(date +%F" "%H:%M)
IP=$(ifconfig eth0 |awk -F '[ :]+' '/inet addr/{print $4}')  
MAIL="example@mail.com"
TOTAL=$(fdisk -l |awk -F'[: ]+' 'BEGIN{OFS="="}/^Disk \/dev/{printf "%s=%sG,",$2,$3}')
PART_USE=$(df -h |awk 'BEGIN{OFS="="}/^\/dev/{print $1,int($5),$6}')
for i in $PART_USE; do
    PART=$(echo $i |cut -d"=" -f1)
    USE=$(echo $i |cut -d"=" -f2)
    MOUNT=$(echo $i |cut -d"=" -f3)
    if [ $USE -gt 80 ]; then
        echo "
        Date: $DATE
        Host: $IP
        Total: $TOTAL
        Problem: $PART=$USE($MOUNT)
        " | mail -s "Disk Monitor" $MAIL
    fi
done
```
#### 8 批量主机磁盘利用率监控

```shell
前提监控端和被监控端SSH免交互登录或者密钥登录。



写一个配置文件保存被监控主机SSH连接信息，文件内容格式：IP User Port



#!/bin/bash
HOST_INFO=host.info
for IP in $(awk '/^[^#]/{print $1}' $HOST_INFO); do
    USER=$(awk -v ip=$IP 'ip==$1{print $2}' $HOST_INFO)
    PORT=$(awk -v ip=$IP 'ip==$1{print $3}' $HOST_INFO)
    TMP_FILE=/tmp/disk.tmp
    ssh -p $PORT $USER@$IP 'df -h' > $TMP_FILE
    USE_RATE_LIST=$(awk 'BEGIN{OFS="="}/^\/dev/{print $1,int($5)}' $TMP_FILE)
    for USE_RATE in $USE_RATE_LIST; do
        PART_NAME=${USE_RATE%=*}
        USE_RATE=${USE_RATE#*=}
        if [ $USE_RATE -ge 80 ]; then
            echo "Warning: $PART_NAME Partition usage $USE_RATE%!"
        fi
    done
done
```
#### 9 检查网站可用性

```shell
1）检查URL可用性


方法1：
check_url() {
    HTTP_CODE=$(curl -o /dev/null --connect-timeout 3 -s -w "%{http_code}" $1)
    if [ $HTTP_CODE -ne 200 ]; then
        echo "Warning: $1 Access failure!"
    fi
}
方法2：
check_url() {
if ! wget -T 10 --tries=1 --spider $1 >/dev/null 2>&1; then  
#-T超时时间，--tries尝试1次，--spider爬虫模式
        echo "Warning: $1 Access failure!"
    fi
}


使用方法：check_url www.baidu.com



2）判断三次URL可用性


思路与上面检查主机存活状态一样。



方法1：利用循环技巧，如果成功就跳出当前循环，否则执行到最后一行
#!/bin/bash  
check_url() {
    HTTP_CODE=$(curl -o /dev/null --connect-timeout 3 -s -w "%{http_code}" $1)
    if [ $HTTP_CODE -eq 200 ]; then
        continue
    fi
}
URL_LIST="www.baidu.com www.agasgf.com"
for URL in $URL_LIST; do
    check_url $URL
    check_url $URL
    check_url $URL
    echo "Warning: $URL Access failure!"
done
方法2：错误次数保存到变量
#!/bin/bash  
URL_LIST="www.baidu.com www.agasgf.com"
for URL in $URL_LIST; do
    FAIL_COUNT=0
    for ((i=1;i<=3;i++)); do
        HTTP_CODE=$(curl -o /dev/null --connect-timeout 3 -s -w "%{http_code}" $URL)
        if [ $HTTP_CODE -ne 200 ]; then
            let FAIL_COUNT++
        else
            break
        fi
    done
    if [ $FAIL_COUNT -eq 3 ]; then
        echo "Warning: $URL Access failure!"
    fi
done
方法3：错误次数保存到数组
#!/bin/bash  
URL_LIST="www.baidu.com www.agasgf.com"
for URL in $URL_LIST; do
    NUM=1
    while [ $NUM -le 3 ]; do
        HTTP_CODE=$(curl -o /dev/null --connect-timeout 3 -s -w "%{http_code}" $URL)
        if [ $HTTP_CODE -ne 200 ]; then
            FAIL_COUNT[$NUM]=$IP  #创建数组，以$NUM下标，$IP元素
            let NUM++
        else
            break
        fi
    done
    if [ ${#FAIL_COUNT[*]} -eq 3 ]; then
        echo "Warning: $URL Access failure!"
        unset FAIL_COUNT[*]    #清空数组
    fi
done
```
#### 10 检查MySQL主从同步状态
```shell

#!/bin/bash  
USER=bak
PASSWD=123456
IO_SQL_STATUS=$(mysql -u$USER -p$PASSWD -e 'show slave status\G' |awk -F: '/Slave_.*_Running/{gsub(": ",":");print $0}')  #gsub去除冒号后面的空格
for i in $IO_SQL_STATUS; do
    THREAD_STATUS_NAME=${i%:*}
    THREAD_STATUS=${i#*:}
    if [ "$THREAD_STATUS" != "Yes" ]; then
        echo "Error: MySQL Master-Slave $THREAD_STATUS_NAME status is $THREAD_STATUS!"
    fi
done
```
## 10 个方便的 Bash 别名
```shell
#1、 你有几次遇到需要解压 .tar 文件但无法记住所需的确切参数？别名可以帮助你！只需将以下内容添加到 .bash_profile 中，然后使用 untar FileName 解压缩任何 .tar 文件。

alias untar='tar -zxvf '

#2、 想要下载的东西，但如果出现问题可以恢复吗？

alias wget='wget -c '

#3、 是否需要为新的网络帐户生成随机的 20 个字符的密码？没问题。

alias getpass="openssl rand -base64 20"

#4、 下载文件并需要测试校验和？我们也可做到。

alias sha='shasum -a 256 '

#5、 普通的 ping 将永远持续下去。我们不希望这样。相反，让我们将其限制在五个 ping。

alias ping='ping -c 5'

#6、 在任何你想要的文件夹中启动 Web 服务器。

alias www='python -m SimpleHTTPServer 8000'

#7、 想知道你的网络有多快？只需下载 Speedtest-cli 并使用此别名即可。你可以使用 speedtest-cli --list 命令选择离你所在位置更近的服务器。

alias speed='speedtest-cli --server 2406 --simple'

#8、 你有多少次需要知道你的外部 IP 地址，但是不知道如何获取？我也是。

alias ipe='curl ipinfo.io/ip'

#9、 需要知道你的本地 IP 地址？

alias ipi='ipconfig getifaddr en0'

#10、 最后，让我们清空屏幕。

alias c='clear'

```
