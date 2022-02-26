import requests
from flask import *
from user_agent import *
app = Flask(__name__)
@app.route("/")
def q():
 return jsonify(Telegram="@JJJJzJJJ",Channel="@LLYYLLL")
@app.route("/api/check/instagram/JJJJzJJJ/")
def f():
 Email = request.args.get("Email")
 url = "https://www.instagram.com/accounts/login/ajax/"
 headers ={
"accept": "*/*",
"set-cookie":"csrftoken=pbue6mbF5LmIenm1zdbcQ1u7dcx2QJYw; Domain=.instagram.com; expires=Fri, 24-Feb-2023 21:57:51 GMT; Max-Age=31449600; Path=/; Secure",
"accept-encoding": "gzip, deflate, br",
"accept-language":"ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",'cookie':'csrftoken=pbue6mbF5LmIenm1zdbcQ1u7dcx2QJYw; mid=YhlQygABAAEb4ySI9IwK_HoaHItk; ig_did=222785FC-683C-4B45-8F9D-AF9DD07DF87B; ig_nrcb=1',
"content-length": "316",
"content-type": "application/x-www-form-urlencoded",
'sec-ch-ua':'"" Not A;Brand";v="99", "Chromium";v="98',
"sec-ch-ua-mobile": "?1",
'sec-ch-ua-platform': '"Android',
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-origin",
"user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.106 Mobile Safari/537.36",
"x-asbd-id": "198387",
"x-csrftoken": "pbue6mbF5LmIenm1zdbcQ1u7dcx2QJYw",
"x-ig-app-id": "1217981644879628",
"x-ig-www-claim": "0",
"x-instagram-ajax": "238ee7baa9c1",
"x-requested-with": "XMLHttpRequest",}
 data= {
"username": str(Email),
"optIntoOneTap": "false",
"queryParams": {},
"stopDeletionNonce": "",
"trustedDeviceRecords": {}}
 req = requests.post(url,headers=headers,data=data).text
 if '"user":true' in req:
   return jsonify(Telegram="@JJJJzJJJ",Email=Email,Check="Aailable✅")
 else:
  return jsonify(Telegram="@JJJJzJJJ",Email=Email,Checker="UnAailable❌")
app.run()
