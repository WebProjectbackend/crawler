import requests
from bs4 import BeautifulSoup

# 네이버 뉴스 크롤링 -> 초코나 뮤직 이라는 단어가 들어만 있으면 다 나옴
naver_title_list = []
news_url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EC%B4%88%EC%BD%94%EB%AE%A4%EC%A7%81&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=74&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start="
for i in range(0, 10):
    num = (i * 10) + 1
    #print(num)
    url = news_url + "{}".format(num)
    #print(url)
    raw = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
    html = BeautifulSoup(raw.text, "html.parser")
    title = html.find_all("div" , {"class" : "news_area"})

    for t in title:
        link = t.find("a", {"class" : "news_tit"})
        ti = t.find("a", {"class" : "news_tit"}).text
        
        if "초코뮤직" in ti:
            print(ti)
            line = []
            line.append(ti)
            line.append(t.find("a", {"class" : "info press"}).text) # 언론사
            line.append(t.find("span", {"class" : "info"}).text) # 날짜
            line.append(link.attrs["href"]) # 링크
            naver_title_list.append(line)
        para = t.find("a", {"class" : "api_txt_lines dsc_txt_wrap"})
        if "초코뮤직" in para:
            print(ti)
            line = []
            line.append(ti)
            line.append(t.find("a", {"class" : "info press"}).text) # 언론사
            line.append(t.find("span", {"class" : "info"}).text) # 날짜
            line.append(link.attrs["href"]) # 링크
            naver_title_list.append(line)


# print(naver_title_list)
