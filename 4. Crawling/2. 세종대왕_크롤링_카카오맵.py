#!/usr/bin/env python
# coding: utf-8

# # 크롤링 코드

# # 0. Import

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import pandas as pd
import csv


# ---
# # 크롤링 함수 정의
# ### 1번째 페이지 크롤링

# In[ ]:


def crawl_1st(start, end):
    result = []
    
    for i in range(start, end):
        if i == 4: # 광고 스킵
            continue
        
        driver.implicitly_wait(1)
        name = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[""" + str(i) + """]/div[3]/strong/a[2]""")
        result.append(name.text)

        driver.implicitly_wait(1)
        address = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[""" + str(i) + """]/div[5]/div[2]/p[1]""")
        result.append(address.text)
    
    # 16번째 크롤링
    driver.implicitly_wait(1)
    name = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[16]/div[3]/strong/a[2]""")
    result.append(name.text)

    driver.implicitly_wait(1)
    address = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[16]/div[5]/div[2]/p[1]""")
    result.append(address.text)
    
    print('crawling completed!')
    
    return result


# ---
# ### 2~5번째 페이지 크롤링

# In[ ]:


def crawl_2to5(start, end, s_page, e_page):
    result2 = []
    
    # 아래로 스크롤
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    
    # 장소 더보기 클릭
    driver.find_element_by_xpath("""//*[@id="info.search.place.more"]""").click()

    time.sleep(3)
    
    # 2 페이지 크롤링
    for i in range(start, end):
        if i == 4: # 광고 스킵
            continue
        
        driver.implicitly_wait(1)
        name = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[""" + str(i) + """]/div[3]/strong/a[2]""")
        result2.append(name.text)

        driver.implicitly_wait(1)
        address = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[""" + str(i) + """]/div[5]/div[2]/p[1]""")
        result2.append(address.text)
    
    # 16번째 크롤링
    driver.implicitly_wait(1)
    name = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[16]/div[3]/strong/a[2]""")
    result2.append(name.text)

    driver.implicitly_wait(1)
    address = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[16]/div[5]/div[2]/p[1]""")
    result2.append(address.text)
    
    # 3~5 페이지 크롤링
    for j in range(s_page, e_page):
        
        # 다음 버튼 누르기
        driver.find_element_by_xpath('''//*[@id="info.search.page.no''' + str(j) + '''"]''').click()
        
        time.sleep(2)

        # 다음 페이지 크롤링
        for k in range(start, end):
            if k == 4: # 광고 스킵
                continue
        
            driver.implicitly_wait(1)
            name = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[""" + str(k) + """]/div[3]/strong/a[2]""")
            result2.append(name.text)

            driver.implicitly_wait(1)
            address = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[""" + str(k) + """]/div[5]/div[2]/p[1]""")
            result2.append(address.text)
    
        # 16번째 크롤링
        driver.implicitly_wait(1)
        name = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[16]/div[3]/strong/a[2]""")
        result2.append(name.text)

        driver.implicitly_wait(1)
        address = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[16]/div[5]/div[2]/p[1]""")
        result2.append(address.text)
            
    return result2


# ---
# ### 6~10 페이지 크롤링

# In[ ]:


def crawl_6to10(start, end, s_page, e_page):
    result3 = []
    
    # 아래로 스크롤
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    
    # 장소 더보기 클릭
    driver.find_element_by_xpath("""//*[@id="info.search.place.more"]""").click()
    time.sleep(3)
    
    # 다음 탭으로 이동
    driver.find_element_by_xpath('''//*[@id="info.search.page.next"]''').click()
    time.sleep(3)
    
    # 페이지 크롤링
    for i in range(start, end):
        if i == 4: # 광고 스킵
            continue
        
        driver.implicitly_wait(1)
        name = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[""" + str(i) + """]/div[3]/strong/a[2]""")
        result3.append(name.text)

        driver.implicitly_wait(1)
        address = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[""" + str(i) + """]/div[5]/div[2]/p[1]""")
        result3.append(address.text)
    
    # 16번째 크롤링
    driver.implicitly_wait(1)
    name = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[16]/div[3]/strong/a[2]""")
    result3.append(name.text)

    driver.implicitly_wait(1)
    address = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[16]/div[5]/div[2]/p[1]""")
    result3.append(address.text)
    
    ### 7 ~ 10 크롤링 ###
    for j in range(s_page, e_page):
        
        # 다음 버튼 누르기
        driver.find_element_by_xpath('''//*[@id="info.search.page.no''' + str(j) + '''"]''').click()        
        time.sleep(2)

        # 페이지별 크롤링
        for k in range(start, end):
            if k == 4: # 광고 스킵
                continue
        
            driver.implicitly_wait(1)
            name = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[""" + str(k) + """]/div[3]/strong/a[2]""")
            result3.append(name.text)

            driver.implicitly_wait(1)
            address = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[""" + str(k) + """]/div[5]/div[2]/p[1]""")
            result3.append(address.text)
    
        # 16번째 크롤링
        driver.implicitly_wait(1)
        name = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[16]/div[3]/strong/a[2]""")
        result3.append(name.text)

        driver.implicitly_wait(1)
        address = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[16]/div[5]/div[2]/p[1]""")
        result3.append(address.text)
        
    return result3


# ---
# ### 6~ (5페이지 단위) 페이지 크롤링 (10페이지 이상)

# In[ ]:


def crawl_over11(start, end, s_page, e_page, pages):
    result4 = []
    
    # 아래로 스크롤
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    
    # 장소 더보기 클릭
    driver.find_element_by_xpath("""//*[@id="info.search.place.more"]""").click()
    time.sleep(3)
    
    # 다음 탭으로 이동
    driver.find_element_by_xpath('''//*[@id="info.search.page.next"]''').click()
    time.sleep(3)
    
    # 6 페이지 크롤링
    for i in range(start, end):
        if i == 4: # 광고 스킵
            continue
        
        driver.implicitly_wait(1)
        name = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[""" + str(i) + """]/div[3]/strong/a[2]""")
        result4.append(name.text)

        driver.implicitly_wait(1)
        address = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[""" + str(i) + """]/div[5]/div[2]/p[1]""")
        result4.append(address.text)
    
    # 16번째 크롤링
    driver.implicitly_wait(1)
    name = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[16]/div[3]/strong/a[2]""")
    result4.append(name.text)

    driver.implicitly_wait(1)
    address = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[16]/div[5]/div[2]/p[1]""")
    result4.append(address.text)
    
    ### 7 ~ 10 크롤링 ###
    for j in range(s_page, e_page):
        
        # 다음 버튼 누르기
        driver.find_element_by_xpath('''//*[@id="info.search.page.no''' + str(j) + '''"]''').click()        
        time.sleep(2)

        # 페이지별 크롤링
        for k in range(start, end):
            if k == 4: # 광고 스킵
                continue
        
            driver.implicitly_wait(1)
            name = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[""" + str(k) + """]/div[3]/strong/a[2]""")
            result4.append(name.text)

            driver.implicitly_wait(1)
            address = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[""" + str(k) + """]/div[5]/div[2]/p[1]""")
            result4.append(address.text)
    
        # 16번째 크롤링
        driver.implicitly_wait(1)
        name = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[16]/div[3]/strong/a[2]""")
        result4.append(name.text)

        driver.implicitly_wait(1)
        address = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[16]/div[5]/div[2]/p[1]""")
        result4.append(address.text)
    
    ### 다음 버튼 누른 후 5페이지 단위 크롤링 ###
    for num in range(1, pages):
        driver.find_element_by_xpath('''//*[@id="info.search.page.next"]''').click()
        time.sleep(3)
                
        for l in range(start, end):
            if l == 4: # 광고 스킵
                continue
        
            driver.implicitly_wait(1)
            name = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[""" + str(l) + """]/div[3]/strong/a[2]""")
            result4.append(name.text)

            driver.implicitly_wait(1)
            address = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[""" + str(l) + """]/div[5]/div[2]/p[1]""")
            result4.append(address.text)
    
        # 16번째 크롤링
        driver.implicitly_wait(1)
        name = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[16]/div[3]/strong/a[2]""")
        result4.append(name.text)

        driver.implicitly_wait(1)
        address = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[16]/div[5]/div[2]/p[1]""")
        result4.append(address.text)
    
        # 3 ~ 5 페이지 크롤링
        for m in range(s_page, e_page):
        
            # 다음 버튼 누르기
            driver.find_element_by_xpath('''//*[@id="info.search.page.no''' + str(m) + '''"]''').click()
            time.sleep(2)

            # 다음 페이지 크롤링
            for n in range(start, end):
                if n == 4: # 광고 스킵
                    continue
        
                driver.implicitly_wait(1)
                name = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[""" + str(n) + """]/div[3]/strong/a[2]""")
                result4.append(name.text)

                driver.implicitly_wait(1)
                address = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[""" + str(n) + """]/div[5]/div[2]/p[1]""")
                result4.append(address.text)
    
            # 16번째 크롤링
            driver.implicitly_wait(1)
            name = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[16]/div[3]/strong/a[2]""")
            result4.append(name.text)

            driver.implicitly_wait(1)
            address = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[16]/div[5]/div[2]/p[1]""")
            result4.append(address.text)
        
    return result4


# ---
# ### 5 페이지가 아닌 페이지 크롤링

# In[ ]:


def under5(start, end, s_page, e_page, pages):
    result5 = []
    
    # 아래로 스크롤
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    
    # 장소 더보기 클릭
    driver.find_element_by_xpath("""//*[@id="info.search.place.more"]""").click()
    time.sleep(3)
    
    # 다음 탭으로 이동
    for num in range(1, pages):
        driver.find_element_by_xpath('''//*[@id="info.search.page.next"]''').click()
        time.sleep(2)
    
    # 페이지 크롤링
    for i in range(start, end):
        if i == 4: # 광고 스킵
            continue
        
        driver.implicitly_wait(1)
        name = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[""" + str(i) + """]/div[3]/strong/a[2]""")
        result5.append(name.text)

        driver.implicitly_wait(1)
        address = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[""" + str(i) + """]/div[5]/div[2]/p[1]""")
        result5.append(address.text)
    
    # 16번째 크롤링
    driver.implicitly_wait(1)
    name = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[16]/div[3]/strong/a[2]""")
    result5.append(name.text)

    driver.implicitly_wait(1)
    address = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[16]/div[5]/div[2]/p[1]""")
    result5.append(address.text)
    
    ### 페이지 크롤링 ###
    for j in range(s_page, e_page):
        
        # 다음 버튼 누르기
        driver.find_element_by_xpath('''//*[@id="info.search.page.no''' + str(j) + '''"]''').click()        
        time.sleep(2)

        # 페이지별 크롤링
        for k in range(start, end):
            if k == 4: # 광고 스킵
                continue
        
            driver.implicitly_wait(1)
            name = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[""" + str(k) + """]/div[3]/strong/a[2]""")
            result5.append(name.text)

            driver.implicitly_wait(1)
            address = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[""" + str(k) + """]/div[5]/div[2]/p[1]""")
            result5.append(address.text)
    
        # 16번째 크롤링
        driver.implicitly_wait(1)
        name = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[16]/div[3]/strong/a[2]""")
        result5.append(name.text)

        driver.implicitly_wait(1)
        address = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[16]/div[5]/div[2]/p[1]""")
        result5.append(address.text)
        
    return result5


# ---
# ### 마지막 페이지 크롤링

# In[ ]:


def last(start, end, pages):
    result6 = []
    
    # 아래로 스크롤
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    
    # 장소 더보기 클릭
    driver.find_element_by_xpath("""//*[@id="info.search.place.more"]""").click()
    time.sleep(3)
    
    # pages 탭으로 이동
    for num in range(1, pages):
        driver.find_element_by_xpath('''//*[@id="info.search.page.next"]''').click()
        time.sleep(2)
        
    # n번째 페이지로 이동 (선택)
    # driver.find_element_by_xpath('''//*[@id="info.search.page.no2"]''').click()
    # time.sleep(2)
    
    for i in range(start, end):
        if i == 4: # 광고 스킵
            continue
        
        driver.implicitly_wait(1)
        name = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[""" + str(i) + """]/div[3]/strong/a[2]""")
        result6.append(name.text)

        driver.implicitly_wait(1)
        address = driver.find_element_by_xpath("""//*[@id="info.search.place.list"]/li[""" + str(i) + """]/div[5]/div[2]/p[1]""")
        result6.append(address.text)
        
    return result6


# ---
# # 1. 마트 크롤링
# 
# ### 1st function

# In[ ]:


# 검색어 설정
find = input('검색할 정보를 입력하세요: ')

# 크롬 실행
driver = webdriver.Chrome('/Users/yoonjeonghyeon/Desktop/python/chromedriver')
driver.get("https://map.kakao.com")
driver.implicitly_wait(5)

# 검색창에 검색어 입력하기
search_box = driver.find_element_by_css_selector("#search\.keyword\.query")
search_box.send_keys(find)

time.sleep(3)

# 검색버튼 누르기
search_box.send_keys(Keys.ENTER)
driver.find_element_by_xpath("""//*[@id="dimmedLayer"]""").click()

# 페이지 더보기 먼저 눌러야 할 경우
# driver.find_element_by_xpath("""//*[@id="info.search.place.more"]""").click()
# time.sleep(3)

소정1 = crawl_1st(1, 16)
전의1 = crawl_1st(1, 16)
전동1 = crawl_1st(1, 16)
연서1 = crawl_1st(1, 16)
조치원1 = crawl_1st(1, 16)
연동1 = crawl_1st(1, 16)
부강1 = crawl_1st(1, 16)
연기1 = crawl_1st(1, 16)
장군1 = crawl_1st(1, 16)
금남1 = crawl_1st(1, 16)
고운1 = crawl_1st(1, 16)
아름1 = crawl_1st(1, 16)
도담1 = crawl_1st(1, 16)
종촌1 = crawl_1st(1, 16)
다정1 = crawl_1st(1, 16)
새롬1 = crawl_1st(1, 16)
한솔1 = crawl_1st(1, 16)
대평1 = crawl_1st(1, 16)
보람1 = crawl_1st(1, 16)
소담1 = crawl_1st(1, 16)


# ### 2nd function

# In[ ]:


find = input('검색할 정보를 입력하세요: ')

driver = webdriver.Chrome('/Users/yoonjeonghyeon/Desktop/python/chromedriver')
driver.get("https://map.kakao.com")
driver.implicitly_wait(5)

# 검색창에 검색어 입력하기
search_box = driver.find_element_by_css_selector("#search\.keyword\.query")
search_box.send_keys(find)

time.sleep(3)

# 검색버튼 누르기
search_box.send_keys(Keys.ENTER)
driver.find_element_by_xpath("""//*[@id="dimmedLayer"]""").click()

소정2 = crawl_2to5(1, 16, 3, 6)
전동2 = crawl_2to5(1, 16, 3, 6)
연서2 = crawl_2to5(1, 16, 3, 6)
조치원2 = crawl_2to5(1, 16, 3, 6)
연동2 = crawl_2to5(1, 16, 3, 6)
부강2 = crawl_2to5(1, 16, 3, 6)
연기2 = crawl_2to5(1, 16, 3, 6)
장군2 = crawl_2to5(1, 16, 3, 6)
금남2 = crawl_2to5(1, 16, 3, 6)
고운2 = crawl_2to5(1, 16, 3, 6)
아름2 = crawl_2to5(1, 16, 3, 6)
도담2 = crawl_2to5(1, 16, 3, 6)
종촌2 = crawl_2to5(1, 16, 3, 6)
다정2 = crawl_2to5(1, 16, 3, 6)
새롬2 = crawl_2to5(1, 16, 3, 6)
한솔2 = crawl_2to5(1, 16, 3, 6)
대평2 = crawl_2to5(1, 16, 3, 6)
보람2 = crawl_2to5(1, 16, 3, 6)
소담2 = crawl_2to5(1, 16, 3, 6)


# ### 3-1 function

# In[ ]:


find = input('검색할 정보를 입력하세요: ')

driver = webdriver.Chrome('/Users/yoonjeonghyeon/Desktop/python/chromedriver')
driver.get("https://map.kakao.com")
driver.implicitly_wait(5)

# 검색창에 검색어 입력하기
search_box = driver.find_element_by_css_selector("#search\.keyword\.query")
search_box.send_keys(find)

time.sleep(3)

# 검색버튼 누르기
search_box.send_keys(Keys.ENTER)
driver.find_element_by_xpath("""//*[@id="dimmedLayer"]""").click()

연동3 = crawl_6to10(1, 16, 2, 6)
연기3 = crawl_6to10(1, 16, 2, 6)
금남3 = crawl_6to10(1, 16, 2, 6)


# ### 3-2 function

# In[ ]:


find = input('검색할 정보를 입력하세요: ')

driver = webdriver.Chrome('/Users/yoonjeonghyeon/Desktop/python/chromedriver')
driver.get("https://map.kakao.com")
driver.implicitly_wait(5)

# 검색창에 검색어 입력하기
search_box = driver.find_element_by_css_selector("#search\.keyword\.query")
search_box.send_keys(find)

time.sleep(3)

# 검색버튼 누르기
search_box.send_keys(Keys.ENTER)
driver.find_element_by_xpath("""//*[@id="dimmedLayer"]""").click()

소정3 = crawl_over11(1, 16, 2, 6, 3)


# ### 4th function

# In[ ]:


find = input('검색할 정보를 입력하세요: ')

driver = webdriver.Chrome('/Users/yoonjeonghyeon/Desktop/python/chromedriver')
driver.get("https://map.kakao.com")
driver.implicitly_wait(5)

# 검색창에 검색어 입력하기
search_box = driver.find_element_by_css_selector("#search\.keyword\.query")
search_box.send_keys(find)

time.sleep(3)

# 검색버튼 누르기
search_box.send_keys(Keys.ENTER)
driver.find_element_by_xpath("""//*[@id="dimmedLayer"]""").click()

소정4 = under5(1, 16, 1, 1, 4)
전의2 = under5(1, 16, 1, 1, 1)
전동3 = under5(1, 16, 1, 3, 2) 116
연서3 = under5(1, 16, 1, 5, 2)면 138
조치원3 = under5(1, 16, 1, 4, 2) 125
연동4 = under5(1, 16, 1, 1, 3)면 167
부강3 = under5(1, 16, 1, 1, 2)면 89
연기4 = under5(1, 16, 1, 1, 3)면 175
장군3 = under5(1, 16, 1, 5, 2)면 143
금남4 = under5(1, 16, 1, 1, 3)면 175
고운3 = under5(1, 16, 1, 5, 2)동 139
아름3 = under5(1, 16, 1, 4, 2)동 122
도담3 = under5(1, 16, 1, 5, 2)동 136
종촌3 = under5(1, 16, 1, 3, 2)동 117
다정3 = under5(1, 16, 1, 3, 2)동 115
새롬3 = under5(1, 16, 1, 3, 2)동 115
한솔3 = under5(1, 16, 1, 3, 2)동 109
대평3 = under5(1, 16, 1, 2, 2)동 102
보람3 = under5(1, 16, 1, 4, 2)동 123
소담3 = under5(1, 16, 1, 3, 2)동 117


# ### 5th function

# In[ ]:


find = input('검색할 정보를 입력하세요: ')

driver = webdriver.Chrome('/Users/yoonjeonghyeon/Desktop/python/chromedriver')
driver.get("https://map.kakao.com")
driver.implicitly_wait(5)

# 검색창에 검색어 입력하기
search_box = driver.find_element_by_css_selector("#search\.keyword\.query")
search_box.send_keys(find)

time.sleep(3)

# 검색버튼 누르기
search_box.send_keys(Keys.ENTER)
driver.find_element_by_xpath("""//*[@id="dimmedLayer"]""").click()

소정5 = last(1, 16, 5)
전의3 = last(1, 12, 1)
전동4 = last(1, 12, 2)
연서4 = last(1, 3, 2)
조치4 = last(1, 6, 2)
연동4 = last(1, 3, 3)
부강4 = last(1, 14, 2)
연기5 = last(1, 9, 3)
장군4 = last(1, 9, 2)
금남5 = last(1, 9, 3)
고운4 = last(1, 3, 2)
아름4 = last(1, 1, 2)
도담4 = last(1, 15, 2)
종촌4 = last(1, 12, 2)
다정4 = last(1, 9, 2)
새롬4 = last(1, 9, 2)
한솔4 = last(1, 4, 2)
대평4 = last(1, 12, 2)
보람4 = last(1, 3, 2)
소담4 = last(1, 12, 2)


# ---
# ### 데이터 합치기

# In[ ]:


소정 = 소정1 + 소정2 + 소정3 + 소정4 + 소정5
전의 = 전의1 + 전의2 + 전의3
전동 = 전의1 + 전의2 + 전의3 + 전의4
연서 = 연서1 + 연서2 + 연서3 + 연서4
조치원 = 조치원1 + 조치원2 + 조치원3 + 조치원4
연동 = 연동1 + 연동2 + 연동3 + 연동4
부강 = 부강1 + 부강2 + 부강3 + 부강4
연기 = 연기1 + 연기2 + 연기3 + 연기4 + 연기5
장군 = 장군1 + 장군2 + 장군3 + 장군4
금남 = 금남1 + 금남2 + 금남3 + 금남4 + 금남5
고운 = 고운1 + 고운2 + 고운3 + 고운4
아름 = 아름1 + 아름2 + 아름3 + 아름4
도담 = 도담1 + 도담2 + 도담3 + 도담4
종촌 = 종촌1 + 종촌2 + 종촌3 + 종촌4
다정 = 다정1 + 다정2 + 다정3 + 다정4
새롬 = 새롬1 + 새롬2 + 새롬3 + 새롬4
한솔 = 한솔1 + 한솔2 + 한솔3 + 한솔4
대평 = 대평1 + 대평2 + 대평3 + 대평4
보람 = 보람1 + 보람2 + 보람3 + 보람4
소담 = 소담1 + 소담2 + 소담3 + 소담4


# ### 이름 / 주소 분리 후 df로 변환,  csv로 저장

# In[ ]:


# 소정면 데이터
name = []
address = []

for i in range(len(소정)):
    if i % 2 == 0:
        name.append(소정[i])
    else:
        address.append(소정[i])
        
df소정 = pd.DataFrame(columns = ['name', 'address'])
    
df소정['name'] = name
df소정['address'] = address

df소정.to_csv("sojeong2.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 전의면 데이터
name = []
address = []

for i in range(len(전의)):
    if i % 2 == 0:
        name.append(전의[i])
    else:
        address.append(전의[i])
        
df전의 = pd.DataFrame(columns = ['name', 'address'])
    
df전의['name'] = name
df전의['address'] = address

df전의.to_csv("jeonui2.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 전동면 데이터
name = []
address = []

for i in range(len(전동)):
    if i % 2 == 0:
        name.append(전동[i])
    else:
        address.append(전동[i])
        
df전동 = pd.DataFrame(columns = ['name', 'address'])
    
df전동['name'] = name
df전동['address'] = address

df전동.to_csv("jeondong2.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 연서면 데이터
name = []
address = []

for i in range(len(연서)):
    if i % 2 == 0:
        name.append(연서[i])
    else:
        address.append(연서[i])
        
df연서 = pd.DataFrame(columns = ['name', 'address'])
    
df연서['name'] = name
df연서['address'] = address

df연서.to_csv("yeonseo2.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 조치원읍 데이터
name = []
address = []

for i in range(len(조치원)):
    if i % 2 == 0:
        name.append(조치원[i])
    else:
        address.append(조치원[i])
        
df조치원 = pd.DataFrame(columns = ['name', 'address'])
    
df조치원['name'] = name
df조치원['address'] = address

df조치원.to_csv("jochiwon2.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 연동면 데이터
name = []
address = []

for i in range(len(연동)):
    if i % 2 == 0:
        name.append(연동[i])
    else:
        address.append(연동[i])
        
df연동 = pd.DataFrame(columns = ['name', 'address'])
    
df연동['name'] = name
df연동['address'] = address

df연동.to_csv("yeondong2.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 부강면 데이터
name = []
address = []

for i in range(len(부강)):
    if i % 2 == 0:
        name.append(부강[i])
    else:
        address.append(부강[i])
        
df부강 = pd.DataFrame(columns = ['name', 'address'])
    
df부강['name'] = name
df부강['address'] = address

df부강.to_csv("bugang2.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 연기면 데이터
name = []
address = []

for i in range(len(연기)):
    if i % 2 == 0:
        name.append(연기[i])
    else:
        address.append(연기[i])
        
df연기 = pd.DataFrame(columns = ['name', 'address'])
    
df연기['name'] = name
df연기['address'] = address

df연기.to_csv("yeongi2.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 장군면 데이터
name = []
address = []

for i in range(len(장군)):
    if i % 2 == 0:
        name.append(장군[i])
    else:
        address.append(장군[i])
        
df장군 = pd.DataFrame(columns = ['name', 'address'])
    
df장군['name'] = name
df장군['address'] = address

df장군.to_csv("janggoon2.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 금남면 데이터
name = []
address = []

for i in range(len(금남)):
    if i % 2 == 0:
        name.append(금남[i])
    else:
        address.append(금남[i])
        
df금남 = pd.DataFrame(columns = ['name', 'address'])
    
df금남['name'] = name
df금남['address'] = address

df금남.to_csv("geumnam2.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 고운동 데이터
name = []
address = []

for i in range(len(고운)):
    if i % 2 == 0:
        name.append(고운[i])
    else:
        address.append(고운[i])
        
df고운 = pd.DataFrame(columns = ['name', 'address'])
    
df고운['name'] = name
df고운['address'] = address

df고운.to_csv("goun2.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 아름동 데이터
name = []
address = []

for i in range(len(아름)):
    if i % 2 == 0:
        name.append(아름[i])
    else:
        address.append(아름[i])
        
df아름 = pd.DataFrame(columns = ['name', 'address'])
    
df아름['name'] = name
df아름['address'] = address

df아름.to_csv("areum2.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 도담동 데이터
name = []
address = []

for i in range(len(도담)):
    if i % 2 == 0:
        name.append(도담[i])
    else:
        address.append(도담[i])
        
df도담 = pd.DataFrame(columns = ['name', 'address'])
    
df도담['name'] = name
df도담['address'] = address

df도담.to_csv("dodam2.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 종촌동 데이터
name = []
address = []

for i in range(len(종촌)):
    if i % 2 == 0:
        name.append(종촌[i])
    else:
        address.append(종촌[i])
        
df종촌 = pd.DataFrame(columns = ['name', 'address'])
    
df종촌['name'] = name
df종촌['address'] = address

df종촌.to_csv("jongchon2.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 다정동 데이터
name = []
address = []

for i in range(len(다정)):
    if i % 2 == 0:
        name.append(다정[i])
    else:
        address.append(다정[i])
        
df다정 = pd.DataFrame(columns = ['name', 'address'])
    
df다정['name'] = name
df다정['address'] = address

df다정.to_csv("dajeong2.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 새롬동 데이터
name = []
address = []

for i in range(len(새롬)):
    if i % 2 == 0:
        name.append(새롬[i])
    else:
        address.append(새롬[i])
        
df새롬 = pd.DataFrame(columns = ['name', 'address'])
    
df새롬['name'] = name
df새롬['address'] = address

df새롬.to_csv("saerom2.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 한솔동 데이터
name = []
address = []

for i in range(len(한솔)):
    if i % 2 == 0:
        name.append(한솔[i])
    else:
        address.append(한솔[i])
        
df한솔 = pd.DataFrame(columns = ['name', 'address'])
    
df한솔['name'] = name
df한솔['address'] = address

df한솔.to_csv("hansol2.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 대평동 데이터
name = []
address = []

for i in range(len(대평)):
    if i % 2 == 0:
        name.append(대평[i])
    else:
        address.append(대평[i])
        
df대평 = pd.DataFrame(columns = ['name', 'address'])
    
df대평['name'] = name
df대평['address'] = address

df대평.to_csv("daepyeong2.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 보람동 데이터
name = []
address = []

for i in range(len(보람)):
    if i % 2 == 0:
        name.append(보람[i])
    else:
        address.append(보람[i])
        
df보람 = pd.DataFrame(columns = ['name', 'address'])
    
df보람['name'] = name
df보람['address'] = address

df보람.to_csv("boram2.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 소담동 데이터
name = []
address = []

for i in range(len(소담)):
    if i % 2 == 0:
        name.append(소담[i])
    else:
        address.append(소담[i])
        
df소담 = pd.DataFrame(columns = ['name', 'address'])
    
df소담['name'] = name
df소담['address'] = address

df소담.to_csv("sojeong2.csv", mode = 'w', encoding = 'utf-8')


# ---
# ### 데이터 가공

# In[ ]:


import pandas as pd
import numpy as np

print("pandas version: ", pd.__version__)


# In[ ]:


data1 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling2/sojeong2.csv', index_col = 0)
data2 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling2/jeonui2.csv', index_col = 0)
data3 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling2/jeondong2.csv', index_col = 0)
data4 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling2/yeonseo2.csv', index_col = 0)
data5 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling2/jochiwon2.csv', index_col = 0)
data6 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling2/yeondong2.csv', index_col = 0)
data7 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling2/bugang2.csv', index_col = 0)
data8 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling2/yeongi2.csv', index_col = 0)
data9 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling2/janggoon2.csv', index_col = 0)
data10 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling2/geumnam2.csv', index_col = 0)
data11 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling2/goun2.csv', index_col = 0)
data12 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling2/areum2.csv', index_col = 0)
data13 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling2/dodam2.csv', index_col = 0)
data14 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling2/jongchon2.csv', index_col = 0)
data15 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling2/dajeong2.csv', index_col = 0)
data16 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling2/saerom2.csv', index_col = 0)
data17 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling2/hansol2.csv', index_col = 0)
data18 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling2/daepyeong2.csv', index_col = 0)
data19 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling2/boram2.csv', index_col = 0)
data20 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling2/sodam2.csv', index_col = 0)


# In[ ]:


# 앞에서 크롤링 한 데이터 모두 합치기
df = pd.concat([data1, data2, data3, data4,
                     data5, data6, data7, data8,
                     data9, data10, data11, data12,
                     data13, data14, data15, data16,
                     data17, data18, data19, data20], ignore_index = True)


# In[ ]:


# 중복되는 주소 drop
df2 = df.drop_duplicates(['address'])
# 세종시가 아닌 곳은 drop
cond1 = df2['address'].str.contains('세종특별자치시')
df3 = df2[cond1]
# 우리가 원하는 마트가 아닌 곳은 drop
cond2 = ~ df3['name'].str.contains('CU|전기차|펫마트|지스마트네트웍스|ABC|고기마트|휴대폰|크린토피아|크린시아|낚시|공중전화')
df4 = df3[cond2]
df4.to_csv('sejongmart_utf8.csv', mode = 'w', encoding = 'utf-8')


# # 2. 은행 크롤링
# ### 1st function

# In[ ]:


# 검색어 설정
find = input('검색할 정보를 입력하세요: ')

# 크롬 실행
driver = webdriver.Chrome('/Users/yoonjeonghyeon/Desktop/python/chromedriver')
driver.get("https://map.kakao.com")
driver.implicitly_wait(5)

# 검색창에 검색어 입력하기
search_box = driver.find_element_by_css_selector("#search\.keyword\.query")
search_box.send_keys(find)

time.sleep(3)

# 검색버튼 누르기
search_box.send_keys(Keys.ENTER)
driver.find_element_by_xpath("""//*[@id="dimmedLayer"]""").click()

# 페이지 더보기 먼저 눌러야 할 경우
# driver.find_element_by_xpath("""//*[@id="info.search.place.more"]""").click()
# time.sleep(3)

소정1 = crawl_1st(1, 16)
전의1 = crawl_1st(1, 16)
전동1 = crawl_1st(1, 16)
연서1 = crawl_1st(1, 16)
조치원1 = crawl_1st(1, 16)
연동1 = crawl_1st(1, 16)
부강1 = crawl_1st(1, 16)
연기1 = crawl_1st(1, 16)
장군1 = crawl_1st(1, 16)
금남1 = crawl_1st(1, 16)
고운1 = crawl_1st(1, 16)
아름1 = crawl_1st(1, 16)
도담1 = crawl_1st(1, 16)
종촌1 = crawl_1st(1, 16)
다정1 = crawl_1st(1, 16)
새롬1 = crawl_1st(1, 16)
한솔1 = crawl_1st(1, 16)
대평1 = crawl_1st(1, 16)
보람1 = crawl_1st(1, 16)
소담1 = crawl_1st(1, 16)


# ### 2nd function

# In[ ]:


find = input('검색할 정보를 입력하세요: ')

driver = webdriver.Chrome('/Users/yoonjeonghyeon/Desktop/python/chromedriver')
driver.get("https://map.kakao.com")
driver.implicitly_wait(5)

# 검색창에 검색어 입력하기
search_box = driver.find_element_by_css_selector("#search\.keyword\.query")
search_box.send_keys(find)

time.sleep(3)

# 검색버튼 누르기
search_box.send_keys(Keys.ENTER)
driver.find_element_by_xpath("""//*[@id="dimmedLayer"]""").click()

소정2 = crawl_2to5(1, 16, 3, 6)
전동2 = crawl_2to5(1, 16, 3, 6)
연서2 = crawl_2to5(1, 16, 3, 6)
조치원2 = crawl_2to5(1, 16, 3, 6)
연동2 = crawl_2to5(1, 16, 3, 6)
부강2 = crawl_2to5(1, 16, 3, 6)
연기2 = crawl_2to5(1, 16, 3, 6)
장군2 = crawl_2to5(1, 16, 3, 6)
금남2 = crawl_2to5(1, 16, 3, 6)
고운2 = crawl_2to5(1, 16, 3, 6)
아름2 = crawl_2to5(1, 16, 3, 6)
도담2 = crawl_2to5(1, 16, 3, 6)
종촌2 = crawl_2to5(1, 16, 3, 6)
다정2 = crawl_2to5(1, 16, 3, 6)
새롬2 = crawl_2to5(1, 16, 3, 6)
한솔2 = crawl_2to5(1, 16, 3, 6)
대평2 = crawl_2to5(1, 16, 3, 6)
보람2 = crawl_2to5(1, 16, 3, 6)
소담2 = crawl_2to5(1, 16, 3, 6)


# ### 3rd function

# In[ ]:


find = input('검색할 정보를 입력하세요: ')

driver = webdriver.Chrome('/Users/yoonjeonghyeon/Desktop/python/chromedriver')
driver.get("https://map.kakao.com")
driver.implicitly_wait(5)

# 검색창에 검색어 입력하기
search_box = driver.find_element_by_css_selector("#search\.keyword\.query")
search_box.send_keys(find)

time.sleep(3)

# 검색버튼 누르기
search_box.send_keys(Keys.ENTER)
driver.find_element_by_xpath("""//*[@id="dimmedLayer"]""").click()

소정3 = crawl_6to10(1, 16, 2, 6)
연서3 = crawl_6to10(1, 16, 2, 6)
연동3 = crawl_6to10(1, 16, 2, 6)
연기3 = crawl_6to10(1, 16, 2, 6)
장군3 = crawl_6to10(1, 16, 2, 6)
금남3 = crawl_6to10(1, 16, 2, 6)
고운3 = crawl_6to10(1, 16, 2, 6)
도담3 = crawl_6to10(1, 16, 2, 6)
다정3 = crawl_6to10(1, 16, 2, 6)
새롬3 = crawl_6to10(1, 16, 2, 6)
보람3 = crawl_6to10(1, 16, 2, 6)
소담3 = crawl_6to10(1, 16, 2, 6)


# ### 4th function

# In[ ]:


find = input('검색할 정보를 입력하세요: ')

driver = webdriver.Chrome('/Users/yoonjeonghyeon/Desktop/python/chromedriver')
driver.get("https://map.kakao.com")
driver.implicitly_wait(5)

# 검색창에 검색어 입력하기
search_box = driver.find_element_by_css_selector("#search\.keyword\.query")
search_box.send_keys(find)

time.sleep(3)

# 검색버튼 누르기
search_box.send_keys(Keys.ENTER)
driver.find_element_by_xpath("""//*[@id="dimmedLayer"]""").click()

소정4 = under5(1, 16, 2, 6, 4)
전동3 = under5(1, 16, 2, 4, 3)
조치원3 = under5(1, 16, 2, 4, 3)
연동3 = under5(1, 16, 2, 5, 3)
부강3 = under5(1, 16, 1, 1, 3)
연기4 = under5(1, 16, 2, 4, 3)
장군4 = under5(1, 16, 2, 3, 3)
금남4 = under5(1, 16, 2, 4, 3)
아름3 = under5(1, 16, 2, 5, 3)
종촌3 = under5(1, 16, 2, 5, 3)
한솔3 = under5(1, 16, 2, 5, 3)
대평3 = under5(1, 16, 2, 5, 3)
보람4 = under5(1, 16, 1, 1, 3)
소담4 = under5(1, 16, 1, 1, 3)


# ### 5th function

# In[ ]:


find = input('검색할 정보를 입력하세요: ')

driver = webdriver.Chrome('/Users/yoonjeonghyeon/Desktop/python/chromedriver')
driver.get("https://map.kakao.com")
driver.implicitly_wait(5)

# 검색창에 검색어 입력하기
search_box = driver.find_element_by_css_selector("#search\.keyword\.query")
search_box.send_keys(find)

time.sleep(3)

# 검색버튼 누르기
search_box.send_keys(Keys.ENTER)
driver.find_element_by_xpath("""//*[@id="dimmedLayer"]""").click()

소정5 = last(1, 9, 4)
전의2 = last(1, 7, 1)
전동4 = last(1, 1, 2)
연서4 = last(1, 9, 3)
조치원4 = last(1, 6, 2)
연동4 = last(1, 15, 3)
부강4 = last(1, 10, 2)
연기5 = last(1, 12, 3)
장군5 = last(1, 15, 3)
금남5 = last(1, 12, 3)
고운4 = last(1, 7, 3)
아름4 = last(1, 13, 2)
도담4 = last(1, 9, 3)
종촌4 = last(1, 8, 2)
다정4 = last(1, 4, 3)
새롬4 = last(1, 4, 3)
한솔4 = last(1, 3, 2)
대평4 = last(1, 11, 2)
보람5 = last(1, 8, 3)


# ---
# ## 데이터 합치기

# In[ ]:


소정 = 소정1 + 소정2 + 소정3 + 소정4 + 소정5
전의 = 전의1 + 전의2
전동 = 전의1 + 전의2 + 전의3 + 전의4
연서 = 연서1 + 연서2 + 연서3 + 연서4
조치원 = 조치원1 + 조치원2 + 조치원3 + 조치원4
연동 = 연동1 + 연동2 + 연동3 + 연동4
부강 = 부강1 + 부강2 + 부강3 + 부강4
연기 = 연기1 + 연기2 + 연기3 + 연기4 + 연기5
장군 = 장군1 + 장군2 + 장군3 + 장군4 + 장군5
금남 = 금남1 + 금남2 + 금남3 + 금남4 + 금남5
고운 = 고운1 + 고운2 + 고운3 + 고운4
아름 = 아름1 + 아름2 + 아름3 + 아름4
도담 = 도담1 + 도담2 + 도담3 + 도담4
종촌 = 종촌1 + 종촌2 + 종촌3 + 종촌4
다정 = 다정1 + 다정2 + 다정3 + 다정4
새롬 = 새롬1 + 새롬2 + 새롬3 + 새롬4
한솔 = 한솔1 + 한솔2 + 한솔3 + 한솔4
대평 = 대평1 + 대평2 + 대평3 + 대평4
보람 = 보람1 + 보람2 + 보람3 + 보람4
소담 = 소담1 + 소담2 + 소담3 + 소담4


# ### 이름 / 주소 분리 후 df로 변환,  csv로 저장

# In[ ]:


# 소정면 데이터
name = []
address = []

for i in range(len(소정)):
    if i % 2 == 0:
        name.append(소정[i])
    else:
        address.append(소정[i])
        
df소정 = pd.DataFrame(columns = ['name', 'address'])
    
df소정['name'] = name
df소정['address'] = address

df소정.to_csv("sojeong1.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 전의면 데이터
name = []
address = []

for i in range(len(전의)):
    if i % 2 == 0:
        name.append(전의[i])
    else:
        address.append(전의[i])
        
df전의 = pd.DataFrame(columns = ['name', 'address'])
    
df전의['name'] = name
df전의['address'] = address

df전의.to_csv("jeonui1.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 전동면 데이터
name = []
address = []

for i in range(len(전동)):
    if i % 2 == 0:
        name.append(전동[i])
    else:
        address.append(전동[i])
        
df전동 = pd.DataFrame(columns = ['name', 'address'])
    
df전동['name'] = name
df전동['address'] = address

df전동.to_csv("jeondong.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 연서면 데이터
name = []
address = []

for i in range(len(연서)):
    if i % 2 == 0:
        name.append(연서[i])
    else:
        address.append(연서[i])
        
df연서 = pd.DataFrame(columns = ['name', 'address'])
    
df연서['name'] = name
df연서['address'] = address

df연서.to_csv("yeonseo1.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 조치원읍 데이터
name = []
address = []

for i in range(len(조치원)):
    if i % 2 == 0:
        name.append(조치원[i])
    else:
        address.append(조치원[i])
        
df조치원 = pd.DataFrame(columns = ['name', 'address'])
    
df조치원['name'] = name
df조치원['address'] = address

df조치원.to_csv("jochiwon1.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 연동면 데이터
name = []
address = []

for i in range(len(연동)):
    if i % 2 == 0:
        name.append(연동[i])
    else:
        address.append(연동[i])
        
df연동 = pd.DataFrame(columns = ['name', 'address'])
    
df연동['name'] = name
df연동['address'] = address

df연동.to_csv("yeondong1.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 부강면 데이터
name = []
address = []

for i in range(len(부강)):
    if i % 2 == 0:
        name.append(부강[i])
    else:
        address.append(부강[i])
        
df부강 = pd.DataFrame(columns = ['name', 'address'])
    
df부강['name'] = name
df부강['address'] = address

df부강.to_csv("bugang1.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 연기면 데이터
name = []
address = []

for i in range(len(연기)):
    if i % 2 == 0:
        name.append(연기[i])
    else:
        address.append(연기[i])
        
df연기 = pd.DataFrame(columns = ['name', 'address'])
    
df연기['name'] = name
df연기['address'] = address

df연기.to_csv("yeongi1.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 장군면 데이터
name = []
address = []

for i in range(len(장군)):
    if i % 2 == 0:
        name.append(장군[i])
    else:
        address.append(장군[i])
        
df장군 = pd.DataFrame(columns = ['name', 'address'])
    
df장군['name'] = name
df장군['address'] = address

df장군.to_csv("janggoon1.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 금남면 데이터
name = []
address = []

for i in range(len(금남)):
    if i % 2 == 0:
        name.append(금남[i])
    else:
        address.append(금남[i])
        
df금남 = pd.DataFrame(columns = ['name', 'address'])
    
df금남['name'] = name
df금남['address'] = address

df금남.to_csv("geumnam1.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 고운동 데이터
name = []
address = []

for i in range(len(고운)):
    if i % 2 == 0:
        name.append(고운[i])
    else:
        address.append(고운[i])
        
df고운 = pd.DataFrame(columns = ['name', 'address'])
    
df고운['name'] = name
df고운['address'] = address

df고운.to_csv("goun1.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 아름동 데이터
name = []
address = []

for i in range(len(아름)):
    if i % 2 == 0:
        name.append(아름[i])
    else:
        address.append(아름[i])
        
df아름 = pd.DataFrame(columns = ['name', 'address'])
    
df아름['name'] = name
df아름['address'] = address

df아름.to_csv("areum1.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 도담동 데이터
name = []
address = []

for i in range(len(도담)):
    if i % 2 == 0:
        name.append(도담[i])
    else:
        address.append(도담[i])
        
df도담 = pd.DataFrame(columns = ['name', 'address'])
    
df도담['name'] = name
df도담['address'] = address

df도담.to_csv("dodam1.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 종촌동 데이터
name = []
address = []

for i in range(len(종촌)):
    if i % 2 == 0:
        name.append(종촌[i])
    else:
        address.append(종촌[i])
        
df종촌 = pd.DataFrame(columns = ['name', 'address'])
    
df종촌['name'] = name
df종촌['address'] = address

df종촌.to_csv("jongchon1.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 다정동 데이터
name = []
address = []

for i in range(len(다정)):
    if i % 2 == 0:
        name.append(다정[i])
    else:
        address.append(다정[i])
        
df다정 = pd.DataFrame(columns = ['name', 'address'])
    
df다정['name'] = name
df다정['address'] = address

df다정.to_csv("dajeong1.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 새롬동 데이터
name = []
address = []

for i in range(len(새롬)):
    if i % 2 == 0:
        name.append(새롬[i])
    else:
        address.append(새롬[i])
        
df새롬 = pd.DataFrame(columns = ['name', 'address'])
    
df새롬['name'] = name
df새롬['address'] = address

df새롬.to_csv("saerom1.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 한솔동 데이터
name = []
address = []

for i in range(len(한솔)):
    if i % 2 == 0:
        name.append(한솔[i])
    else:
        address.append(한솔[i])
        
df한솔 = pd.DataFrame(columns = ['name', 'address'])
    
df한솔['name'] = name
df한솔['address'] = address

df한솔.to_csv("hansol1.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 대평동 데이터
name = []
address = []

for i in range(len(대평)):
    if i % 2 == 0:
        name.append(대평[i])
    else:
        address.append(대평[i])
        
df대평 = pd.DataFrame(columns = ['name', 'address'])
    
df대평['name'] = name
df대평['address'] = address

df대평.to_csv("daepyeong1.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


name = []
address = []

for i in range(len(보람)):
    if i % 2 == 0:
        name.append(보람[i])
    else:
        address.append(보람[i])
        
df보람 = pd.DataFrame(columns = ['name', 'address'])
    
df보람['name'] = name
df보람['address'] = address

df보람.to_csv("boram1.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 소담동 데이터
name = []
address = []

for i in range(len(소담)):
    if i % 2 == 0:
        name.append(소담[i])
    else:
        address.append(소담[i])
        
df소담 = pd.DataFrame(columns = ['name', 'address'])
    
df소담['name'] = name
df소담['address'] = address

df소담.to_csv("sojeong1.csv", mode = 'w', encoding = 'utf-8')


# ---
# ### 데이터 가공

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


data1 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling1/sojeong.csv', index_col = 0)
data2 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling1/jeonui.csv', index_col = 0)
data3 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling1/jeondong.csv', index_col = 0)
data4 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling1/yeonseo.csv', index_col = 0)
data5 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling1/jochiwon.csv', index_col = 0)
data6 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling1/yeondong.csv', index_col = 0)
data7 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling1/bugang.csv', index_col = 0)
data8 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling1/yeongi.csv', index_col = 0)
data9 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling1/janggoon.csv', index_col = 0)
data10 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling1/geumnam.csv', index_col = 0)
data11 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling1/goun.csv', index_col = 0)
data12 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling1/areum.csv', index_col = 0)
data13 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling1/dodam.csv', index_col = 0)
data14 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling1/jongchon.csv', index_col = 0)
data15 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling1/dajeong.csv', index_col = 0)
data16 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling1/saerom.csv', index_col = 0)
data17 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling1/hansol.csv', index_col = 0)
data18 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling1/daepyeong.csv', index_col = 0)
data19 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling1/boram.csv', index_col = 0)
data20 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling1/sodam.csv', index_col = 0)


# In[ ]:


# 앞에서 구한 데이터 모두 합치기
df = pd.concat([data1, data2, data3, data4,
                     data5, data6, data7, data8,
                     data9, data10, data11, data12,
                     data13, data14, data15, data16,
                     data17, data18, data19, data20], ignore_index = True)


# In[ ]:


# 중복되는 주소는 drop
df2 = df.drop_duplicates(['address'])
# 세종시가 아닌 곳은 drop
condition = df2['address'].str.contains('세종특별자치시')
df3 = df2[condition]
df3.to_csv('sejongbank_utf8.csv', mode = 'w', encoding = 'utf-8')


# ---
# # 3. 병원 크롤링
# ### 1st function

# In[ ]:


# 검색어 설정
find = input('검색할 정보를 입력하세요: ')

# 크롬 실행
driver = webdriver.Chrome('/Users/yoonjeonghyeon/Desktop/python/chromedriver')
driver.get("https://map.kakao.com")
driver.implicitly_wait(5)

# 검색창에 검색어 입력하기
search_box = driver.find_element_by_css_selector("#search\.keyword\.query")
search_box.send_keys(find)

time.sleep(3)

# 검색버튼 누르기
search_box.send_keys(Keys.ENTER)
driver.find_element_by_xpath("""//*[@id="dimmedLayer"]""").click()

# 페이지 더보기 먼저 눌러야 할 경우
# driver.find_element_by_xpath("""//*[@id="info.search.place.more"]""").click()
# time.sleep(3)

소정1 = crawl_1st(1, 16)
전의1 = crawl_1st(1, 16)
전동1 = crawl_1st(1, 16)
연서1 = crawl_1st(1, 16)
조치원1 = crawl_1st(1, 16)
연동1 = crawl_1st(1, 16)
부강1 = crawl_1st(1, 16)
연기1 = crawl_1st(1, 16)
장군1 = crawl_1st(1, 16)
금남1 = crawl_1st(1, 16)
고운1 = crawl_1st(1, 16)
아름1 = crawl_1st(1, 16)
도담1 = crawl_1st(1, 16)
종촌1 = crawl_1st(1, 16)
다정1 = crawl_1st(1, 16)
새롬1 = crawl_1st(1, 16)
한솔1 = crawl_1st(1, 16)
대평1 = crawl_1st(1, 16)
보람1 = crawl_1st(1, 16)
소담1 = crawl_1st(1, 16)


# ### 2nd function

# In[ ]:


find = input('검색할 정보를 입력하세요: ')

driver = webdriver.Chrome('/Users/yoonjeonghyeon/Desktop/python/chromedriver')
driver.get("https://map.kakao.com")
driver.implicitly_wait(5)

# 검색창에 검색어 입력하기
search_box = driver.find_element_by_css_selector("#search\.keyword\.query")
search_box.send_keys(find)

time.sleep(3)

# 검색버튼 누르기
search_box.send_keys(Keys.ENTER)
driver.find_element_by_xpath("""//*[@id="dimmedLayer"]""").click()

소정2 = crawl_2to5(1, 16, 3, 6)
전동2 = crawl_2to5(1, 16, 3, 6)
연서2 = crawl_2to5(1, 16, 3, 6)
조치원2 = crawl_2to5(1, 16, 3, 6)
연동2 = crawl_2to5(1, 16, 3, 6)
부강2 = crawl_2to5(1, 16, 3, 6)
연기2 = crawl_2to5(1, 16, 3, 6)
장군2 = crawl_2to5(1, 16, 3, 6)
금남2 = crawl_2to5(1, 16, 3, 6)
고운2 = crawl_2to5(1, 16, 3, 6)
아름2 = crawl_2to5(1, 16, 3, 6)
도담2 = crawl_2to5(1, 16, 3, 6)
종촌2 = crawl_2to5(1, 16, 3, 6)
다정2 = crawl_2to5(1, 16, 3, 6)
새롬2 = crawl_2to5(1, 16, 3, 6)
한솔2 = crawl_2to5(1, 16, 3, 6)
대평2 = crawl_2to5(1, 16, 3, 6)
보람2 = crawl_2to5(1, 16, 3, 6)
소담2 = crawl_2to5(1, 16, 3, 6)


# #### 3rd function

# In[ ]:


find = input('검색할 정보를 입력하세요: ')

driver = webdriver.Chrome('/Users/yoonjeonghyeon/Desktop/python/chromedriver')
driver.get("https://map.kakao.com")
driver.implicitly_wait(5)

# 검색창에 검색어 입력하기
search_box = driver.find_element_by_css_selector("#search\.keyword\.query")
search_box.send_keys(find)

time.sleep(3)

# 검색버튼 누르기
search_box.send_keys(Keys.ENTER)
driver.find_element_by_xpath("""//*[@id="dimmedLayer"]""").click()

소정3 = crawl_over11(1, 16, 2, 6, 4)
연서3 = crawl_over11(1, 16, 2, 6, 2)
연동3 = crawl_over11(1, 16, 2, 6, 3)
연기3 = crawl_over11(1, 16, 2, 6, 4)
장군3 = crawl_over11(1, 16, 2, 6, 5)
금남3 = crawl_over11(1, 16, 2, 6, 4)
고운3 = crawl_over11(1, 16, 2, 6, 3)
아름3 = crawl_over11(1, 16, 2, 6, 3)
도담3 = crawl_over11(1, 16, 2, 6, 3)
종촌3 = crawl_over11(1, 16, 2, 6, 3)
다정3 = crawl_over11(1, 16, 2, 6, 3)
새롬3 = crawl_over11(1, 16, 2, 6, 3)
한솔3 = crawl_over11(1, 16, 2, 6, 3)
대평3 = crawl_over11(1, 16, 2, 6, 3)
보람3 = crawl_over11(1, 16, 2, 6, 4)
소담3 = crawl_over11(1, 16, 2, 6, 3)


# ### 4th function

# In[ ]:


find = input('검색할 정보를 입력하세요: ')

driver = webdriver.Chrome('/Users/yoonjeonghyeon/Desktop/python/chromedriver')
driver.get("https://map.kakao.com")
driver.implicitly_wait(5)

# 검색창에 검색어 입력하기
search_box = driver.find_element_by_css_selector("#search\.keyword\.query")
search_box.send_keys(find)

time.sleep(3)

# 검색버튼 누르기
search_box.send_keys(Keys.ENTER)
driver.find_element_by_xpath("""//*[@id="dimmedLayer"]""").click()

소정4 = under5(1, 15, 1, 1, 5)
전의2 = under5(1, 16, 2, 2, 1)
전동3 = under5(1, 16, 2, 5, 2)
연서4 = under5(1, 16, 1, 1, 3)
조치원3 = under5(1, 16, 2, 5, 2)
연동4 = under5(1, 16, 2, 2, 4)
부강3 = under5(1, 16, 1, 1, 2)
연기4 = under5(1, 16, 2, 4, 5)
장군4 = under5(1, 3, 1, 1, 7)
금남4 = under5(1, 16, 2, 2, 5)
고운4 = under5(1, 16, 2, 5, 5)
아름4 = under5(1, 16, 2, 2, 3)
종촌4 = under5(1, 16, 2, 2, 3)
한솔4 = under5(1, 16, 2, 2, 3)
대평4 = under5(1, 16, 2, 5, 3)
보람4 = under5(1, 16, 1, 1, 3)
소담4 = under5(1, 16, 1, 1, 3)


# #### 5th function

# In[ ]:


find = input('검색할 정보를 입력하세요: ')

driver = webdriver.Chrome('/Users/yoonjeonghyeon/Desktop/python/chromedriver')
driver.get("https://map.kakao.com")
driver.implicitly_wait(5)

# 검색창에 검색어 입력하기
search_box = driver.find_element_by_css_selector("#search\.keyword\.query")
search_box.send_keys(find)

time.sleep(3)

# 검색버튼 누르기
search_box.send_keys(Keys.ENTER)
driver.find_element_by_xpath("""//*[@id="dimmedLayer"]""").click()

소정5 = last(1, 15, 7)
전의3 = last(1, 1, 1)
전동4 = last(1, 1, 2)
연서5 = last(1, 14, 4)
조치원4 = last(1, 3, 2)
연동4 = last(1, 3, 5)
부강4 = last(1, 15, 2)
연기5 = last(1, 15, 6)
장군5 = last(1, 3, 5)
금남5 = last(1, 15, 6)
고운5 = last(1, 3, 5)
아름5 = last(1, 16, 5)
도담5 = last(1, 10, 5)
종촌5 = last(1, 14, 5)
다정5 = last(1, 16, 5)
새롬5 = last(1, 16, 5)
한솔5 = last(1, 7, 5)
대평5 = last(1, 10, 5)
보람5 = last(1, 6, 6)
소담5 = last(1, 16, 5)


# ---
# ### 데이터 합치기

# In[ ]:


소정 = 소정1 + 소정2 + 소정3 + 소정4 + 소정5
전의 = 전의1 + 전의2 + 전의3
전동 = 전의1 + 전의2 + 전의3 + 전의4
연서 = 연서1 + 연서2 + 연서3 + 연서4 + 연서5
조치원 = 조치원1 + 조치원2 + 조치원3 + 조치원4
연동 = 연동1 + 연동2 + 연동3 + 연동4
부강 = 부강1 + 부강2 + 부강3 + 부강4
연기 = 연기1 + 연기2 + 연기3 + 연기4 + 연기5
장군 = 장군1 + 장군2 + 장군3 + 장군4 + 장군5
금남 = 금남1 + 금남2 + 금남3 + 금남4 + 금남5
고운 = 고운1 + 고운2 + 고운3 + 고운4 + 고운5
아름 = 아름1 + 아름2 + 아름3 + 아름4 + 아름5
도담 = 도담1 + 도담2 + 도담3 + 도담4 + 도담5
종촌 = 종촌1 + 종촌2 + 종촌3 + 종촌4 + 종촌5
다정 = 다정1 + 다정2 + 다정3 + 다정4 + 다정5
새롬 = 새롬1 + 새롬2 + 새롬3 + 새롬4 + 새롬5
한솔 = 한솔1 + 한솔2 + 한솔3 + 한솔4 + 한솔5
대평 = 대평1 + 대평2 + 대평3 + 대평4 + 대평5
보람 = 보람1 + 보람2 + 보람3 + 보람4 + 보람5
소담 = 소담1 + 소담2 + 소담3 + 소담4 + 소담5


# ---
# ### 이름 / 주소 분리 후 df로 변환,  csv로 저장

# In[ ]:


# 소정면 데이터
name = []
address = []

for i in range(len(소정)):
    if i % 2 == 0:
        name.append(소정[i])
    else:
        address.append(소정[i])
        
df소정 = pd.DataFrame(columns = ['name', 'address'])
    
df소정['name'] = name
df소정['address'] = address

df소정.to_csv("sojeong3.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 전의면 데이터
name = []
address = []

for i in range(len(전의)):
    if i % 2 == 0:
        name.append(전의[i])
    else:
        address.append(전의[i])
        
df전의 = pd.DataFrame(columns = ['name', 'address'])
    
df전의['name'] = name
df전의['address'] = address

df전의.to_csv("jeonui3.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 전동면 데이터
name = []
address = []

for i in range(len(전동)):
    if i % 2 == 0:
        name.append(전동[i])
    else:
        address.append(전동[i])
        
df전동 = pd.DataFrame(columns = ['name', 'address'])
    
df전동['name'] = name
df전동['address'] = address

df전동.to_csv("jeondong3.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 연서면 데이터
name = []
address = []

for i in range(len(연서)):
    if i % 2 == 0:
        name.append(연서[i])
    else:
        address.append(연서[i])
        
df연서 = pd.DataFrame(columns = ['name', 'address'])
    
df연서['name'] = name
df연서['address'] = address

df연서.to_csv("yeonseo3.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 조치원읍 데이터
name = []
address = []

for i in range(len(조치원)):
    if i % 2 == 0:
        name.append(조치원[i])
    else:
        address.append(조치원[i])
        
df조치원 = pd.DataFrame(columns = ['name', 'address'])
    
df조치원['name'] = name
df조치원['address'] = address

df조치원.to_csv("jochiwon3.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 연동면 데이터
name = []
address = []

for i in range(len(연동)):
    if i % 2 == 0:
        name.append(연동[i])
    else:
        address.append(연동[i])
        
df연동 = pd.DataFrame(columns = ['name', 'address'])
    
df연동['name'] = name
df연동['address'] = address

df연동.to_csv("yeondong3.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 부강면 데이터
name = []
address = []

for i in range(len(부강)):
    if i % 2 == 0:
        name.append(부강[i])
    else:
        address.append(부강[i])
        
df부강 = pd.DataFrame(columns = ['name', 'address'])
    
df부강['name'] = name
df부강['address'] = address

df부강.to_csv("bugang3.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 연기면 데이터
name = []
address = []

for i in range(len(연기)):
    if i % 2 == 0:
        name.append(연기[i])
    else:
        address.append(연기[i])
        
df연기 = pd.DataFrame(columns = ['name', 'address'])
    
df연기['name'] = name
df연기['address'] = address

df연기.to_csv("yeongi3.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 장군면 데이터
name = []
address = []

for i in range(len(장군)):
    if i % 2 == 0:
        name.append(장군[i])
    else:
        address.append(장군[i])
        
df장군 = pd.DataFrame(columns = ['name', 'address'])
    
df장군['name'] = name
df장군['address'] = address

df장군.to_csv("janggoon3.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 금남면 데이터
name = []
address = []

for i in range(len(금남)):
    if i % 2 == 0:
        name.append(금남[i])
    else:
        address.append(금남[i])
        
df금남 = pd.DataFrame(columns = ['name', 'address'])
    
df금남['name'] = name
df금남['address'] = address

df금남.to_csv("geumnam3.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 고운동 데이터
name = []
address = []

for i in range(len(고운)):
    if i % 2 == 0:
        name.append(고운[i])
    else:
        address.append(고운[i])
        
df고운 = pd.DataFrame(columns = ['name', 'address'])
    
df고운['name'] = name
df고운['address'] = address

df고운.to_csv("goun3.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 아름동 데이터
name = []
address = []

for i in range(len(아름)):
    if i % 2 == 0:
        name.append(아름[i])
    else:
        address.append(아름[i])
        
df아름 = pd.DataFrame(columns = ['name', 'address'])
    
df아름['name'] = name
df아름['address'] = address

df아름.to_csv("areum3.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 도담동 데이터
name = []
address = []

for i in range(len(도담)):
    if i % 2 == 0:
        name.append(도담[i])
    else:
        address.append(도담[i])
        
df도담 = pd.DataFrame(columns = ['name', 'address'])
    
df도담['name'] = name
df도담['address'] = address

df도담.to_csv("dodam3.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 종촌동 데이터
name = []
address = []

for i in range(len(종촌)):
    if i % 2 == 0:
        name.append(종촌[i])
    else:
        address.append(종촌[i])
        
df종촌 = pd.DataFrame(columns = ['name', 'address'])
    
df종촌['name'] = name
df종촌['address'] = address

df종촌.to_csv("jongchon3.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 다정동 데이터
name = []
address = []

for i in range(len(다정)):
    if i % 2 == 0:
        name.append(다정[i])
    else:
        address.append(다정[i])
        
df다정 = pd.DataFrame(columns = ['name', 'address'])
    
df다정['name'] = name
df다정['address'] = address

df다정.to_csv("dajeong3.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 새롬동 데이터
name = []
address = []

for i in range(len(새롬)):
    if i % 2 == 0:
        name.append(새롬[i])
    else:
        address.append(새롬[i])
        
df새롬 = pd.DataFrame(columns = ['name', 'address'])
    
df새롬['name'] = name
df새롬['address'] = address

df새롬.to_csv("saerom3.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 한솔동 데이터
name = []
address = []

for i in range(len(한솔)):
    if i % 2 == 0:
        name.append(한솔[i])
    else:
        address.append(한솔[i])
        
df한솔 = pd.DataFrame(columns = ['name', 'address'])
    
df한솔['name'] = name
df한솔['address'] = address

df한솔.to_csv("hansol3.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 대평동 데이터
name = []
address = []

for i in range(len(대평)):
    if i % 2 == 0:
        name.append(대평[i])
    else:
        address.append(대평[i])
        
df대평 = pd.DataFrame(columns = ['name', 'address'])
    
df대평['name'] = name
df대평['address'] = address

df대평.to_csv("daepyeong3.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 보람동 데이터
name = []
address = []

for i in range(len(보람)):
    if i % 2 == 0:
        name.append(보람[i])
    else:
        address.append(보람[i])
        
df보람 = pd.DataFrame(columns = ['name', 'address'])
    
df보람['name'] = name
df보람['address'] = address

df보람.to_csv("boram3.csv", mode = 'w', encoding = 'utf-8')


# In[ ]:


# 소담동 데이터
name = []
address = []

for i in range(len(소담)):
    if i % 2 == 0:
        name.append(소담[i])
    else:
        address.append(소담[i])
        
df소담 = pd.DataFrame(columns = ['name', 'address'])
    
df소담['name'] = name
df소담['address'] = address

df소담.to_csv("sojeong3.csv", mode = 'w', encoding = 'utf-8')


# ---
# ### 데이터 가공

# In[1]:


import pandas as pd
import numpy as np

print("pandas version: ", pd.__version__)


# In[2]:


data1 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling3/sojeong3.csv', index_col = 0)
data2 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling3/jeonui3.csv', index_col = 0)
data3 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling3/jeondong3.csv', index_col = 0)
data4 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling3/yeonseo3.csv', index_col = 0)
data5 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling3/jochiwon3.csv', index_col = 0)
data6 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling3/yeondong3.csv', index_col = 0)
data7 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling3/bugang3.csv', index_col = 0)
data8 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling3/yeongi3.csv', index_col = 0)
data9 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling3/janggoon3.csv', index_col = 0)
data10 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling3/geumnam3.csv', index_col = 0)
data11 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling3/goun3.csv', index_col = 0)
data12 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling3/areum3.csv', index_col = 0)
data13 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling3/dodam3.csv', index_col = 0)
data14 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling3/jongchon3.csv', index_col = 0)
data15 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling3/dajeong3.csv', index_col = 0)
data16 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling3/saerom3.csv', index_col = 0)
data17 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling3/hansol3.csv', index_col = 0)
data18 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling3/daepyeong3.csv', index_col = 0)
data19 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling3/boram3.csv', index_col = 0)
data20 = pd.read_csv('/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Crawling3/sodam3.csv', index_col = 0)


# In[3]:


# 앞에서 크롤링한 데이터 다 합치기
df = pd.concat([data1, data2, data3, data4,
                     data5, data6, data7, data8,
                     data9, data10, data11, data12,
                     data13, data14, data15, data16,
                     data17, data18, data19, data20], ignore_index = True)


# In[6]:


# 중복되는 주소 drop
df2 = df.drop_duplicates(['address'])
# 세종시가 아닌 곳은 drop
cond1 = df2['address'].str.contains('세종특별자치시')
df3 = df2[cond1]
# 병원이 아닌 곳은 drop
cond2 = ~ df3['name'].str.contains('동물|CU|GS|365|컴퓨터|공중전화|하나은행|버거킹|쏘카존|르뺑')
df4 = df3[cond2]
df4.to_csv('hospital_utf8.csv', mode = 'w', encoding = 'utf-8')


# ---
# # 4. 파출소 크롤링

# In[ ]:


# 검색어 설정
find = input('검색할 정보를 입력하세요: ')

# 크롬 실행
driver = webdriver.Chrome('/Users/yoonjeonghyeon/Desktop/python/chromedriver')
driver.get("https://map.kakao.com")
driver.implicitly_wait(5)

# 검색창에 검색어 입력하기
search_box = driver.find_element_by_css_selector("#search\.keyword\.query")
search_box.send_keys(find)

time.sleep(3)

# 검색버튼 누르기
search_box.send_keys(Keys.ENTER)
driver.find_element_by_xpath("""//*[@id="dimmedLayer"]""").click()

# 페이지 더보기 먼저 눌러야 할 경우
# driver.find_element_by_xpath("""//*[@id="info.search.place.more"]""").click()
# time.sleep(3)

파출소1 = crawl_1st(1, 16)
파출소2 = under5(1, 16, 2, 4, 1)
파출소3 = last(1, 3, 1)


# ---
# ### 데이터 합치기

# In[ ]:


파출소 = 파출소1 + 파출소2 + 파출소3


# ---
# ### 이름 / 주소 분리 후 df로 변환,  csv로 저장

# In[ ]:


name = []
address = []

for i in range(len(파출소)):
    if i % 2 == 0:
        name.append(파출소[i])
    else:
        address.append(파출소[i])
        
df파출소 = pd.DataFrame(columns = ['name', 'address'])
    
df파출소['name'] = name
df파출소['address'] = address

df파출소.to_csv("policeoffice.csv", mode = 'w', encoding = 'utf-8')


# ---
# ## 데이터 가공

# In[10]:


import numpy as np
import pandas as pd


# In[11]:


data = pd.read_csv("/Users/yoonjeonghyeon/Desktop/python/KUBIG/Sejong/Result/policeoffice.csv", index_col = 0)


# In[ ]:


# 세종시가 아닌 곳은 drop
condition = data['address'].str.contains('세종특별자치시')
data2 = data[condition]
data2.to_csv("policeoffice_utf-8", mode = 'w', encoding = 'utf-8')

