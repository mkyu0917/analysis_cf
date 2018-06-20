from bs4 import BeautifulSoup

html= '''<td class="title"><div class="tit3">
        <a href="/movie/bi/mi/basic.nhn?code=154285"
         title="쥬라기 월드: 폴른 킹덤">쥬라기 월드: 폴른 킹덤</a></div></td>
      '''



#1.tag조회
def ex1():
    bs=BeautifulSoup(html,'html.parser')
    print(bs)

    tag = bs.td #bs에 있는 td태그 가져오기
    print(tag)
    print()

    tag = bs.a# a 태그 가져오기
    print(tag)
    print(tag.name)

def ex2():
    bs = BeautifulSoup(html, 'html.parser')

    tag = bs.td
    print(tag['class']) #클래스 속성가져외긔

    tag = bs.div
    #에러
    #print(tag['id']
    print(tag.attrs)

def ex3():
    bs = BeautifulSoup(html, 'html.parser')
    tag=bs.find('td',attrs={'class':'title'}) #클래스가 title인놈들 찾기
    print(tag)

    tag=bs.find(attrs={'class' : 'tit3'})
    print(tag)

if __name__ == '__main__':
    #ex1()
    #ex2()
    ex3()