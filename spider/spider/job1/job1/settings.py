# -*- coding: utf-8 -*-

# Scrapy settings for job1 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'job1'

SPIDER_MODULES = ['job1.spiders']
NEWSPIDER_MODULE = 'job1.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'job1 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY =0
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  # 'Accept-Language': 'en',
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    # "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": "sid=sem_pz_bdpc_index; __c=1511146883; __g=sem_pz_bdpc_index; lastCity=101010100; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1511009843,1511146883; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1511161145; __l=l=%2F%3Fsid%3Dsem_pz_bdpc_index&r=http%3A%2F%2Fbzclk.baidu.com%2Fadrc.php%3Ft%3D06KL00c00fDNJKT0A9KU0KZEgsZIwwFp00000axfx-b00000XRRNRM.THdBULP1doZA8QMu1x60UWY4PWbzrj0LP7qCmyqxTAT0T1dhPyuhrHc3Pj0snjK-PH0L0ZRqwbcsPWKAPHIKn1NaPYc4rjfvnYf4fHDsnW-7wjuAfbR0mHdL5iuVmv-b5HnsPWD1nj6knHDhTZFEuA-b5HDv0ARqpZwYTjCEQLILIz4lpA-spy38mvqVQ1q1pyfqTvNVgLKlgvFbTAPxpy4bug60mLFW5HDzPWD%26tpl%3Dtpl_10085_15730_11224%26l%3D1501483047%26ie%3Dutf-8%26f%3D3%26tn%3D96928074_hao_pg%26wd%3Dboss%25E7%259B%25B4%25E8%2581%2598%25E5%25AE%2598%25E7%25BD%2591%26rqlang%3Dcn%26inputT%3D4084%26prefixsug%3Dboos%26rsp%3D3&g=%2F%3Fsid%3Dsem_pz_bdpc_index; __a=28696314.1511009934.1511009934.1511146883.35.2.34.34; JSESSIONID=""",
    "Host": "www.zhipin.com",
    "Pragma": "no-cache",
    "Referer:https": "//www.zhipin.com/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'job1.middlewares.Job1SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'job1.middlewares.MyCustomDownloaderMiddleware': 543,
   'job1.mymiddlewares.RandomProxy': 1,

}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'job1.pipelines.Job1Pipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
RANDOM_UA_TYPE = 'random'
# from job1.utils import get_proxy
# m = get_proxy.getproxy()
# # print(m)
# host = str(m[0])+":"+str(m[1])

# PROXIES = [
   # {'host':host},
   # {'host':'101.37.203.65:80'},
   #  {'host':'61.135.217.7:80'},
   #  {'host' : '61.155.164.107:3128'},
   #  {'host' : '61.160.208.222:8080'},
# ]

# AUTH_PRXIES = [
#     {'host':'120.78.166.84:6666','auth':'alice:123456'}
# ]

# url指纹过滤器
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 设置爬虫是否可以中断
SCHEDULER_PERSIST = True

# 设置请求队列类型
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue" # 按优先级入队列
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"  # 按照队列模式
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack" # 按照栈进行请求的调度

# 配置redis管道文件，权重数字相对最大
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 999,  # redis管道文件，自动把数据加载到redis
    'job1.pipelines.Job1Pipeline': 300,
}

# redis
# 连接配置
REDIS_HOST = '192.168.191.128'
REDIS_PORT = 6379