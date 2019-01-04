#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/28 21:30
import requests
'''=============发送请求==========='''
# r = requests.get('https://api.github.com/events')
# r = requests.post('http://httpbin.org/post', data = {'key':'value'})
# r = requests.put('http://httpbin.org/put', data = {'key':'value'})
# r = requests.delete('http://httpbin.org/delete')
# r = requests.head('http://httpbin.org/get')
# r = requests.options('http://httpbin.org/get')

'''======================传递URL参数======================'''
'''Requests 允许你使用 params 关键字参数，以一个字符串字典来提供这些参数。
如果你想传递 key1=value1 和 key2=value2 到 httpbin.org/get '''
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get("http://httpbin.org/get", params=payload)
# print(r.url)   #打印  http://httpbin.org/get?key1=value1&key2=value2

'''注意字典里值为 None 的键都不会被添加到 URL 的查询字符串里。
将一个列表作为值传入'''
# payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
# r = requests.get('http://httpbin.org/get', params=payload)
# print(r.url)   #打印   http://httpbin.org/get?key1=value1&key2=value2&key2=value3

'''=================响应内容==================='''
'''读取服务器响应的内容,,,可以找出 Requests 使用了什么编码，并且能够使用 r.encoding 属性来改变它：'''
import requests
# r = requests.get('https://api.github.com/events')
# print(r.text)
# print(r.encoding)


'''================二进制响应内容==============='''
'''能以字节的方式访问请求响应体，对于非文本请求'''
# r = requests.get('https://api.github.com/events')
# print(r.content)

# from PIL import Image
# from io import BytesIO
# i = Image.open(BytesIO(r.content))

'''==============JSON 响应内容=================='''
'''Requests 中也有一个内置的 JSON 解码器，助你处理 JSON 数据'''
'''如果 JSON 解码失败， r.json() 就会抛出一个异常。'''
'''需要注意的是，成功调用 r.json() 并**不**意味着响应的成功。
有的服务器会在失败的响应中包含一个 JSON 对象（比如 HTTP 500 的错误细节）。这种 JSON 会被解码返回。
要检查请求是否成功，请使用 r.raise_for_status() 或者检查
 r.status_code 是否和你的期望相同'''
# import requests
# r= requests.get('https://api.github.com/events')
# print(r.json())

'''==================原始响应内容=============='''
'''在罕见的情况下，你可能想获取来自服务器的原始套接字响应，那么你可以访问 r.raw。
如果你确实想这么干，那请你确保在初始请求中设置了 stream=True。具体你可以这么做：'''
# import requests
# r = requests.get('https://api.github.com/events', stream=True)
# print(r.raw)   #  打印 <urllib3.response.HTTPResponse object at 0x0000000002CCA588>
# print(r.raw.read(10))   #  打印b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03'


'''这里不懂'''
# import requests
# r = requests.get('https://api.github.com/events', stream=True)
# print(r.raw)   #  打印 <urllib3.response.HTTPResponse object at 0x0000000002CCA588>
# print(r.raw.read(10))
# with open(filename, 'wb') as fd:
#     for chunk in r.iter_content(chunk_size):
#         fd.write(chunk)

'''===============定制请求头============='''
'''如果你想为请求添加 HTTP 头部，只要简单地传递一个
dict 给 headers 参数就可以了。'''
# url = 'https://api.github.com/some/endpoint'
# headers = {'user-agent': 'my-app/0.0.1'}
# r = requests.get(url, headers=headers)
# print(r)


'''=================更加复杂的 POST 请求==============='''
'''通常，你想要发送一些编码为表单形式的数据——非常像一个
 HTML 表单。要实现这个，只需简单地传递一个字典给 data 参数。
 你的数据字典在发出请求时会自动编码为表单形式：'''
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post("http://httpbin.org/post", data=payload)
# print(r.text)
'''你还可以为 data 参数传入一个元组列表。在表单中多个元素使用
同一 key 的时候，这种方式尤其有效'''
# payload = (('key1', 'value1'), ('key1', 'value2'))
# r = requests.post('http://httpbin.org/post', data=payload)
# print(r.text)
'''很多时候你想要发送的数据并非编码为表单形式的。
如果你传递一个 string 而不是一个 dict，那么数据会被直接发布出去。'''
# import json
# url = 'https://api.github.com/some/endpoint'
# payload = {'some': 'data'}
# r = requests.post(url, data=json.dumps(payload))
# print(r)
'''此处除了可以自行对 dict 进行编码，
你还可以使用 json 参数直接传递，然后它就会被自动编码。
这是 2.4.2 版的新加功能：'''
import json
# url = 'https://api.github.com/some/endpoint'
# payload = {'some': 'data'}
# r = requests.post(url, json=payload)
# print(r)



'''=================POST一个多部分编码(Multipart-Encoded)的文件================='''
# url = 'http://httpbin.org/post'
# files = {'file': open('report.xls', 'rb')}
# r = requests.post(url, files=files)
# r.text

'''==================响应状态码================='''
'''我们可以检测响应状态码'''
# r = requests.get('http://httpbin.org/get')
# print(r.status_code)   #打印 200
'''为方便引用，Requests还附带了一个内置的状态码查询对象'''
# r = requests.get('http://httpbin.org/get')
# print(r.status_code == requests.codes.ok)   #打印true
'''但是，由于我们的例子中 r 的 status_code 是 200 ，当我们调用 raise_for_status() 时，得到的是：'''
r = requests.get('http://httpbin.org/get')
print(r.raise_for_status())   #打印none





'''====================响应头================='''
'''它是仅为 HTTP 头部而生的。根据 RFC 2616，
HTTP 头部是大小写不敏感的。'''
# r = requests.get('http://httpbin.org/get')
# print(r.headers)
'''我们可以使用任意大写形式来访问这些响应头字段：'''
# r = requests.get('http://httpbin.org/get')
# print(r.headers['Content-Type'])   #打印 application/json
# print(r.headers.get('content-type'))  #打印  application/json







'''====================Cookie==============='''
'''如果某个响应中包含一些 cookie，你可以快速访问它们'''
# url = 'http://example.com/some/cookie/setting/url'
# r = requests.get(url)
# print(r.cookies['example_cookie_name'])
'''要想发送你的cookies到服务器，可以使用 cookies 参数'''
# url = 'http://httpbin.org/cookies'
# cookies = dict(cookies_are='working')
# r = requests.get(url, cookies=cookies)
# print(r.text)
'''Cookie 的返回对象为 RequestsCookieJar，它的行为和字典类似，
但接口更为完整，适合跨域名跨路径使用。你还可以把 Cookie Jar
传到 Requests 中：'''
# jar = requests.cookies.RequestsCookieJar()
# jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
# jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
# url = 'http://httpbin.org/cookies'
# r = requests.get(url, cookies=jar)
# print(r.text)

'''=================重定向与请求历史==================='''
'''默认情况下，除了 HEAD, Requests 会自动处理所有重定向。
可以使用响应对象的 history 方法来追踪重定向。
Response.history 是一个 Response 对象的列表，
为了完成请求而创建了这些对象。这个对象列表按照从最老到最近的
请求进行排序。'''
# r = requests.get('http://github.com')
# print(r.url)   #    打印  https://github.com/
# print(r.status_code)   #  打印 200
# print(r.history)  #打印   [<Response [301]>]
'''如果你使用的是GET、OPTIONS、POST、PUT、PATCH 或者 DELETE，
那么你可以通过 allow_redirects 参数禁用重定向处理'''
# r = requests.get('http://github.com', allow_redirects=False)
# print(r.status_code)  #打印 301
# print(r.history)      #打印[]
'''如果你使用了 HEAD，你也可以启用重定向'''
# r = requests.head('http://github.com', allow_redirects=True)
# print(r.url)     #打印 https://github.com/
# print(r.history)  #打印   [<Response [301]>]



'''=============超时================'''
'''可以告诉 requests 在经过以 timeout 参数设定的秒数时间之后停止等待响应。
基本上所有的生产代码都应该使用这一参数。如果不使用，你的程序可能会永远失去响应'''



'''=====================错误与异常==============='''
'''遇到网络问题（如：DNS 查询失败、拒绝连接等）时，Requests 会抛出一个 ConnectionError 异常。
如果 HTTP 请求返回了不成功的状态码， Response.raise_for_status() 会抛出一个 HTTPError 异常。
若请求超时，则抛出一个 Timeout 异常。
若请求超过了设定的最大重定向次数，则会抛出一个 TooManyRedirects 异常。
所有Requests显式抛出的异常都继承自 requests.exceptions.RequestException'''
