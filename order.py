headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9',
  'Accept-Language': 'zh-CN,zh;q=0.8',
  'Accept-Encoding': 'gzip, deflate',
  'user-agent': "Mozilla/5.0+(Windows+NT+6.2;+WOW64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/45.0.2454.101+Safari/537.36"
}

urls = [
  'http://www.cnblogs.com/moodlxs/p/3248890.html', 
  'https://www.zhihu.com/topic/19804387/newest',
  'http://blog.csdn.net/yueguanghaidao/article/details/24281751',
  'https://my.oschina.net/visualgui823/blog/36987',
  'http://blog.chinaunix.net/uid-9162199-id-4738168.html',
  'http://www.tuicool.com/articles/u67Bz26',
  'http://rfyiamcool.blog.51cto.com/1030776/1538367/',
  'http://itindex.net/detail/26512-flask-tornado-gevent'
]

"""
顺序抓取
"""
def func():
  import requests
  import time
  print(u'顺序抓取')

  startTime = time.time()
  for url in urls:
    try:
      r = requests.get(url, allow_redirects=False, timeout=2.0, headers=headers)
    except:
      pass
    else:
      print(r.status_code, r.url)
  
  endTime = time.time()
  print(endTime - startTime)

func()