#### 安装完以后
```
# source ~/admin-openrc.sh 

# nova network-create vmprivate --fixed-range-v4 10.11.12.0/24 --fixed-cidr 10.11.12.0/24 --bridge br100 --bridge-interface eth1

# nova network-list

# nova network-show xxxx

# nova floating-ip-bulk-create 192.168.x.xx/24

```


```
【137 】【纯环境】【】【】【】【6.21】
【2.60】【物理机】【】【】【】【8.3 】【8.10】【9.10】【半小时】
root@cloudlet:~/elijah-openstack/ansible# ansible-playbook -i ./hosts openstackpp.yaml

PLAY [controller, compute] **************************************************************************

TASK [Gathering Facts] ******************************************************************************
ok: [localhost]

TASK [cloudlet : (CLOUDLET) install fabric/openssh/git] *********************************************
ok: [localhost] => (item=[u'fabric', u'git', u'openssh-server'])

TASK [cloudlet : (CLOUDLET) checkout elijah-provisioning code from github] **************************
ok: [localhost]

TASK [cloudlet : (CLOUDLET) install library using fabric] *******************************************
changed: [localhost]

TASK [cloudlet : (CLOUDLET) uninstall pbr installed with elijah-provisioning as it conflicts with openstack python clients] ***
changed: [localhost]

TASK [cloudlet : (CLOUDLET) add user to kvm/libvirtd groups] ****************************************
ok: [localhost]

PLAY [controller, compute] **************************************************************************

TASK [Gathering Facts] ******************************************************************************
ok: [localhost]

TASK [openstack-common : (GPUPASS) modify grub config to enable IOMMU] ***********************************
skipping: [localhost]

TASK [openstack-common : (GPUPASS) update grub] **********************************************************
skipping: [localhost]

TASK [openstack-common : (GPUPASS) update initram-fs modules for VFIO] ***********************************
skipping: [localhost]

TASK [openstack-common : (GPUPASS) update initram-fs] ****************************************************
skipping: [localhost]

TASK [openstack-common : (GPUPASS) add GPU devices to VFIO conf] *****************************************
skipping: [localhost]

TASK [openstack-common : (GPUPASS) remove any existing nvidia drivers] ***********************************
skipping: [localhost]

TASK [openstack-common : (GPUPASS) reboot and...] ********************************************************
skipping: [localhost]

TASK [openstack-common : (GPUPASS) ...wait for SSH to come back up] **************************************
skipping: [localhost]

TASK [openstack-common : (OS-COMMON) modify grub config to show text on boot] ***********************
changed: [localhost]

TASK [openstack-common : (OS-COMMON) install Ubuntu-Cloud-Keyring] **********************************
ok: [localhost]

TASK [openstack-common : (OS-COMMON) add Kilo repo] *************************************************
ok: [localhost]

TASK [openstack-common : (OS-COMMON) update cache and perform upgrade] ******************************
changed: [localhost]

TASK [openstack-common : (OS-COMMON) install python openstack client] *******************************
ok: [localhost] => (item=[u'python-openstackclient'])

PLAY [controller] ***********************************************************************************

TASK [Gathering Facts] ******************************************************************************
ok: [localhost]

TASK [openstack-controller : (CONTROLLER) install mariadb and python lib] ***************************
ok: [localhost] => (item=mariadb-server)
ok: [localhost] => (item=python-mysqldb)
ok: [localhost] => (item=python-pip)

TASK [openstack-controller : pip] *******************************************************************
changed: [localhost]

TASK [openstack-controller : (CONTROLLER) run mysql installation] ***********************************
changed: [localhost]

TASK [openstack-controller : (CONTROLLER) create mysql conf] ****************************************
changed: [localhost]

RUNNING HANDLER [openstack-controller : restart mysql] **********************************************
changed: [localhost]

TASK [openstack-controller : (CONTROLLER) install RabbitMQ] *****************************************
changed: [localhost]

TASK [openstack-controller : (CONTROLLER) check if openstack user already exists] *******************
changed: [localhost]

TASK [openstack-controller : (CONTROLLER) create openstack rabbitmq user] ***************************
changed: [localhost]

TASK [openstack-controller : (CONTROLLER) set user perms] *******************************************
changed: [localhost]

TASK [openstack-controller : (KEYSTONE) transfer keystonedb SQL script] *****************************
changed: [localhost]

TASK [openstack-controller : (KEYSTONE) check if keystone db already exists] ************************
changed: [localhost]

TASK [openstack-controller : (KEYSTONE) create keystone db] *****************************************
changed: [localhost]

TASK [openstack-controller : (KEYSTONE) disable automatic startup of keystone] **********************
changed: [localhost]

TASK [openstack-controller : (KEYSTONE) install keystone...] ****************************************
changed: [localhost] => (item=[u'keystone'])

TASK [openstack-controller : (KEYSTONE)  install apache/memcached] **********************************
ok: [localhost] => (item=apache2)
changed: [localhost] => (item=libapache2-mod-wsgi)
changed: [localhost] => (item=memcached)
ok: [localhost] => (item=python-memcache)

TASK [openstack-controller : (KEYSTONE) replace keystone conf] **************************************
changed: [localhost]

TASK [openstack-controller : (KEYSTONE) populate identity service database] *************************
changed: [localhost]

TASK [openstack-controller : (KEYSTONE) replace servername in apache conf] **************************
changed: [localhost]

TASK [openstack-controller : (KEYSTONE) create wsgi-keystone.conf] **********************************
changed: [localhost]

TASK [openstack-controller : (KEYSTONE) enable identity service virtual hosts] **********************
changed: [localhost]

TASK [openstack-controller : (KEYSTONE) create wsgi dir] ********************************************
changed: [localhost]

TASK [openstack-controller : (KEYSTONE) copy keystone wsgi components] ******************************
changed: [localhost]

TASK [openstack-controller : (KEYSTONE) copy keystone wsgi components] ******************************
changed: [localhost]

TASK [openstack-controller : (KEYSTONE) stop keystone service if running (it will restart with apache2)] ***
ok: [localhost]

TASK [openstack-controller : (KEYSTONE) remove SQLite] **********************************************
changed: [localhost]

RUNNING HANDLER [openstack-controller : restart apache] *********************************************
changed: [localhost]

TASK [openstack-controller : (KEYSTONE) wait 5s for keystone to come back up] ***********************
changed: [localhost]

TASK [openstack-controller : (KEYSTONE) create identity service] ************************************
changed: [localhost]

TASK [openstack-controller : (KEYSTONE) create identity endpoint] ***********************************
changed: [localhost]

TASK [openstack-controller : (KEYSTONE) create admin project] ***************************************
changed: [localhost]

TASK [openstack-controller : (KEYSTONE) create service project] *************************************
changed: [localhost]

TASK [openstack-controller : (KEYSTONE) create admin user] ******************************************
changed: [localhost]

TASK [openstack-controller : (KEYSTONE) create admin role] ******************************************
changed: [localhost]

TASK [openstack-controller : (KEYSTONE) create user role] *******************************************
changed: [localhost]

TASK [openstack-controller : (KEYSTONE) add admin role to admin user] *******************************
changed: [localhost]

TASK [openstack-controller : (KEYSTONE) create OpenStack client script] *****************************
changed: [localhost]

TASK [openstack-controller : (GLANCE) transfer glancedb SQL script] *********************************
changed: [localhost]

TASK [openstack-controller : (GLANCE) check if glance db already exists] ****************************
changed: [localhost]

TASK [openstack-controller : (GLANCE) create glance db] *********************************************
changed: [localhost]

TASK [openstack-controller : (GLANCE) check if glance user already exists] **************************
changed: [localhost]

TASK [openstack-controller : (GLANCE) create glance user] *******************************************
changed: [localhost]

TASK [openstack-controller : (GLANCE) check if glance user is admin in service project] *************
changed: [localhost]

TASK [openstack-controller : (GLANCE) add glance user to service project] ***************************
changed: [localhost]

TASK [openstack-controller : (GLANCE) check if glance service exists] *******************************
changed: [localhost]

TASK [openstack-controller : (GLANCE) create glance service entity] *********************************
changed: [localhost]

TASK [openstack-controller : (GLANCE) check if glance endpoint exists] ******************************
changed: [localhost]

TASK [openstack-controller : (GLANCE) create api endpoint] ******************************************
changed: [localhost]

TASK [openstack-controller : (GLANCE) install glance and associated packages] ***********************
changed: [localhost] => (item=[u'glance', u'python-glanceclient'])

TASK [openstack-controller : (GLANCE) replace glance-api.conf] **************************************
changed: [localhost]

TASK [openstack-controller : (GLANCE) replace glance-registry.conf] *********************************
changed: [localhost]

TASK [openstack-controller : (GLANCE) populate image service database] ******************************
changed: [localhost]

RUNNING HANDLER [openstack-controller : restart glance] *********************************************
changed: [localhost] => (item=glance-registry)
changed: [localhost] => (item=glance-api)

TASK [openstack-controller : (GLANCE) remove SQLite] ************************************************
ok: [localhost]

TASK [openstack-controller : (NOVA) transfer novadb SQL script] *************************************
changed: [localhost]

TASK [openstack-controller : (NOVA) check if nova db already exists] ********************************
changed: [localhost]

TASK [openstack-controller : (NOVA) create nova db] *************************************************
changed: [localhost]

TASK [openstack-controller : (NOVA) check if nova user already exists] ******************************
changed: [localhost]

TASK [openstack-controller : (NOVA) create nova user] ***********************************************
changed: [localhost]

TASK [openstack-controller : (NOVA) check if nova user is admin in service project] *****************
changed: [localhost]

TASK [openstack-controller : (NOVA) add nova user to service project] *******************************
changed: [localhost]

TASK [openstack-controller : (NOVA) check if nova service exists] ***********************************
changed: [localhost]

TASK [openstack-controller : (NOVA) create nova service entity] *************************************
changed: [localhost]

TASK [openstack-controller : (NOVA) check if nova endpoint exists] **********************************
changed: [localhost]

TASK [openstack-controller : (NOVA) create nova api endpoint] ***************************************
changed: [localhost]

TASK [openstack-controller : (NOVA) install nova-api and associated packages] ***********************
changed: [localhost] => (item=[u'nova-api', u'nova-cert', u'nova-conductor', u'nova-consoleauth', u'nova-novncproxy', u'nova-scheduler', u'python-novaclient'])

TASK [openstack-controller : (NOVA) make log directory] *********************************************
changed: [localhost]

TASK [openstack-controller : (NOVA) setup log configuration] ****************************************
changed: [localhost]

TASK [openstack-controller : (NOVA) install nova-network] *******************************************
changed: [localhost] => (item=[u'nova-network'])

TASK [openstack-controller : (NOVA) replace nova.conf] **********************************************
changed: [localhost]

TASK [openstack-controller : (NOVA) replace api-paste.ini] ******************************************
changed: [localhost]

TASK [openstack-controller : (NOVA) replace rootwrap.conf] ******************************************
changed: [localhost]

TASK [openstack-controller : (NOVA) replace policy.json] ********************************************
changed: [localhost]

TASK [openstack-controller : (NOVA) populate nova service database] *********************************
changed: [localhost]

TASK [openstack-controller : (NOVA) add nova to kvm/libvirtd groups] ********************************
changed: [localhost]

RUNNING HANDLER [openstack-controller : restart nova] ***********************************************
changed: [localhost] => (item=nova-api)
changed: [localhost] => (item=nova-cert)
changed: [localhost] => (item=nova-consoleauth)
changed: [localhost] => (item=nova-conductor)
changed: [localhost] => (item=nova-scheduler)
changed: [localhost] => (item=nova-novncproxy)

TASK [openstack-controller : (NOVA) remove SQLite] **************************************************
changed: [localhost]

TASK [openstack-controller : (SINGLE_NIC) install dummy kernel module] ******************************
skipping: [localhost]

TASK [openstack-controller : (SINGLE_NIC) check if secondary NIC exists] ****************************
skipping: [localhost]

TASK [openstack-controller : (SINGLE_NIC) create virtual NIC] ***************************************
skipping: [localhost]

TASK [openstack-controller : (NEUTRON) transfer neutrondb SQL script] *******************************
skipping: [localhost]

TASK [openstack-controller : (NEUTRON) check if neutron db already exists] **************************
skipping: [localhost]

TASK [openstack-controller : (NEUTRON) create neutron db] *******************************************
skipping: [localhost]

TASK [openstack-controller : (NEUTRON) check if neutron user already exists] ************************
skipping: [localhost]

TASK [openstack-controller : (NEUTRON) create neutron user] *****************************************
skipping: [localhost]

TASK [openstack-controller : (NEUTRON) check if neutron user is admin in service project] ***********
skipping: [localhost]

TASK [openstack-controller : (NEUTRON) add neutron user to service project] *************************
skipping: [localhost]

TASK [openstack-controller : (NEUTRON) check if neutron service exists] *****************************
skipping: [localhost]

TASK [openstack-controller : (NEUTRON) create neutron service entity] *******************************
skipping: [localhost]

TASK [openstack-controller : (NEUTRON) check if neutron endpoint exists] ****************************
skipping: [localhost]

TASK [openstack-controller : (NEUTRON) create api endpoint] *****************************************
skipping: [localhost]

TASK [openstack-controller : (NEUTRON) install neutron and associated packages] *********************
skipping: [localhost] => (item=[]) 

TASK [openstack-controller : (NEUTRON) replace neutron.conf] ****************************************
skipping: [localhost]

TASK [openstack-controller : (NEUTRON) replace ml2_conf.ini] ****************************************
skipping: [localhost]

TASK [openstack-controller : (NEUTRON) replace linuxbridge_agent.ini] *******************************
skipping: [localhost]

TASK [openstack-controller : (NEUTRON) replace l3_agent.ini] ****************************************
skipping: [localhost]

TASK [openstack-controller : (NEUTRON) replace dhcp_agent.ini] **************************************
skipping: [localhost]

TASK [openstack-controller : (NEUTRON) replace metadata_agent.ini] **********************************
skipping: [localhost]

TASK [openstack-controller : (NEUTRON) populate network service database] ***************************
skipping: [localhost]

TASK [openstack-controller : (NEUTRON) remove SQLite] ***********************************************
skipping: [localhost]

TASK [openstack-controller : (HEAT) transfer heatdb SQL script] *************************************
changed: [localhost]

TASK [openstack-controller : (HEAT) check if heat db already exists] ********************************
changed: [localhost]

TASK [openstack-controller : (HEAT) create heat db] *************************************************
changed: [localhost]

TASK [openstack-controller : (HEAT) check if heat user already exists] ******************************
changed: [localhost]

TASK [openstack-controller : (HEAT) create heat user] ***********************************************
changed: [localhost]

TASK [openstack-controller : (HEAT) check if heat user is admin in service project] *****************
changed: [localhost]

TASK [openstack-controller : (HEAT) add heat user to service project] *******************************
changed: [localhost]

TASK [openstack-controller : (HEAT) check if heat service exists] ***********************************
changed: [localhost]

TASK [openstack-controller : (HEAT) create heat service entity] *************************************
changed: [localhost]

TASK [openstack-controller : (HEAT) check if cloudformation service exists] *************************
changed: [localhost]

TASK [openstack-controller : (HEAT) create cloudformation service entity] ***************************
changed: [localhost]

TASK [openstack-controller : (HEAT) check if orchestration endpoint exists] *************************
changed: [localhost]

TASK [openstack-controller : (HEAT) create orchestration endpoint] **********************************
changed: [localhost]

TASK [openstack-controller : (HEAT) check if cloudformation endpoint exists] ************************
changed: [localhost]

TASK [openstack-controller : (HEAT) create cloudformation endpoint] *********************************
changed: [localhost]

TASK [openstack-controller : (HEAT) check if heat user already exists] ******************************
changed: [localhost]

TASK [openstack-controller : (HEAT) create heat_domain_admin user] **********************************
changed: [localhost]

TASK [openstack-controller : (HEAT) give heat_domain_admin admin privs] *****************************
changed: [localhost]

TASK [openstack-controller : (HEAT) check if stack owner role exists] *******************************
changed: [localhost]

TASK [openstack-controller : (HEAT) create stack owner role] ****************************************
changed: [localhost]

TASK [openstack-controller : (HEAT) give hadmin heat_stack_owner privs] *****************************
changed: [localhost]

TASK [openstack-controller : (HEAT) check if stack user role exists] ********************************
changed: [localhost]

TASK [openstack-controller : (HEAT) create stack user role] *****************************************
changed: [localhost]

TASK [openstack-controller : (HEAT) create heat-domain script] **************************************
changed: [localhost]

TASK [openstack-controller : (HEAT) install heat and associated packages] ***************************
changed: [localhost] => (item=[u'heat-api', u'heat-engine', u'heat-api-cfn', u'python-heatclient'])

TASK [openstack-controller : (HEAT) replace heat.conf] **********************************************
changed: [localhost]

TASK [openstack-controller : (HEAT) populate orchestration database] ********************************
changed: [localhost]

RUNNING HANDLER [openstack-controller : restart heat] ***********************************************
changed: [localhost] => (item=heat-engine)
changed: [localhost] => (item=heat-api)
changed: [localhost] => (item=heat-api-cfn)

TASK [openstack-controller : (HEAT) run domain script to create heat domain] ************************
changed: [localhost]

TASK [openstack-controller : (HEAT) remove SQLite] **************************************************
ok: [localhost]

TASK [openstack-controller : (HORIZON) install dashboard] *******************************************
changed: [localhost] => (item=[u'openstack-dashboard'])

TASK [openstack-controller : (HORIZON) replace local_settings.py] ***********************************
changed: [localhost]

TASK [openstack-controller : (HORIZON) add global application group to openstack-dashboard.conf] ****
changed: [localhost]

TASK [openstack-controller : (OPENSTACK-EXT) install git] *******************************************
ok: [localhost] => (item=[u'git'])

TASK [openstack-controller : (OPENSTACK-EXT) checkout elijah-openstack code from github] ************
ok: [localhost]

TASK [openstack-controller : (OPENSTACK-EXT) copy cloudlet.py] **************************************
changed: [localhost]

TASK [openstack-controller : (OPENSTACK-EXT) copy cloudlet_api.py] **********************************
changed: [localhost]

TASK [openstack-controller : (OPENSTACK-EXT) ensure nova.conf is up to date] ************************
ok: [localhost]

TASK [openstack-controller : (OPENSTACK-EXT) copy dashboard files] **********************************
changed: [localhost]

TASK [openstack-controller : (OPENSTACK-EXT) add cloudlet panel to dashboard] ***********************
changed: [localhost]

RUNNING HANDLER [openstack-controller : restart apache] *********************************************
changed: [localhost]

RUNNING HANDLER [openstack-controller : restart nova] ***********************************************
changed: [localhost] => (item=nova-api)
changed: [localhost] => (item=nova-cert)
changed: [localhost] => (item=nova-consoleauth)
changed: [localhost] => (item=nova-conductor)
changed: [localhost] => (item=nova-scheduler)
changed: [localhost] => (item=nova-novncproxy)

PLAY [compute] **************************************************************************************

TASK [Gathering Facts] ******************************************************************************
ok: [localhost]

TASK [openstack-compute : (COMPUTE) install nova-compute] *******************************************
changed: [localhost] => (item=[u'nova-compute', u'sysfsutils'])

TASK [openstack-compute : (COMPUTE) install neutron-plugin] *****************************************
skipping: [localhost] => (item=[]) 

TASK [openstack-compute : (COMPUTE) replace nova.conf] **********************************************
skipping: [localhost]

TASK [openstack-compute : (COMPUTE) replace nova-compute.conf] **************************************
changed: [localhost]

TASK [openstack-compute : (COMPUTE) add nova to kvm/libvirtd groups] ********************************
ok: [localhost]

TASK [openstack-compute : (COMPUTE) remove SQLite] **************************************************
ok: [localhost]

TASK [openstack-compute : (COMPUTE) create OpenStack client script] *********************************
ok: [localhost]

TASK [openstack-compute : install networking components] ********************************************
skipping: [localhost] => (item=[]) 

TASK [openstack-compute : (COMPUTE) replace neutron.conf] *******************************************
skipping: [localhost]

TASK [openstack-compute : (COMPUTE) replace linuxbridge_agent.ini] **********************************
skipping: [localhost]

TASK [openstack-compute : (OPENSTACK-EXT) install fabric/openssh/git] *******************************
ok: [localhost] => (item=[u'git'])

TASK [openstack-compute : (OPENSTACK-EXT) checkout elijah-openstack code from github] ***************
ok: [localhost]

TASK [openstack-compute : (OPENSTACK-EXT) copy cloudlet_manager.py] *********************************
changed: [localhost]

TASK [openstack-compute : (OPENSTACK-EXT) copy cloudlet_driver.py] **********************************
changed: [localhost]

TASK [openstack-compute : (OPENSTACK-EXT) copy cloudlet_api.py] *************************************
changed: [localhost]

TASK [openstack-compute : (OPENSTACK-EXT) ensure nova-compute.conf is up to date] *******************
ok: [localhost]

TASK [openstack-compute : (OPENSTACK-EXT) restart core nova service if running everything on a single node] ***
changed: [localhost] => (item=nova-api)
changed: [localhost] => (item=nova-cert)
changed: [localhost] => (item=nova-consoleauth)
changed: [localhost] => (item=nova-conductor)
changed: [localhost] => (item=nova-scheduler)
changed: [localhost] => (item=nova-novncproxy)

TASK [openstack-compute : (OPENSTACK-EXT) ensure symlink to bios.bin exists] ************************
ok: [localhost]

TASK [openstack-compute : (OPENSTACK-EXT) ensure symlink to kvmvapic.bin exists] ********************
changed: [localhost]

TASK [openstack-compute : (OPENSTACK-EXT) ensure symlink to vgabios-cirrus.bin exists] **************
ok: [localhost]

TASK [openstack-compute : (OPENSTACK-EXT) change qemu conf] *****************************************
changed: [localhost]

TASK [openstack-compute : (OPENSTACK-EXT) exclude libvirt from apparmor] ****************************
changed: [localhost]

RUNNING HANDLER [openstack-compute : restart nova-compute] ******************************************
changed: [localhost] => (item=nova-compute)

RUNNING HANDLER [openstack-compute : restart libvirt-bin] *******************************************
changed: [localhost] => (item=libvirt-bin)

PLAY [controller] ***********************************************************************************

TASK [Gathering Facts] ******************************************************************************
ok: [localhost]
 [WARNING]: Reset is not implemented for this connection


PLAY RECAP ****************************************
localhost                  : ok=154  changed=133  unreachable=0    failed=0 
```
