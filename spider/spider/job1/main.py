from scrapy import cmdline
import os
# cmdline.execute('scrapy crawl hao123'.split())

os.chdir('job1/spiders')
# cmdline.execute('scrapy crawl boss'.split())
cmdline.execute('scrapy runspider boss.py'.split())
# cmdline.execute('scrapy runspider mycrawler_redis.py'.split())
