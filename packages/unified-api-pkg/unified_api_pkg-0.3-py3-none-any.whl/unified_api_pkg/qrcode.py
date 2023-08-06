import clr
import json
clr.AddReference("System.Collections")
clr.AddReference(r"paymentQR")

from System.Collections import ArrayList
from System import String
from .paymentQR import TransRecord
from .paymentQR import paymentQRAPI



SALE = 1
VOID = 2
REFUND = 3
TEST = 4

testingQR=paymentQRAPI()
testdata = TransRecord()
arraylist = ArrayList()
result = -1

def sale(code, ecrRef, amount, transData, stringList):
    print("QRcode sale called")
    result = testingQR.SaleQR(code,ecrRef,amount,testdata,arraylist)
    jsonString = testdata.toJSONString()
    tempDict = json.loads(jsonString)
    for val in tempDict:
        transData[val] = tempDict[val]
    for val in arraylist:
        stringList.append(val)
    return result


def voidSale(invoice,transData,stringList):
    result = testingQR.Void(invoice,"",testdata,arraylist)
    jsonString = testdata.toJSONString()
    tempDict = json.loads(jsonString)
    for val in tempDict:
        transData[val] = tempDict[val]
    for val in arraylist:
        stringList.append(val)
    return result

def refund(EcrRef,Amount,originalData,transData,stringList):
    result = testingQR.Refund(EcrRef,Amount,originalData,testdata,arraylist)
    jsonString = testdata.toJSONString()
    tempDict = json.loads(jsonString)
    for val in tempDict:
        transData[val] = tempDict[val]
    for val in arraylist:
        stringList.append(val)
    return result

