import sys
import requests
client_id = ""
client_secret = ""
lang = "Kor" # 언어 코드 ( Kor )
# url = "https://naveropenapi.apigw-pub.fin-ntruss.com/recog/v1/stt?lang=" + lang
url = "https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=" + lang

data = open("C:/Users/User/Downloads/test.mp3", 'rb')
headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret,
    "Content-Type": "application/octet-stream"
}
response = requests.post(url,  data=data, headers=headers)
rescode = response.status_code
if(rescode == 200):
    print (response.text)
else:
    print("Error : " + response.text)