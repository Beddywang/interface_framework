# -*- coding: utf-8 -*-
import os

#获取到工程目录
baseDir = os.path.dirname(os.path.dirname(__file__))

#设置Excel的目录
excel_file_path = baseDir + '/TestData/inter_test_data.xlsx'

API_apiName = 1
API_requestUrl = 2
API_requestMethod = 3
API_paramsType = 4
API_apiTestCaseFileName = 5

#注册接口用例sheet的列号映射关系
CASE_requestData = 1
CASE_relyData = 2
CASE_responseCode = 3
CASE_responseData = 4
CASE_dataStore = 5
CASE_checkPoint = 6
CASE_active = 7
CASE_status = 8
CASE_errorInfo = 9

#存储请求参数里面的依赖数据
REQUEST_DATA = {}
RESPONSE_DATA = {}

if __name__ == '__main__':
    print baseDir
    print excel_file_path