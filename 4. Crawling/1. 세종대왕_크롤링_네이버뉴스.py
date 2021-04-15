#!/usr/bin/env python
# coding: utf-8

# # 네이버 지도 크롤링

# ### 크롤링 함수 정의

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from fake_useragent import UserAgent
import csv
import time

RESULT_PATH = '/Users/yoonjeonghyeon/Desktop/python/crawling/'
now = datetime.now()

def crawler(maxpage, query, s_date, e_date, year):
    s_from = s_date.replace(".", "") # 시작 날짜 설정
    e_to = e_date.replace(".", "") # 종료 날짜 설정
    page = 1
    maxpage_t = (int(maxpage) - 1) * 10 + 1    
    path = "/Users/yoonjeonghyeon/Desktop/python/crawling/sejong"+ year +".csv" # 파일에 저장
    f = open(path, 'w', encoding = 'utf-8')

    wr = csv.writer(f)
    wr.writerow(['years','company','title','contents','link'])
    
    while page < maxpage_t:
        
        url = 'https://search.naver.com/search.naver?where=news&query=' + query + '&sort=0&ds=' + s_date + '&de=' + e_date + '&nso=so%3Ar%2Cp%3Afrom' + s_from + 'to' + e_to + '%2Ca%3A&start=' + str(page)

        # ua = UserAgent()
        # headers = {'User-Agent' : ua.random}

        req = requests.get(url)
        
        cont = req.content
        soup = BeautifulSoup(cont, 'html.parser')
        
        for urls in soup.select("a.info"):
            
            try:
                if urls["href"].startswith("https://news.naver.com"):
                        news_detail = []
                        
                        ua = UserAgent()
                        headers = {"User-Agent" : ua.random}
                        
                        breq = requests.get(urls["href"], headers = headers)
                        bsoup = BeautifulSoup(breq.content, 'html.parser')
                        
                        # 뉴스 제목 크롤링
                        title = bsoup.select('h3#articleTitle')[0].text
                        news_detail.append(title)
                        
                        # 뉴스 날짜 크롤링
                        pdate = bsoup.select('.t11')[0].get_text()[:11]
                        news_detail.append(pdate)
                        
                        # 뉴스 본문 크롤링
                        _text = bsoup.select('#articleBodyContents')[0].get_text().replace('\n', " ")
                        btext = _text.replace("// flash 오류를 우회하기 위한 함수 추가 function _flash_removeCallback() {}", "")
                        
                        news_detail.append(btext.strip())
                        news_detail.append(urls["href"])
                        
                        # 뉴스 언론사 크롤링
                        pcompany = bsoup.select('#footer address')[0].a.get_text()
                        news_detail.append(pcompany)
                                            
                        wr.writerow([news_detail[1].replace(',',''), news_detail[4].replace(',',''), news_detail[0].replace(',',''),
                                    news_detail[2].replace(',',''), news_detail[3].replace(',','')])
            except Exception as e:
                continue
        page += 10
        
    print('Completed!')
    
    f.close()


# ### 크롤링 코드 실행

# In[ ]:


# 2017년 뉴스 크롤링
crawler(100000, '세종시 부동산', '2017.01.01', '2017.12.31', '2017')
# 2018년 뉴스 크롤링
crawler(100000, '세종시 부동산', '2018.01.01', '2018.12.31', '2018')
# 2019년 뉴스 크롤링
crawler(100000, '세종시 부동산', '2019.01.01', '2019.12.31', '2019')
# 2020년 뉴스 크롤링
crawler(100000, '세종시 부동산', '2020.01.01', '2020.12.31', '2020')

