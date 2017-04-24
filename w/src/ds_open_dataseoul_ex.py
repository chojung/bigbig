
import os
import requests
import urlparse
import mylib

def doIt():
    keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
    key=mylib.getKey(keyPath)
    # (1) make params with resource IDs
    KEY=key['dataseoul']
    TYPE='json'
    SERVICE='SearchSTNBySubwayLineService'
    START_INDEX=str(1)
    END_INDEX=str(10)
    LINE_NUM=str(2)
    params=os.path.join(KEY,TYPE,SERVICE,START_INDEX,END_INDEX,LINE_NUM)
    # (2) make a full url
    _url='http://openAPI.seoul.go.kr:8088/'
    #url=urlparse.urljoin(_url,params)
    url=u'http://openapi.seoul.go.kr:8088/5a4a64554f776f6f35336c6f456963/json/SearchSTNBySubwayLineService/1/10/2'
    # (3) get data
    data=requests.get(url).text
    #print(url)
    print data[:300]

if __name__ == "__main__":
    doIt()