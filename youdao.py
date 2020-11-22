import urllib.request
import urllib.parse
import json

def translate():
    centens = input('输入要翻译的语句:')
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    head = {}#增加请求头，防反爬虫
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    data = {}#带上from data的数据进行请求
    data['i'] = centens
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '16057996372935'
    data['sign'] = '0965172abb459f8c7a791df4184bf51c'
    data['lts'] = '1605799637293'
    data['bv'] = 'f7d97c24a497388db1420108e6c3537b'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_REALTlME'
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url,data,head)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    req = json.loads(html)
    result = req['translateResult'][0][0]['tgt']
    # print(f'中英互译的结果：{result}')
    return result
t = translate()
print(f'中英互译的结果：{t}')