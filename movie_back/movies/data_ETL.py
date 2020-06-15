import requests
import json
import csv
import pandas as pd
from pandas.io.json import json_normalize

# ========================== 데이터 Extraction ==========================

Servicekey = '04SY8J71WZ1Q1761IC2I'
base_url = 'http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json2.jsp?collection=kmdb_new2'
url = base_url + f'&ServiceKey={Servicekey}&listCount=1000&startCount=50'

response = requests.get(url).json()
data = json.dumps(response)

# ** 1년 단위로 영화 정보 json 파일로 저장 **
for year in range(1939, 2021):

    print(year-1938) # iteration 확인 위한 프린트

    year = str(year)
    urltemplate = base_url + f'&createDts={year}' + f'&ServiceKey={Servicekey}&listCount=1000&startCount=50'
    response = requests.get(urltemplate).json() # type : dict
    # print(response)
    with open(f'final_pjt/movie_back/movies/fixtures/kmdb_data_{year}.json', 'w', encoding='utf-8') as outfile:
         json.dump(response, outfile, indent=2)


# ========================== 데이터 Cleansing ==========================
# ** docid 값과 해당 객체를 딕셔너리 형태로 만들어 중복을 제거함 **
movies = dict()
columns = ['title','titleEng','nation','runtime','rating','genre','repRlsDate','keywords','posters','stlls']

for year in range(1939, 2014):
    year = str(year)
    with open(f'final_pjt/movie_back/movies/fixtures/before_data_cleansing/kmdb_data_{year}.json', 'r', encoding='utf-8') as f:
        read = json.load(f)
        data = read['Data'][0]
        results = data['Result']
        
        for result in results : 
            movie = dict()
            movie['model'] = 'movies.Movie'
            if result['DOCID'] not in movies.keys():
                movie['pk'] = result['DOCID'] # pk 값이 integer여야 하나봄
                if result['runtime'] != '' and result['posters'] != '':
                    fields = dict()
                    for colname in columns :
                        fields[colname] = result[colname]
                    fields['directorNm'] = result['directors']['director'][0]["directorNm"]
                    fields["directorEnNm"] = result['directors']['director'][0]["directorEnNm"]
                    fields['plotLang'] = result['plots']['plot'][0]['plotLang']
                    fields['plotText'] = result['plots']['plot'][0]['plotText']
                    fields['vodUrl'] = result['vods']['vod'][0]['vodUrl']
                    movie['fields'] = fields
                    movies[movie['pk']] = movie
        
        print(len(movies)) # 1622
        info = list(movies.values())

        with open('final_pjt/movie_back/movies/fixtures/important_data.json', 'w', encoding='utf-8') as outfile:
            json.dump(info, outfile, indent=2, ensure_ascii=False)


    # ========================== 데이터 Transform ==========================
    # 모델에서 숫자 형태로 받고싶은 데이터에 대해 형 변환 진행
    # print(type(result_df['runtime'][0])) # type : str
    # print(type(result_df['audiAcc'][0])) # type : str
    
    # runtime은 정제된 값이기 때문에 형 변환이 한번에 가능함
    # result_df = result_df.astype({'runtime': 'int'})
    # print(result_df['runtime'].dtypes) # int64

    # audiAcc은 알 수 없는 값이 존재하여, 에러 처리가 필요함 - NaN으로 표시
    # result_df['audiAcc'] = pd.to_numeric(result_df['audiAcc'], errors='coerce')
    # print(result_df['audiAcc'].dtypes) # type : float64

    # print(result_df.dtypes)
    # print(result_df) # [1622 rows x 14 columns]

    # df = result_df.to_csv('final_pjt/movie_back/movies/fixtures/data_to_use2.csv')

    

    # ========================== 데이터 test ==========================
    # runtime 속성의 min, max 값을 알아보자
    # print(min(result_df['runtime'])) # 최소 3분짜리 영화..!
    # print(max(result_df['runtime'])) # 최대 576분짜리 영화......!


    # ++ 분포도 알 수 있을까?
    # 코렙에서 아래와 같은 코드로 돌려옴
    # https://colab.research.google.com/drive/10U2NdXogkYFwo7kNKrXOUuU_vY-EraY1?usp=sharing