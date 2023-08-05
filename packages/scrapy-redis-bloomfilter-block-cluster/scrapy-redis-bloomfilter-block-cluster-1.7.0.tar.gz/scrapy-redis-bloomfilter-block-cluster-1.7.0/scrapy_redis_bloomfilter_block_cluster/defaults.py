import redis
import rediscluster

# Scheduler default settings
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = 'scrapy_redis_bloomfilter_block_cluster.queue.FifoQueue'
SCHEDULER_QUEUE_KEY = '%(spider)s:requests'
DUPEFILTER_CLASS = 'scrapy_redis_bloomfilter_block_cluster.dupefilter.LockRFPDupeFilter'
DUPEFILTER_DEBUG = False
DUPEFILTER_KEY = '%(spider)s:dupefilter'

# Redis bloomfilter 锁，个数与超时时间，使用 scrapy_redis_bloomfilter_block_cluster.dupefilter.LockRFPDupeFilter 时有效
DUPEFILTER_LOCK_KEY = '%(spider)s:lock'
DUPEFILTER_LOCK_NUM = 16    # Redis bloomfilter 锁个数，可以设置值：16，256，4096
DUPEFILTER_LOCK_TIMEOUT = 15

SCHEDULER_FLUSH_ON_START = False
SCHEDULER_IDLE_BEFORE_CLOSE = 0

CLOSE_EXT_ENABLED =  True
IDLE_NUMBER_BEFORE_CLOSE = 360  # 一次空闲周期 5s 左右

# Pipeline default settings
REDIS_PIPELINE_KEY = '%(spider)s:items'
REDIS_PIPELINE_SERIALIZER = 'scrapy.utils.serialize.ScrapyJSONEncoder'

# Redis default settings
REDIS_START_URLS_KEY = '%(spider)s:start_urls'
REDIS_START_URLS_AS_SET = False
REDIS_START_URLS_AUTO_INSERT = True    # 启动时是否自动插入 start urls

REDIS_ENCODING = 'utf-8'
REDIS_PARAMS = {
    'socket_timeout': 30,
    'socket_connect_timeout': 30,
    'retry_on_timeout': True,
    'password': None,
    'encoding': REDIS_ENCODING,
}
REDIS_CLUSTER_PARAMS = {
    'socket_timeout': 30,
    'socket_connect_timeout': 30,
    'retry_on_timeout': True,
    'password': None,
    'encoding': REDIS_ENCODING,
}
REDIS_CLS = redis.Redis
REDIS_CLUSTER_CLS = rediscluster.RedisCluster

# BloomFilter default settings
BLOOMFILTER_HASH_NUMBER = 15
BLOOMFILTER_BIT = 32
BLOOMFILTER_BLOCK_NUM = 1
