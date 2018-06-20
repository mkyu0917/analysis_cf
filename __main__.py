import collection.crawler as cw

result = cw.crawling( #크롤링함수를 돌린값을 결과에 저장하고 출력
    url='http://movie.naver.com/movie/sdb/rank/rmovie.nhn',
    encoding='cp949')

print(result)