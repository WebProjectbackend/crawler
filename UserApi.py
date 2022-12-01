import urllib.request
import json
import re


newsList = {"n.news.naver" : "네이버 뉴스",
"newspim": "뉴스핌",
"siminilbo": "시민일보",
"cstimes": "컨슈머타임스",
"kdpress": "데일리경제",
"nbntv": "NBNTV",
"kookje": "국제신문",
"gukjenews": "국제뉴스",
"busaneconomy": "부산제일경제",
"srtimes": "SR타임스 모바일 사이트",
"shinailbo": "신아일보",
"dizzotv": "디지틀조선TV",
"kpenews": "한국정경신문",
"cnbnews": "CNB뉴스",
"asiatoday": "아시아투데이",
"breaknews": "브레이크뉴스",
"daily.hankooki": "데일리한국",
"ilyo": "일요신문"}
newsListNumber = ["n.news.naver", "newspim", "siminilbo", "cstimes", "kdpress", "nbntv", "kookje", "gukjenews", "busaneconomy",
                  "srtimes", "shinailbo", "dizzotv", "kpenews", "cnbnews", "asiatoday", "breaknews", "daily.hankooki", "ilyo"] 

def FindPress(data):
    ran = len(newsListNumber)
    for i in range(0, ran):
        if newsListNumber[i] in data:
            return newsList[newsListNumber[i]]
    return "NaN"

def ShowInfo(data):
    json_data = json.loads(data)
    for x in json_data["items"]:
        # re 모듈에 있는 정규 표현식 사용
        # re.sub(패턴, 교체할 문자열, 문자열, 최대 교체 수 , 플래그)
        # re.sub(a,b,c) -> c 문자열 안에 a라는 문자열을 찾아서 b로 바꿈
        # re.I : 대소문자 구분 X, re.S : 줄바꾸기 문자도 포함하여
        result_title = re.sub('<.+?>', '',x['title'], 0, re.I | re.S)  # title만 가져오기 위한 파싱
        result_description = re.sub('<.+?>', '',x['description'], 0, re.I | re.S)
        result_link = re.sub('<.+?>', '',x['link'], 0, re.I | re.S)
        result_press = FindPress(result_link)
        if "초코뮤직" in result_description or "초코뮤직" in result_title:
            print(f"기사 제목 : {result_title}")
            print(f"기사 본문 : {result_description}")
            print(f"기사 링크 : {result_link}")
            print(f"기사 언론사 : {result_press}")
            print("-------------------------------------------------------------------------")

client_id = '53Zlk_08EPnrNtdMMjqB'
client_secret = 'uEYc1RIM1z'

text = "초코뮤직"
encText = urllib.parse.quote(text)
url = "https://openapi.naver.com/v1/search/news.json?query=" + encText + "&display=100&start=1&sort=sim"

request = urllib.request.Request(url)
request.add_header('X-Naver-Client-Id', client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    data = response_body.decode('utf-8')
    ShowInfo(data)
else:
    print("Error Code:" + rescode)

