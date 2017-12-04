# -*- coding: utf-8 -*-
import scrapy
# 爬虫类需要继承 RedisSpider
from scrapy_redis.spiders import RedisSpider
# 爬虫集成 RedisCrawlSpider
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
import datetime
# from datetime import datetime

import time

def get_num(strs):
    pattern = re.compile(r'\d+')
    m = pattern.findall(strs)
    return m
def get_date_pub(date_pub):
    if ':' in date_pub:
        date_pub = datetime.datetime.now().strftime('%Y-%m-%d')
    elif '昨天' in date_pub:
        # now = datetime.now()
        # datetime.datetime(now.year,now.month,(now.day - 1))
        date_pub = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    else:
        date_pub = '-'.join(get_num(date_pub))
    return  date_pub
def get_year(year):
    if get_num(str(year)):
        year = get_num(str(year))[0]
    else:
        year = 0
    return year
def get_money(money):
    if 'K' in money:
        money = get_num(money)
    else:
        money = money / 1000
    return money

# class BossSpider(CrawlSpider):
class BossSpider(RedisCrawlSpider):
    name = 'boss'
    allowed_domains = ['zhipin.com']
    # start_urls = ['https://www.zhipin.com/']
    # 设置爬虫的rediskey
    redis_key = 'BossSpider:start_urls'
    # start_urls = ['https://www.zhipin.com']
    rules = (
        # 列表页
        Rule(LinkExtractor(allow=r'/c\d+'), follow=True),
        Rule(LinkExtractor(allow=r'job_detail/(.*).html'), callback='parse_item', follow=False, process_request = 'process_request'),
    # , process_request = 'process_request'

    )

    def process_request(self,request):
        request.priority = 1
        return request

    # def process_link(self ,links):
    #     for link in links:
    #         # print(link)
    #         pass
    #     return links

    def parse_item(self, response):
        print(response.url)
        url = response.url
        try:
            job_name = response.xpath('//div[@class="job-primary"]//div[@class="name"]/text()').extract()[0]
        except Exception as e:
            job_name = response.xpath('//div[@class="job-primary"]//div[@class="name"]/text()').extract()[0]
            print(job_name)
            print(e)
            job_name = ''
        # return job_name

        smoney = response.xpath('//div[@class="job-primary"]//div[@class="name"]/span/text()').extract()[0]
        smoney = get_money(smoney)[0]
        emoney = response.xpath('//div[@class="job-primary"]//div[@class="name"]/span/text()').extract()[0]
        emoney = get_money(emoney)[1]
        location = response.xpath('//*[@id="main"]/div[1]/div/div/div[2]/p/text()[1]').extract()[0]
        syear = response.xpath('//*[@id="main"]/div[1]/div/div/div[2]/p/text()[2]').extract()
        syear = get_year(syear)
        eyear = response.xpath('//*[@id="main"]/div[1]/div/div/div[2]/p/text()[2]').extract()
        eyear = get_year(eyear)
        degree = response.xpath('//*[@id="main"]/div[1]/div/div/div[2]/p/text()[3]').extract()[0]
        tags = ','.join(response.xpath('//div[@class="job-tags"]/span/text()').extract())
        date_pub = response.xpath('//span[@class="time"]/text()').extract()[0]
        date_pub = get_date_pub(date_pub)
        welfare = '福利...'
        jobdesc = ''.join(response.xpath('//div[@class="text"]/text()').extract()).strip()
        jobaddr = response.xpath('//div[@class="location-address"]/text()').extract()[0]
        company_desc = '公司详情...'
        company = response.xpath('//h3[@class="name"]//text()').extract()[0]
        if 'zhipin' in response.url:
            source = 'Boss直聘'
        else:
            source = '其他网址'
        crawl_time = datetime.datetime.now().strftime('%Y-%m-%d')
        # print(url,job_name,smoney,emoney,location,syear,eyear,degree,tags,date_pub,welfare,jobdesc,jobaddr,company_desc,company,source,crawl_time)
        yield {
            'url': url,
            'job_name': job_name,
            'smoney': smoney,
            'emoney': emoney,
            'location': location,
            'syear': syear,
            'eyear': eyear,
            'degree': degree,
            'tags': tags,
            'date_pub': date_pub,
            'welfare': welfare,
            'jobdesc': jobdesc,
            'jobaddr': jobaddr,
            'company_desc': company_desc,
            'company': company,
            'source': source,
            'crawl_time': crawl_time
        }

