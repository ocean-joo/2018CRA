"""
this file is getting other info about movie.
input is movie's name and prdtYear.
i'll return content (form : dict) using api

"""

import ListofMovie as lm
import get_api as api
import csv

data = lm.get_movie_list()

dataF = open("/home/hyewon/2018CRA/otherInfo.csv", 'w', encoding='utf-8', newline='')
f = csv.writer(dataF)

f.writerow(['Movie Name', 'Movie Code', 'Open date', 'Movie Type', 'Nation', 'Genre', 'Directors', 'companys'])


for i in data :
    cont = api.get_info(i[0], i[1])
    info = []
    info.extend([cont['movieNm'], cont['movieCd'], cont['openDt'], cont['typeNm'], cont['repNationNm'], cont['repGenreNm']])
    if cont['directors'] : # 감독정보가 있으면
        info.append(cont['directors'][0]['peopleNm'])
    else :
        info.append('NA')
    if cont['companys'] : #제작사가 있으면
        info.append(cont['companys'][0]['companyCd'] + "/" + cont['companys'][0]['companyNm'])
    else :
        info.append('NA')

    f.writerow(info)

dataF.close()
