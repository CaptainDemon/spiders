# from Mydb import Mydb
from job1.utils.Mydb import Mydb


mydb = Mydb('127.0.0.1','root','123456','temp',port=3307,charset='utf8')

def getproxy():
    sql = 'select * from proxy_gaoni ORDER BY rand()'
    # sql = 'select * from proxy_gaoni ORDER BY rand() limit 1'
    res = mydb.query(sql)
    proxy_info = res[0]
    return proxy_info
# m = getproxy()
# print(m)