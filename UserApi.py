import urllib.request

# https://developers.naver.com/apps/#/wizard/register
# 여기서 인증하고 발급받기

client_id = '53Zlk_08EPnrNtdMMjqB'
client_secret = 'uEYc1RIM1z'

text = input("검색할 단어를 입력하세요 : ")
encText = urllib.parse.quote(text)
url = "https://openapi.naver.com/v1/search/blog?query=" + encText

request = urllib.request.Request(url)
request.add_header('X-Naver-Client-Id', client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)