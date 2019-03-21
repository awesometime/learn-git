Oxx_URL=http://com/fanghuchengxu/
Cxx_Axxx=*.tar

function getImage()
{
	#from where, name
	#echo "get image"
	# 将下载的文件存放到指定的文件夹下，同时重命名下载的文件，利用-O;-o 指定log
	wget -O ${Cxx_Axxx} -o wget.log ${Oxx_URL}${Cxx_Axxx}
}
function installImage()
{
	docker load -i ${Cxx_Axxx}
	rm ${Cxx_Axxx}
}

function getVersion()
{
	docker images | grep fanghu | awk '{print $2;exit}'
}

function newAxxx()
{
	selectquyu
	# $? 最后命令的退出状态，0表示没有错误，其他表示有错误
	quyuID=$?
	# -eq 两数相等为真
	#if [ ${quyuID} -eq 6 ]; then
	docker run -d -v /etc:/usr/local/fanghuchengxu/mnt/etc:ro -v /usr:/usr/local/fanghuchengxu/mnt/usr:ro -v /var/lib/docker:/var/lib/docker:ro -v /var/run/docker.sock:/var/run/docker.sock:ro --net=host --pid=host --cap-add=NET_ADMIN  --cap-add=SYS_ADMIN  --cap-add=SYS_PTRACE  --cap-add AUDIT_CONTROL  --cpu-period=100000 --cpu-quota=20000 --restart=always --env CSS_MASTER_ADDR="https://100.125.2.145:443/hostmgr/websocket" fanghu:$1
	#fi
}

function stopAxxx()
{
	cids=`docker ps | grep fanghu | awk '{print $1;exit}'`
	for cid in ${cids}
	do
		docker stop $cid
		docker rm $cid
	done
}
function removeAxxx()
{
	cids=`docker ps -a | grep fanghu | awk '{print $1}'`
	for cid in $cids
	do
		docker stop ${cid}
		docker rm ${cid}
	done
}

function removeImage()
{
	imgids=`docker images | grep fanghu | awk '{print $3}'`
	for imgid in $imgids
	do
		docker rmi $imgid
	done
}
function installAxxx()
{
	getImage
	ret=$?
	# -ne 两数不等为真
	if [ $ret -ne 0 ]; then
		exit
	fi
	stopAxxx
	removeAxxx
	removeImage
	installImage
	version=`getVersion`
	newAxxx $version
}
function installDep()
{
	# 将错误输出2重定向到标准输出1,然后将标准输出1全部放到/dev/null文件 即清空
	yum --version > /dev/null 2>&1
	if [ $? -eq 0 ]; then
		wget --version > /dev/null 2>&1
		if [ $? -ne 0 ]; then
			yum -y install wget
		fi
		curl --version > /dev/null 2>&1
		# 上一条有错  不为0   执行
		if [ $? -ne 0 ]; then
			yum -y install curl
		fi
		sha256sum --version > /dev/null 2>&1
		if [ $? -ne 0 ]; then
			yum -y install sha256sum
		fi
	fi
	apt-get --version > /dev/null 2>&1
	if [ $? -eq 0 ]; then
		apt-get update
		wget --version > /dev/null 2>&1
		if [ $? -ne 0 ]; then
			apt-get -y install wget
		fi
		curl --version > /dev/null 2>&1
		if [ $? -ne 0 ]; then
			apt-get -y install curl
		fi
		sha256sum --version > /dev/null 2>&1
		if [ $? -ne 0 ]; then
			apt-get -y install sha256sum
		fi
	fi
}
function selectquyu()
{
	return 6
	curl -k --connect-timeout 4 https://host/version > /dev/null 2>&1
	if [ $? -eq 0 ]; then
			return 1
	fi
	curl -k --connect-timeout 4 https://host/version > /dev/null 2>&1
	if [ $? -eq 0 ]; then
			return 2
	fi
	curl -k --connect-timeout 4 https://host/version > /dev/null 2>&1
	if [ $? -eq 0 ]; then
			return 3
	fi
	curl -k --connect-timeout 4 https://host/version > /dev/null 2>&1
	if [ $? -eq 0 ]; then
			return 4
	fi
	echo "[ERROR] can't connect to server. Please check Security Group setting."
	return 5
}



if [ $# -eq 0 ]; then
#	echo "install"
	installAxxx
	echo "Sucessed install fanghu"
	exit
fi
if [ $1 == 'unstall' ]; then
	stopAxxx
	removeAxxx
	removeImage
	echo "Sucessed remove fanghu"
	exit
fi
