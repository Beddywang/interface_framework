# -*- coding: utf-8 -*-
from config.public_data import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class RelyDataStore(object):
    def __init__(self):
        pass

    @classmethod
    def do(cls, storePoint, apiName, caseId,request_source={}, response_source={}):
        # {"request": ["username", "password"], "response": ["userid"]}
        for key, value in storePoint.items():
            if key == "request":
                # 说明存储的数据来自请求参数
                for i in value:
                    if request_source.has_key(i):
                        if not REQUEST_DATA.has_key(apiName):
                            # 说明存储数据的结构还未生成，需要指明数据存储结构
                            REQUEST_DATA[apiName] = {str(caseId):{i:request_source[i]}}
                        else:
                            # 说明存储数据结构中最外层结构完整
                            if REQUEST_DATA[apiName].has_key(str(caseId)):
                                REQUEST_DATA[apiName][str(caseId)][i] = request_source[i]
                            else:
                                REQUEST_DATA[apiName][str(caseId)] = {i:request_source[i]}
                            # return REQUEST_DATA
                    else:
                        print "请求参数中不存在字段" + i
            if key == "response":
                for i in value:
                    if response_source.has_key(i):
                        if not RESPONSE_DATA.has_key(apiName):
                            # 说明存储数据的结构还未生成，需要指明数据存储结构
                            RESPONSE_DATA[apiName] = {str(caseId):{i:response_source[i]}}
                        else:
                            # 说明存储数据结构中最外层结构完整
                            if RESPONSE_DATA[apiName].has_key(str(caseId)):
                                RESPONSE_DATA[apiName][str(caseId)][i] = response_source[i]
                            else:
                                RESPONSE_DATA[apiName][str(caseId)] = {i:response_source[i]}
                            # return REQUEST_DATA
                    else:
                        print "响应body里没有此"


if __name__ == '__main__':
    r = {"username":"srwcx01","password":"12dfsdft54","email":"wcd@qq.com"}
    s = {"request":["username","password"],"response":["code","userid"]}
    res = {"code":00,"userid":12}

    print REQUEST_DATA
    print RESPONSE_DATA
