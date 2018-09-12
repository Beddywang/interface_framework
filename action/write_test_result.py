# -*- coding: utf-8 -*-
from config.public_data import *

def write_result(wbObj, sheetObj, responseData, errorKey, rowNum):
    try:
        #写响应body
        wbObj.writeCell(sheet=sheetObj,content="%s"%responseData,
                        rowNo=rowNum, colsNo=CASE_responseData)
        if errorKey:
            wbObj.writeCell(sheet=sheetObj,content="faild",rowNo=rowNum,colsNo=CASE_status)
            wbObj.writeCell(sheet=sheetObj,content="%s"%errorKey,rowNo=rowNum,colsNo=CASE_errorInfo)
        else:
            wbObj.writeCell(sheet=sheetObj, content="success", rowNo=rowNum, colsNo=CASE_status)
    except Exception as e:
        print e




