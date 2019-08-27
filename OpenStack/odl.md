本地构建工程
1、构建工程原型 mvn archetype:generate
mvn archetype:generate -DarchetypeGroupId=org.opendaylight.controller -DarchetypeArtifactId=opendaylight-startup-archetype -DarchetypeRepository=http://nexus.opendaylight.org/content/repositories/opendaylight.release/ -DarchetypeCatalog=remote -DarchetypeVersion=1.3.0-Carbon

2、编译工程 ，在pom features 文件中删掉不需要的模块

文件目录说明及需要修改的文件
api          [编写yang]  [接口 模板类]
feature      [feature-xml删除不需要的]
impl         [rpc实现]  [注册blueprint <bean rpc-impl>]

mvn clean install -DskipTests -Dmaven.javadoc.skip=true -Dcheckstyle.skip=true

3、检查基本功能：cd karaf/target/assembly/bin    ./karaf ./start ./client
4、修改YANG文件
5、实现 odl RPC API
基础语法
input builder output builder

6、修改Odlopsprovider注册在odlops.yang中创建的RPC。
7、在BluePrint中注册自己的RPC.API。  bean 


服务器启动
8、将自己构建好的模块从本地C:\Users\lx\.m2\repository\com\ctcc\learn传到服务器
指定目录/root/distribution-karaf-0.6.0-Carbon/system/com/ctcc下

配置文件 /root/distribution-karaf-0.6.0-Carbon/etc/org.apache.karaf.features.cfg 指定需要加载的东西，包括features,ssh等。
具体features在配置文件/root/distribution-karaf-0.6.0-Carbon/system/org/opendaylight/integration/features-integration-index/0.6.0-Carbon/features-integration-index-0.6.0-Carbon-features.xml 里指定
所以在该features配置文件中添加自己写的repository
<repository>mvn:com.ctcc.learn/myexample-features/0.1.0-SNAPSHOT/xml/features</repository>
<repository>mvn:com.ctcc.myclass/classrelated-features/0.1.0-SNAPSHOT/xml/features</repository>


9、删除data lock log等文件,启动karaf
/root/distribution-karaf-0.6.0-Carbon/bin#   ./start   clean  debug    启动karaf
/root/distribution-karaf-0.6.0-Carbon/bin#   ./client  登录
进入后
opendaylight-user@root>feature:install odl-mdsal-all               # MD-SAL
opendaylight-user@root>feature:install odl-dluxapps-applications   # 界面相关
opendaylight-user@root>feature:install odl-myexample
opendaylight-user@root>feature:install odl-cl
odl-classrelated          odl-classrelated-api      odl-classrelated-rest     odl-clustering-test-app      
opendaylight-user@root>feature:install odl-classrelated

10、登录http://172.18.141.230:8181/index.html
