import requests
import schedule
import time
from datetime import datetime


token1 = ""
token2 = ""
token3 = ""

all_token = [token1,token2,token3]


def covid_report(token):

    url_covid = "https://covid19.ddc.moph.go.th/api/Cases/today-cases-all"
    response  = requests.get(url_covid)
    new_case = response.json()[0]["new_case"]
    new_case = "{:,}".format(new_case)
    new_death = response.json()[0]["new_death"]
    date = response.json()[0]["txn_date"]
    
    year,month,day = date.split('-')
    day = day.lstrip("0")
    thai_full_months = [
        "มกราคม",
        "กุมภาพันธ์",
        "มีนาคม",
        "เมษายน",
        "พฤษภาคม",
        "มิถุนายน",
        "กรกฎาคม",
        "สิงหาคม",
        "กันยายน",
        "ตุลาคม",
        "พฤศจิกายน",
        "ธันวาคม",
    ]
    months = thai_full_months[int(month)-1]
    date_thai = day +" "+ months +" "+ str(int(year)+543) 
    
    url = 'https://notify-api.line.me/api/notify'

    headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+ token}

    msg_report = "\nยอดผู้ติดเชื้อโควิดวันนี้\n("  +date_thai  +  ")\nติดเชื้อ " + new_case +" ราย\nเสียชีวิต " +  str(new_death) + " ราย"
    r = requests.post(url, headers=headers, data = {'message':msg_report})


for token in all_token:
    covid_report(token)

   
