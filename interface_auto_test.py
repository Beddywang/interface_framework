# -*- coding: utf-8 -*-
import requests
from utils.ParseExcel import *
from config.public_data import *
from utils.HttpClient import *
from action.get_rely import *
from action.data_store import *
from action.check_result import *
from action.write_test_result import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    parseE = ParseExcel()
    parseE.loadWorkBook(excel_file_path)
    sheetObj = parseE.getSheetByName(u'API')
    actitiveList = parseE.getColumn(sheetObj,7)
    for id,i in enumerate(actitiveList[1:],2): #2为指定起点，为了后面传入行号方便
        # print id,i.value
        if i.value == 'y':
            rowObj = parseE.getRow(sheetObj,id)
            apiName = rowObj[API_apiName].value
            requestUrl = rowObj[API_requestUrl].value
            requestMethod = rowObj[API_requestMethod].value
            paramsType = rowObj[API_paramsType].value
            apiTestCaseFileName = rowObj[API_apiTestCaseFileName].value
            # print apiName,requestUrl,requestMethod,paramsType,apiTestCaseFileName

            # 下一步读用例sheet表，准备执行测试用例
            caseSheetObj = parseE.getSheetByName(apiTestCaseFileName)
            caseActiveObj = parseE.getColumn(caseSheetObj, CASE_active)
            for c_idx, col in enumerate(caseActiveObj[1:], 2):
                if col.value == "y":
                    # 说明此case行需要执行
                    caseRowObj = parseE.getRow(caseSheetObj, c_idx)
                    requestData = caseRowObj[CASE_requestData - 1].value
                    relyData = caseRowObj[CASE_relyData - 1].value
                    datastore = caseRowObj[CASE_dataStore -1].value
                    checkpoint = caseRowObj[CASE_checkPoint -1].value
                    if relyData:
                        # 发送接口请求之前，先做依赖数据的处理
                        requestData = "%s" % GetKey.get(eval(requestData), eval(relyData))
                    print "requestData:",requestData
                    httpclient = HttpClient()
                    response = httpclient.request(requestMethod,requestUrl,paramsType,requestData)
                    # print response.status_code
                    print "%s的返回结果为：%s"%(apiName,response.text)
                    if response.status_code == 200:
                        responseData = response.json()
                        # print type(requestData),type(responseData)
                        if datastore:
                            RelyDataStore.do(eval(datastore),apiName,c_idx -1, request_source=eval(requestData),response_source=responseData)
                        errorKey = CheckResult.check(responseData,eval(checkpoint))
                        # print errorKey
                        # print type(responseData),errorKey
                        write_result(parseE,caseSheetObj,responseData,errorKey,c_idx)
                else:
                    print "用例被忽略执行"
        else:
            print "用例被忽略执行"

        # print i.value
if __name__ == '__main__':
    main()
