import pandas as pd



#pelicana
pelicanan_table=pd.DataFrame.from_csv('__result__/crawling/pelicana_table.csv',
                      encoding ='utf-8',
                      index_col=0, # 인덱스 컬럼은 0
                      header=0).fillna('') # fillna = 비어있는 것들은()안에 것으로 채워라



pelicanan_table = pelicanan_table[pelicanan_table.sido != ''] #sido가 비어있지 않으면 row를 가져옴
pelicanan_table = pelicanan_table[pelicanan_table.gungu != '']

# 'SIDO GUNGU' 별 매장수
s1=pelicanan_table.apply(lambda r:str(r['sido'])+' '+str(r['gungu']),axis=1) # 람다가 파라미터로 들어가있음 axis = 1<-컬럼기준으로 데이터를 줌 serise1
#print(df.value_counts())
#print(df)
s2=s1.value_counts()# 중복되는 데이터를 하나의 테이블로 뽑음 serise2
print(s2)
#kyuchon




#goobne