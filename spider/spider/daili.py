import requests
import time
from Mydb import Mydb
# import lxml
from lxml import etree
mydb = Mydb('127.0.0.1','root','123456',db='temp',port=3307,charset='utf-8')
url ="http://www.kuaidaili.com/getproxy/?orderid=961124994498471&num=100&area=&area_ex=&port=&port_ex=&ipstart=&ipstart_ex=&carrier=0&an_ha=1&an_an=1&sp1=1&protocol=1&method=1&quality=0&sort=0&b_pcchrome=1&b_pcie=1&b_pcff=1&showtype=1"

response = requests.get(url)
# html = response.content.decode('utf-8')
html = response.content.decode('utf-8')
#xpath 解析
# html = etree.HTML(html)
response = etree.HTML(html)
# response=response
# print(response)
# response = res.text
# download_btn
# //*[@id="content"]/text()[1]
ip = response.xpath('//*[@id="content"]/text()')[6:-1]

print(ip)
# ip = response.split('\r\n')
for item in ip:
    proxy = item.split('\r\n')[0].strip().split(':')
    print(proxy)
    sql = 'insert into proxy_gaoni(host,port,http_type) VALUES("%s","%s","%s") ON duplicate key UPDATE port=VALUES(port)' % (proxy[0],proxy[1],'http')
    mydb.exe(sql)
    # time.sleep(7)
