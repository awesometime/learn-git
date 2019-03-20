#!/bin/bash
set -xe
unset COLUMNS
PROG_NAME=$0
ACTION=$1
APP_NAME=LB
REPO_RPM=LB
CONFIG_RPM=LB_config
SCRIPT_HOME=$(cd $(dirname $0)/..; pwd)


usage() {
    echo "Usage: $PROG_NAME {start|stop|online|offline|install|uninstall|check_status}"
    exit 2 # bad usage
}

log()
{
    echo "`date "+%Y-%m-%d %T"`: $1"
}

#check user
if [ "$UID" -ne 0 ]; then
    log "ERROR: the scripte must run as root"
    exit 3
fi

#check usage
if [ $# -lt 1 ]; then
    usage
    exit 2
fi


start()
{
    log "INFO: start  ${APP_NAME} beginning!"
    if [ -f /etc/init.d/nginxd ]; then
    /etc/init.d/nginxd start
    fi
    log "INFO: start ${APP_NAME} ending"
}

stop()
{
    log "INFO: stop ${APP_NAME} beginning!"

    if [ -f /etc/init.d/nginxd ]; then
    /etc/init.d/nginxd stop
    fi
    log "INFO: stop ${APP_NAME} ending"
}

online()
{
    log "INFO: online ${APP_NAME} beginning!"
    #sleep 5
    #systemctl start health_check
    log "INFO: Nothing to do online ${APP_NAME}"
}
offline()
{
    log "INFO: stop ${APP_NAME} beginning!"
    #systemctl stop health_check
    #sleep 15
    log "INFO: Nothing to do offline ${APP_NAME}"
}

install()
{
    log "INFO: install ${APP_NAME} beginning!"

    rpm -ivh ${SCRIPT_HOME}/repo/${REPO_RPM}_nginx* --nodeps --force
    sh /tmp/LB/nginx/install.sh --install

    rpm -ivh ${SCRIPT_HOME}/repo/${REPO_RPM}_ommha* --nodeps --force

    rpm -ivh ${SCRIPT_HOME}/config/${CONFIG_RPM}* --nodeps --force
    sh /tmp/install.sh --installdouble

    sh /tmp/plugin/floatingIp/config.sh --install
    sh /tmp/plugin/resource/config.sh --install
    sh /tmp/plugin/cleanlog/config.sh --install
    sh /tmp/plugin/nginx/config.sh --install

    log "INFO: install ${APP_NAME} ending!"
}

uninstall()
{
    log "INFO: uninstall  ${APP_NAME} beginning!"

    if [ -f /tmp/nginx/install.sh -a -f /etc/init.d/nginxd ]; then
    sh /tmp/nginx/install.sh --uninstall
    fi
    rpm -q ${REPO_RPM}_nginx | grep "not installed" || rpm -e ${REPO_RPM}_nginx --allmatches

    if [ -f /tmp/install.sh -a -f /etc/init.d/had ]; then
    sh /tmp/install.sh --uninstall
    fi
    rpm -q ${REPO_RPM}_ommha | grep "not installed" || rpm -e ${REPO_RPM}_ommha --allmatches

    rpm -q ${CONFIG_RPM} | grep "not installed" || rpm -e ${CONFIG_RPM} --allmatches

    log "INFO: uninstall ${APP_NAME} finished"
}

check_status()
{
    log "INFO: check_status  ${APP_NAME} beginning!"


    log "INFO: check_status ${APP_NAME} finished"
}


case "$ACTION" in
start)
start
;;
stop)
stop
;;
online)
online
;;
offline)
offline
;;
restart)
offline
stop
start
online
;;
install)
install
;;
uninstall)
uninstall
;;
check_status)
check_status
;;
*)
usage
;;
esac
