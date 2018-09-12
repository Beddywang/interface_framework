#encoding=utf-8
import requests
import json

class HttpClient(object):
    def __init__(self):
        pass

    def request(self, requestMethod, requestUrl, paramsType,
               requestData = None, headers = None, cookies = None):
        if requestMethod.lower() == "post":
            if paramsType == "form":
                #requestData是一个str,形如dict，用eval转换后，类型就是dict，然后再用json.dumps转变为str
                response = self.__post(url = requestUrl, data = json.dumps(eval(requestData)),
                                       headers = headers, cookies = cookies)
                return response
            elif paramsType == "json":
                response = self.__post(url=requestUrl, json = requestData,
                                       headers = headers, cookies = cookies)
                return response
        elif requestMethod.lower() == "get":
            if paramsType == "url":
                request_url = "%s%s" %(requestUrl, requestData)
                response = self.__get(url = request_url,
                                       headers = headers, cookies = cookies)
                return response
            elif paramsType == "params":
                response = self.__get(url=requestUrl, params = requestData,
                                      headers=headers, cookies=cookies)
                return response

    def __post(self, url, data = None, json = None, **kwargs):
        response = requests.post(url = url, data = data, json = json)
        return response

    def __get(self, url, params = None, **kwargs):
        response = requests.get(url = url, params = params)
        return response



if __name__ == '__main__':
    hc = HttpClient()
    paramData = '{"username":"xxxx","password":"xxxxxx","email":"xxxxx"}'
    print type(eval(paramData))
    print type(json.dumps(eval(paramData)))
    response = hc.request('post','http://xxxxxx','form',paramData)
    print response.status_code
    print response.text
    print response.json()














