#encoding=utf-8
from config.public_data import REQUEST_DATA,RESPONSE_DATA
from utils.md5_encrypt import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class GetKey(object):
    def __init__(self):
        pass

    @classmethod
    def get(cls, dataSource, relyData):
        data = dataSource.copy()
        for key, value in relyData.items():
            if key == "request":
                # 说明应该去REQUEST_DATA获取值
                for k, v in value.items():
                    # print k,v
                    interfaceName, case_id = v.split("->")
                    print type(interfaceName),REQUEST_DATA
                    data[k] = REQUEST_DATA[interfaceName][case_id][k]
                    if k == 'password':
                        data[k] = md5_encrypt(data[k])
            elif key == "response":
                # 说明应该去RESPONSE_DATA获取值
                for k, v in value.items():
                    interfaceName, case_id = v.split("->")
                    data[k] = RESPONSE_DATA[interfaceName][case_id][k]
        return data

if __name__ == '__main__':
    REQUEST_DATA = {u"用户注册": {"1": {"username": "2wcd", "password": "sdfwe2"}}}
    s = {"username":"","password":""}
    rely = {"request":{"username":"register->1","password":"register->1"}}
    print GetKey.get(s, rely)


