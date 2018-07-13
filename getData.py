"""
this file is getting other info about movie.
input is movie's name and prdtYear.
i'll return content (form : dict) using api

"""

import ListofMovie as lm
import get_api as api

data = lm.get_movie_list()

dataF = open("/home/hyewon/2018CRA/otherInfo.txt", 'w')
num = 1

for i in data :
    cont = api.get_info(i[0], i[1])
    info = "%d번째 영화이름 : " % num  + cont['movieNm'] + '\n'
    info = info + "영화코드 : " + cont['movieCd'] + '\n' 
    info = info + "개봉연월일 : " + cont['openDt'] + '\n' 
    info = info + "영화 유형 : " + cont['typeNm'] + '\n' 
    info = info + "대표 제작 국가 : " + cont['repNationNm'] + '\n' 
    info = info + "대표 장르 : " + cont['repGenreNm'] + '\n' 
    if cont['directors'] : # 감독정보가 있으면
        info = info + "감독 : " + cont['directors'][0]['peopleNm'] + '\n' 
    else :
        info = info + "감독 : None\n"
    if cont['companys'] : #제작사가 있으면
        info = info + "제작사 : "
        for j in cont['companys'] :
            info = info + j['companyCd'] + "/" + j['companyNm'] + "  "
        info = info + '\n'
    else :
        info = info + "제작사 : None.\n"

    info = info + "\n\n\n"
    dataF.write(info)
    num = num+1

dataF.close()
