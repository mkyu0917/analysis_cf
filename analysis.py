import pandas as pd
import matplotlib.pyplot as plt


#pelicana

pelicana_table=pd.DataFrame.from_csv('__result__/crawling/pelicana_table.csv',
                      encoding ='utf-8',
                      index_col=0, # 인덱스 컬럼은 0
                      header=0).fillna('') # fillna = 비어있는 것들은()안에 것으로 채워라



pelicana_table = pelicana_table[pelicana_table.sido != ''] #sido가 비어있지 않으면 row를 가져옴
pelicana_table = pelicana_table[pelicana_table.gungu != '']

# 'SIDO GUNGU' 별 매장수
pelicana=pelicana_table.apply(lambda r:str(r['sido'])+' '+str(r['gungu']),axis=1).value_counts() # 람다가 파라미터로 들어가있음 axis = 1<-컬럼기준으로 데이터를 줌 serise1

# print(df.value_counts())
# print(pelicana)
# s2=s1.value_counts()# 중복되는 데이터를 하나의 테이블로 뽑음 serise2
# print(s2)

#kyuchon
kyuchon_table=pd.DataFrame.from_csv('__result__/crawling/kyuchon_table.csv',
                      encoding ='utf-8',
                      index_col=0, # 인덱스 컬럼은 0
                      header=0).fillna('') # fillna = 비어있는 것들은()안에 것으로 채워라



kyuchon_table = kyuchon_table[kyuchon_table.sido != ''] #sido가 비어있지 않으면 row를 가져옴
kyuchon_table = kyuchon_table[kyuchon_table.gungu != '']

# 'SIDO GUNGU' 별 매장수
kyuchon=kyuchon_table.apply(lambda r:str(r['sido'])+' '+str(r['gungu']),axis=1).value_counts() # 람다가 파라미터로 들어가있음 axis = 1<-컬럼기준으로 데이터를 줌 serise1



#goobne
goobne_table=pd.DataFrame.from_csv('__result__/crawling/goobne_table.csv',
                      encoding ='utf-8',
                      index_col=0, # 인덱스 컬럼은 0
                      header=0).fillna('') # fillna = 비어있는 것들은()안에 것으로 채워라



goobne_table = goobne_table[goobne_table.sido != ''] #sido가 비어있지 않으면 row를 가져옴
goobne_table = goobne_table[goobne_table.gungu != '']

# 'SIDO GUNGU' 별 매장수
goobne=goobne_table.apply(lambda r:str(r['sido'])+' '+str(r['gungu']),axis=1).value_counts() # 람다가 파라미터로 들어가있음, axis = 1<-컬럼기준으로 데이터를 줌 serise1


#nene
nene_table=pd.DataFrame.from_csv('__result__/crawling/nene_table.csv',
                      encoding ='utf-8',
                      index_col=0, # 인덱스 컬럼은 0
                      header=0).fillna(0) # fillna = 비어있는 것들은()안에 것으로 채워라



nene_table = nene_table[nene_table.sido != ''] #sido가 비어있지 않으면 row를 가져옴
nene_table = nene_table[nene_table.gungu != '']

# 'SIDO GUNGU' 별 매장수
nene=nene_table.apply(lambda r:str(r['sido'])+' '+str(r['gungu']),axis=1).value_counts() # 람다가 파라미터로 들어가있음, axis = 1<-컬럼기준으로 데이터를 줌 serise1






chicken_table=pd.DataFrame({'pelicana':pelicana, 'nene': nene, 'kyochon': kyuchon,'goobne':goobne })
chicken_table = chicken_table.drop(chicken_table[chicken_table.index == '00 18'].index) #쓸때없는 데이터 drop
chicken_table = chicken_table.drop(chicken_table[chicken_table.index == '테스트 테스트구'].index)
#print(chicken_table)
chicken_sum_table=chicken_table.sum(axis=0)
#print(chicken_sum_table)
#print(chicken_sum_table.lioc[:5])

plt.figure()
chicken_sum_table.plot(kind='bar')
plt.show()