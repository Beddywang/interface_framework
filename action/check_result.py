# -*- coding: utf-8 -*-
import re
class CheckResult(object):
    def __init__(self):
        pass

    @classmethod
    def check(cls,responseObj,checkpoint):
        errorKey = {}
        for key,value in checkpoint.items():
            if isinstance(value,(str,unicode)):
                if responseObj[key] != value:
                    errorKey[key] = responseObj[key]
                elif isinstance(value,dict):
                    if value.has_key('value'):
                        sourceData = responseObj[key]
                        regStr = value["value"]
                        rg = re.match(regStr,"%s"%responseObj)
                        if not rg:
                            errorKey[key] = sourceData
                    elif value.has_key('type'):
                        typeS = value["type"]
                        if typeS == "N":
                            #说明是整型
                            if isinstance(sourceData,(int,long)):
                                errorKey[key] = sourceData
        return errorKey
if __name__ == '__main__':
    r = {"code":"01","userid":12,"id":"12"}
    c = {"code":"00","userid":{"type":"N"},"id":{"value":"\d+"}}
    print CheckResult.check(r,c)