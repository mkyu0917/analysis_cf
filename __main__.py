from datetime import datetime
import sys
import time
import urllib
from itertools import count
from bs4 import BeautifulSoup
import pandas as pd
import collection.crawler as cw
from collection.data_dict import sido_dict, gungu_dict #data dict에서 불러옴
import xml.etree.ElementTree as et #xml엘레먼트 트리
from selenium import webdriver

RESULT_DIRECTORY = '__result__/crawling'

def crawling_pelicana():
    results = []
    for page in count(start=1): #import
        url='http://www.pelicana.co.kr/store/stroe_search.html?page=%d&branch_name=&gu=&si='% (page)
        print(page)
        html=cw.crawling(url=url)

        bs=BeautifulSoup(html,'html.parser') # html 파서
        tag_table=bs.find('table', attrs={'class':'table mt20'}) #테이블 속성이 table mt20ㅣ인거 찾으셍
        print(tag_table)
        tag_tbody= tag_table.find('tbody')
        tags_tr= tag_tbody.findAll('tr')
        print(tags_tr)
        #끝 검출
        if len(tags_tr) == 0:
            break


        for tag_tr in tags_tr:
            strings=list(tag_tr.strings) #리스트로 변경해서 개행과 탭,스트링을 가진 리스트로출력
            print(strings)
            name = strings[1]   #리스트에서 지점이름인덱스
            address = strings[3]#리스트에서 주소인덱스
            #print(address.split())#주소값을 분리해서 리스트에 넣음
            sidogu = address.split()[:2] #슬라이싱으로 처음부터 2개만 뽑음

            results.append((name, address) + tuple(sidogu)) # 이름 주소 시도구를 넣은 튜플을 생성, 데이터 변경을 방지

    #store
    #print(results)
    table = pd.DataFrame(results, columns=['name', 'address', 'sido','gungu'])

    table['sido'] = table.sido.apply(lambda v: sido_dict.get(v,v)) # v에 sido값을 주고 그 값을 리턴값으로 변경, 다르지 아느면 그냥 내비둠
    table['gungu'] = table.gungu.apply(lambda v: gungu_dict.get(v, v))

    table.to_csv(
        '{0}/pelicana_table.csv'.format(RESULT_DIRECTORY),
        encoding='utf-8',
        mode='w',
        index=True)

def proc_nene(xml): #xml을 받음
    root=et.fromstring(xml)

    results=[]
    #elements_item=root.findAll('item') #이름이 아이템인 엘레먼트를 찾아줌
    for el in root.findall('item'): # root.findAll을 바로넣어도됨
        name = el.findtext('aname1')#
        sido = el.findtext('aname2')
        gungu = el.findtext('aname3')
        address = el.findtext('aname5')

        results.append((name, address, sido, gungu,))
    print(results)
    return results #값을 크롤링 함수 호출한 곳으로 넘겨줌

def store_nene(data): #데이터 저장
    table = pd.DataFrame(data, columns=['name', 'address', 'sido', 'gungu'])

    table['sido'] = table.sido.apply(lambda v: sido_dict.get(v, v))  # v에 sido값을 주고 그 값을 리턴값으로 변경, 다르지 아느면 그냥 내비둠
    table['gungu'] = table.gungu.apply(lambda v: gungu_dict.get(v, v))

    table.to_csv(
        '{0}/nene_table.csv'.format(RESULT_DIRECTORY),
        encoding='utf-8',
        mode='w',
        index=True)

# kyuchon chicken

def crawling_kyuchon():
    results=[]
    for sido1 in range(1,18):
        for sido2 in count(start=1):
                url = 'http://www.kyochon.com/shop/domestic.asp?sido1=%d&sido2=%d&txtsearch=' % (sido1, sido2)
                html = cw.crawling(url=url)
                if html == None:
                    break
                bs = BeautifulSoup(html, 'html.parser')  # html 파서
                tag_div = bs.find('div', attrs={'class':'shopSchList'})  # 찾으려는 태그 속성이 ~~인거 찾으
                # tag_ul = tag_div.find('ul')                                 # 순차적으로 들어가야됨 한번에 뽑으면 파싱이상
                tag_lis = tag_div.findAll('li')



                for tag_li in tag_lis:
                    strings = list(tag_li.strings)  # 리스트로 변경해서 개행과 탭,스트링을 가진 리스트로출력

                    try:
                        name = strings[3]  # 리스트에서 지점이름인덱스
                        address = strings[5].strip()  # 리스트에서 주소인덱스
                        #print(address.split())#주소값을 분리해서 리스트에 넣음
                        sidogu = address.split()[:2]  # 슬라이싱으로 처음부터 2개만 뽑음
                        results.append((name, address) + tuple(sidogu))
                #print(results)
                    except Exception as e:
                        print('%s : %s' % (e, datetime.now()), file=sys.stderr)

    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gungu'])

    table['sido'] = table.sido.apply(lambda v: sido_dict.get(v, v))  # v에 sido값을 주고 그 값을 리턴값으로 변경, 다르지 아느면 그냥 내비둠
    table['gungu'] = table.gungu.apply(lambda v: gungu_dict.get(v, v))

    table.to_csv(
        '{0}/kyuchon_table.csv'.format(RESULT_DIRECTORY), #csv로 디렉토리에 저장
        encoding='utf-8',
        mode='w',
        index=True)


            #name = strings[1]   #리스트에서 지점이름인덱스
            #address = strings[3]#리스트에서 주소인덱스
            #print(address.split())#주소값을 분리해서 리스트에 넣음
            #sidogu = address.split()[:2] #슬라이싱으로 처음부터 2개만 뽑음

            #results.append((name, address) + tuple(sidogu)) # 이름 주소 시도구를 넣은 튜플을 생성, 데이터 변경을 방지



def crawling_goobne():
    results=[]
    url = 'http://www.goobne.co.kr/store/search_store.jsp'
    #첫 페이지로딩
    wd = webdriver.Chrome('C:/Users/minkyu/Desktop/코딩프로그램/chromedriver.exe') #크롬드라이버 실행
    wd.get(url) #url get방식으로 받아오기 (그냥 있는 그대로 받아오기 ) post는 수정

    time.sleep(5) #5초 대기

    for page in count(start=1): # count(start=1) 처음부터 끝까지 돌음
        script = 'store.getList(%d)' % page #페이지 값이 변경되면서
        print('%s : success for script execute [%s]' % (datetime.now(),script))
        wd.execute_script(script) #스크립트 실행
        time.sleep(5) # 5초 대기

        # 실행결과 HTML(rendering 된 html ) 가져오기
        html = wd.page_source
        #print(html)

        #parsing with bs4 (필요한데이터 뽑아내기?)
        bs = BeautifulSoup(html,'html.parser') #html파서 호출
        tag_tbody=bs.find('tbody', attrs={'id': 'store_list'}) #tbody라는 태그의 속성이 id고 store_list인것
        tags_tr=tag_tbody.findAll('tr') #tbody안에 모든 tr을 가져옴
        #마지막 검출
        if tags_tr[0].get('class') is None: #받아오는 tags_tr[0]의 클래스가 None이면 멈춤
            break

        for tag_tr in tags_tr:
            strings = list(tag_tr.strings) #태그안에 있는 스트링 모두를 리스트로 가져오기4
            name =strings[1]#지점을 담고
            address= strings[6]#주소를 담고
            sidogu = address.split(' ')[0:2]#주소 스플릿해서 시도를 담고

            results.append((name,address)+tuple(sidogu))
    print(results)

    #store
    table=pd.DataFrame(results, columns=['name', 'address','sido','gungu'])# 데이터프레임생성(테이블) ,
    table['sido'] = table.sido.apply(lambda v: sido_dict.get(v,v))# sido라는 딕셔너리에 없으면 그냥 내값을 리턴해라
    table['gungu'] = table.gungu.apply(lambda v: gungu_dict.get(v, v))

    table.to_csv(
        '{0}/goobne_table.csv'.format(RESULT_DIRECTORY),  # csv로 디렉토리에 저장
        encoding='utf-8',
        mode='w',
        index=True)



if __name__=='__main__':


    #crawling_pelicana() #처리, 저장 싹다함
    
    #nene
    # cw.crawling(url='http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'
    #             % (urllib.parse.quote("전체"), urllib.parse.quote("전체")), #lib로 utf-8인코딩해서 넣어줘야 안전
    #             proc=proc_nene,
    #             store=store_nene)
    
    

    #crawling_kyuchon()


    crawling_goobne()
