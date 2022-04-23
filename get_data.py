from pysondb import db
import datetime
import time
import locale
import requests

a=db.getDb("./database.json")

def save_data():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    rate = locale.atof(response.json()["bpi"]["USD"]["rate"].replace(",", ""))
    a.add({"rate": rate, "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    time.sleep(3)
    save_data()

save_data()