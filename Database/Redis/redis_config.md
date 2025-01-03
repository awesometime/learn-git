#最大连接数
redis.pool.maxTotal=1000

#最大空闲连接数
redis.pool.maxIdle=10

#最小空闲连接数
redis.pool.minIdle = 0

#是否启用后进先出
redis.pool.lifo = true

redis.pool.fairness = false

#获取连接时的最大等待毫秒数，如果设置为阻塞时BlockWhenExhausted，如果超时就抛异常；小于零：阻塞不确定的时间，默认-1
redis.pool.maxWaitMillis = 10000

#逐出连接的最小空闲时间，默认1800000毫秒
redis.pool.minEvictableIdleTimeMillis=1800000

#对象空闲多久后逐出，当空闲时间>该值 且 空闲连接>最大空闲数 时直接逐出，不再根据MinEvictableIdleTimeMillis判断（默认逐出策略）
redis.pool.softMinEvictableIdleTimeMillis=10000

#每次逐出检查时，逐出的最大数目 如果为负数就是：1/abs(n)，默认3
redis.pool.numTestsPerEvictionRun=3

#设置的逐出策略类名，默认DefaultEvictionPolicy(当连接超过最大空闲时间,或连接数超过最大空闲连接数)
redis.pool.evictionPolicyClassName = org.apache.commons.pool2.impl.DefaultEvictionPolicy

redis.pool.testOnCreate=true

#在获取连接的时候检查有效性
redis.pool.testOnBorrow=true

redis.pool.testOnReturn=false

#在空闲时检查有效性
redis.pool.testWhileIdle=false

#逐出扫描的时间间隔（毫秒）， 如果为负数则不运行逐出线程，默认-1
redis.pool.timeBetweenEvictionRunsMillis=30000

#连接耗尽时是否阻塞，false报异常，ture阻塞直到超时，默认true
redis.pool.blockWhenExhausted=true

#是否启用pool的jmx管理功能，默认true
redis.pool.jmxEnabled = true

#主机地址
redis.hostName=

#主机端口，默认：6379
redis.port=

#超时时间，默认：2000
redis.timeout=3000

#密码

# "config/redis.properties"  
