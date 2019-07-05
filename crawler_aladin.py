
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import codecs
from datetime import datetime

d = datetime.today()

file_path = "D:/py1530/알라딘 베스트셀러(1~400위)_%d_%d_%d.txt" % (d.year, d.month, d.day)

try:
    f = codecs.open(file_path, mode="w", encoding="utf-8")
except:
    print("디렉토리 경로를 찾을 수 없습니다.")

driver = webdriver.Chrome('D:/py1530/chromedriver.exe')
driver.get('https://www.aladin.co.kr')

driver.find_element_by_xpath('//*[@id="re_mallmenu"]/ul/li[3]/div/a/img').click()

time.sleep(3)

rank = 1
for x in range(2, 10):
    rank_tap = '//*[@id="newbg_body"]/div[3]/ul/li[%d]' % x
    driver.find_element_by_xpath(rank_tap).click()
    time.sleep(1)

    source = driver.page_source
    html_s = BeautifulSoup(source, "html.parser")
    
    best_seller_div = html_s.find_all("div", class_="ss_book_box")
    
    for best_seller in best_seller_div:
    
        first_book = best_seller.find_all("li")    
        
        if first_book[0].text[0] == "[":
            book_title = first_book[1].text
            book_author = first_book[2].text
            book_price = first_book[3].text
        else:
            book_title = first_book[0].text
            book_author = first_book[1].text
            book_price = first_book[2].text
        
        info = book_author.split("|")
        f.write("순위: %d위\r\n" % rank)
        f.write("책 제목: " + book_title + "\r\n")
        f.write("저자: " + info[0].strip() + "\r\n")
        f.write("출판사: " + info[1].strip() + "\r\n")
        f.write("출판일: " + info[2].strip() + "\r\n")
        f.write("가격: " + book_price.split(",  ")[0] + "\r\n")
        f.write("-" * 50 + "\r\n")
        rank += 1

f.close()
print("크롤링 완료!")










