from itertools import count
from bs4 import BeautifulSoup

import collection.crawler as cw

def crawling_pelicana():
    results = []
    for page in count(start=1): #import
        url='http://www.pelicana.co.kr/store/stroe_search.html?page=%d&branch_name=&gu=&si= '% (page)
        html=cw.crawling(url=url)

        bs=BeautifulSoup(html,'html.parser') # html 파서
        tag_table=bs.find('table', attrs={'class':'table mt20'}) #테이블 속성이 table mt20ㅣ인거 찾으셍
        tag_tbody= tag_table.find('tbody')
        tags_tr= tag_tbody.findAll('tr')

        #끝 검출
        if len(tags_tr) == 0:
            break

        for tag_tr in tags_tr:
            strings=list(tag_tr.strings) #리스트로 변경해서 개행과 탭,스트링을 가진 리스트로출력

            name = strings[1]   #리스트에서 지점이름인덱스
            address = strings[3]#리스트에서 주소인덱스
            #print(address.split())#주소값을 분리해서 리스트에 넣음
            sidogu = address.split()[:2] #슬라이싱으로 처음부터 2개만 뽑음

            results.append((name, address) + tuple(sidogu)) # 이름 주소 시도구를 넣은 튜플을 생성, 데이터 변경을 방지
            print(results)
    #sore
    print(results)

if __name__=='__main__':

    #pelicana
    crawling_pelicana() #처리, 저장 싹다함
