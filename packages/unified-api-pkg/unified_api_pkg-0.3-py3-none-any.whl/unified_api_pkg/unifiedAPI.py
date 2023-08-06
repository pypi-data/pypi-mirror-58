#Provide Unified API in here
from .qrcode import sale,voidSale,refund

#Dictonary,List
def saleQR(payment_type, qr_code, ecr_ref, amount, additional_amount,payment_option,criteria_cardbin,transData,printOut):
    print("MIDDLE SALEQR called")
    result = sale(qr_code,ecr_ref,amount,transData,printOut)
    return result




