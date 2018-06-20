import collection.crawler as cw

#def proc(html): #결과처리함수
#    print("processing..."+html)

#def store(result): #저장하는 함수
#    pass

cw.crawling( #크롤링함수를 돌린값을 결과에 저장하고 출력
    url='http://movie.naver.com/movie/sdb/rank/rmovie.nhn',
    encoding='cp949',
    )

