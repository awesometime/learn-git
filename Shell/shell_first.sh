#!/bin/bash
OBS_URL=http://obs.cn-north-5.myhuaweicloud.com/xss-name-5/
RPM_TAR_PACKAGE161=xss_linux64_rpm_cn-north-5.tar.gz
DEB_TAR_PACKAGE161=xss_linux64_deb_cn-north-5.tar.gz
TAR_TAR_PACKAGE161=xss_linux64_tar_cn-north-5.tar.gz
RPM_TAR_PACKAGE76=xss_linux64_rpm_cn-north-6.tar.gz
DEB_TAR_PACKAGE76=xss_linux64_deb_cn-north-6.tar.gz
TAR_TAR_PACKAGE76=xss_linux64_tar_cn-north-6.tar.gz
function installDep()
{
	yum --version > /dev/null 2>&1
	if [ $? -eq 0 ]; then
		wget --version > /dev/null 2>&1
		if [ $? -ne 0 ]; then
			yum -y install wget
		fi
		curl --version > /dev/null 2>&1
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
function selectRegion()
{
	curl -k --connect-timeout 4 https://XXXX > /dev/null 2>&1
	if [ $? -eq 0 ]; then
			return 1
	fi
	curl -k --connect-timeout 4 https://XXXX > /dev/null 2>&1
	if [ $? -eq 0 ]; then
			return 2
	fi
	echo "[ERROR] can't connect to server. Please check Security Group setting."
	return 3
}
function installRPM()
{
	selectRegion
	regionID=$?
	if [ ${regionID} -eq 1 ]; then
		wget ${OBS_URL}${RPM_TAR_PACKAGE161}
		if [ $? -ne 0 ]; then
			echo "[ERROR] Can't download package."
			return 1
		fi
		wget ${OBS_URL}${RPM_TAR_PACKAGE161}.sha256
		if [ $? -ne 0 ]; then
			echo "[ERROR] Can't download sha256 file."
			return 1
		fi
		sha256=`sha256sum ${RPM_TAR_PACKAGE161}`
		file_sha256=`cat ${RPM_TAR_PACKAGE161}.sha256`
		if [ "${sha256}" != "${file_sha256}" ]; then
			echo "[ERROR] package have been changed."
			return 1
		fi
		tar -zxvf ${RPM_TAR_PACKAGE161} > /dev/null 2>&1
		if [ $? -ne 0 ]; then
			echo "[ERROR] Decompression package failed."
			return 1
		fi
	fi
	if [ ${regionID} -eq 2 ]; then
		wget ${OBS_URL}${RPM_TAR_PACKAGE76}
		if [ $? -ne 0 ]; then
			echo "[ERROR] Can't download package."
			return 1
		fi
		wget ${OBS_URL}${RPM_TAR_PACKAGE76}.sha256
		if [ $? -ne 0 ]; then
			echo "[ERROR] Can't download sha256 file."
			return 1
		fi
		sha256=`sha256sum ${RPM_TAR_PACKAGE76}`
		file_sha256=`cat ${RPM_TAR_PACKAGE76}.sha256`
		if [ "${sha256}" != "${file_sha256}" ]; then
			echo "[ERROR] package have been changed."
			return 1
		fi
		tar -zxvf ${RPM_TAR_PACKAGE76} > /dev/null 2>&1
		if [ $? -ne 0 ]; then
			echo "[ERROR] Decompression package failed."
			return 1
		fi
	fi
	
	if [ ${regionID} -eq 3 ]; then
		return 1
	fi
	
	rpm -ivh xss_XSS_xss_Linux*.rpm
	if [ $? -ne 0 ]; then
		echo "[ERROR] Install rpm package failed."
		return 1
	fi
	echo "install rpm package successed."
	return 0
}

function installDEB()
{
	selectRegion
	regionID=$?
	if [ ${regionID} -eq 1 ]; then
		wget ${OBS_URL}${DEB_TAR_PACKAGE161}
		if [ $? -ne 0 ]; then
			echo "[ERROR] Can't download package."
			return 1
		fi
		wget ${OBS_URL}${DEB_TAR_PACKAGE161}.sha256
		if [ $? -ne 0 ]; then
			echo "[ERROR] Can't download sha256 file."
			return 1
		fi
		sha256=`sha256sum ${DEB_TAR_PACKAGE161}`
		file_sha256=`cat ${DEB_TAR_PACKAGE161}.sha256`
		if [ "${sha256}" != "${file_sha256}" ]; then
			echo "[ERROR] package have been changed."
			return 1
		fi
		tar -zxvf ${DEB_TAR_PACKAGE161} > /dev/null 2>&1
		if [ $? -ne 0 ]; then
			echo "[ERROR] Decompression package failed."
			return 1
		fi
	fi
	if [ ${regionID} -eq 2 ]; then
		wget ${OBS_URL}${DEB_TAR_PACKAGE76}
		if [ $? -ne 0 ]; then
			echo "[ERROR] Can't download package."
			return 1
		fi
		wget ${OBS_URL}${DEB_TAR_PACKAGE76}.sha256
		if [ $? -ne 0 ]; then
			echo "[ERROR] Can't download sha256 file."
			return 1
		fi
		sha256=`sha256sum ${DEB_TAR_PACKAGE76}`
		file_sha256=`cat ${DEB_TAR_PACKAGE76}.sha256`
		if [ "${sha256}" != "${file_sha256}" ]; then
			echo "[ERROR] package have been changed."
			return 1
		fi
		tar -zxvf ${DEB_TAR_PACKAGE76} > /dev/null 2>&1
		if [ $? -ne 0 ]; then
			echo "[ERROR] Decompression package failed."
			return 1
		fi
	fi
	
	if [ ${regionID} -eq 3 ]; then
		return 1
	fi
	
	dpkg -i xss_XSS_xss_Linux*.deb
	if [ $? -ne 0 ]; then
		echo "[ERROR] Install deb package failed."
		return 1
	fi
	echo "install deb package successed."
	return 0
}

function installTAR()
{
    selectRegion
	regionID=$?
	if [ ${regionID} -eq 1 ]; then
		wget ${OBS_URL}${TAR_TAR_PACKAGE161}
		if [ $? -ne 0 ]; then
			echo "[ERROR] Can't download package."
			return 1
		fi
		wget ${OBS_URL}${TAR_TAR_PACKAGE161}.sha256
		if [ $? -ne 0 ]; then
			echo "[ERROR] Can't download sha256 file."
			return 1
		fi
		sha256=`sha256sum ${TAR_TAR_PACKAGE161}`
		file_sha256=`cat ${TAR_TAR_PACKAGE161}.sha256`
		if [ "${sha256}" != "${file_sha256}" ]; then
			echo "[ERROR] package have been changed."
			return 1
		fi
		tar -zxvf ${TAR_TAR_PACKAGE161} > /dev/null 2>&1
		if [ $? -ne 0 ]; then
			echo "[ERROR] Decompression package failed."
			return 1
		fi
	fi
	if [ ${regionID} -eq 2 ]; then
		wget ${OBS_URL}${TAR_TAR_PACKAGE76}
		if [ $? -ne 0 ]; then
			echo "[ERROR] Can't download package."
			return 1
		fi
		wget ${OBS_URL}${TAR_TAR_PACKAGE76}.sha256
		if [ $? -ne 0 ]; then
			echo "[ERROR] Can't download sha256 file."
			return 1
		fi
		sha256=`sha256sum ${TAR_TAR_PACKAGE76}`
		file_sha256=`cat ${TAR_TAR_PACKAGE76}.sha256`
		if [ "${sha256}" != "${file_sha256}" ]; then
			echo "[ERROR] package have been changed."
			return 1
		fi
		tar -zxvf ${TAR_TAR_PACKAGE76} > /dev/null 2>&1
		if [ $? -ne 0 ]; then
			echo "[ERROR] Decompression package failed."
			return 1
		fi
	fi

	if [ ${regionID} -eq 3 ]; then
		return 1
	fi
	
	tar -xf xss_XSS_xss_Gentoo*.tar.gz -C /usr/local/
	if [ $? -ne 0 ]; then
		echo "[ERROR] Install tar package failed."
		return 1
	fi
    mv /usr/local/xxgg/control /etc/init.d/xxgg
    chmod a+x /etc/init.d/xxgg
    if [ -x /sbin/rc-update ]; then
        rc-update add xxgg boot default sysinit > /dev/null 2>&1  || return 1
        rc-service xxgg start
    fi
	echo "install tar package successed."
	return 0
}

function install()
{
	echo "start to install XXX "
	installDep
	rpm --version > /dev/null 2>&1
	if [ $? -eq 0 ]; then
		installRPM
		if [ $? -eq 0 ]; then
			return 0
		fi
	fi
	
	dpkg --version > /dev/null 2>&1
	if [ $? -eq 0 ]; then
		installDEB
		if [ $? -eq 0 ]; then
			return 0
		fi
	fi
    
	if [ -f "/etc/gentoo-release" ]; then
		installTAR
		if [ $? -eq 0 ]; then
			return 0
		fi
	fi
	
	echo "Operate System is unsupported."
	return 1
}


/etc/init.d/xxgg status > /dev/null 2>&1
if [ $? -eq 0 ]; then
	echo "[ERROR] xxx have installed, can't install it."
else
	install
	rm -f xss_linux*.tar.gz > /dev/null 2>&1
	rm -f xss_linux*.tar.gz.sha256 > /dev/null 2>&1
	rm -f xss_XSS_xss_Linux*.rpm > /dev/null 2>&1
	rm -f xss_XSS_xss_Linux*.deb > /dev/null 2>&1
	rm -f xss_XSS_xss_Gentoo*.tar.gz > /dev/null 2>&1
	rm -f xxggxxddInstall_32.sh > /dev/null 2>&1
fi


