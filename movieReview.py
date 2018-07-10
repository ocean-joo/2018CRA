# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 13:19:50 2018

@author: hyeOn
"""
 
def movieReview(movie_name, maxPage=10) :
    
    import urllib 

    client_ID = 'iPiLUtbmWB3Ml5f8Ay3A'
    client_secret = 'WH0MRvrfmm'
    encoded_movie_name = urllib.parse.quote(movie_name)
    
    query = "https://openapi.naver.com/v1/search/movie.json"
    option = "?display=1&yearfrom=2000&yearto=2018&query="
    
    url_query = query + option + encoded_movie_name
    
    request = urllib.request.Request(url_query)
    request.add_header("X-Naver-Client-Id",client_ID)
    request.add_header("X-Naver-Client-Secret",client_secret)
    
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    
    if rescode != 200 :
        print("Error Code : " + str(rescode))
    
    import json
    item = json.loads(response.read())
    url = item['items'][0]['link']
    #rating = item['items'][0]['userRating']

    str2 = url.split('code=')[1]

    str1 = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code='
    str3 = '&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false'

    import requests
    from bs4 import BeautifulSoup

    result = tuple()

    for j in range(1,maxPage+1) :
        inputStr = str1 + str2 + str3 + '&page=' + str(j)
        html = requests.get(inputStr).text
        soup = BeautifulSoup(html, 'html.parser')
        
<<<<<<< HEAD
        text_list = (soup.select('body > div > div > div.score_result > ul div.score_reple > p'),
				soup.select("body > div > div > div.score_result > ul div.star_score > em"))
        for i, k in text_list :
            temp[0] = i.text
            temp[0] = temp[0].rstrip()
            if temp[0].startwith("관람객") :
                temp[0] = temp[0].split("관람객")[0]
            temp[1] = k.text
=======
        text_list = soup.select('body > div > div > div.score_result > ul div.score_reple > p')
        
        for i in text_list :
            temp = i.text
            temp = temp.rstrip()
            if temp.startswith("관람객") :
                temp = temp.split('관람객')[1]
>>>>>>> 49b01a4572e11431a58105debf874c9502eb9237
            result.append(temp)
    
    return result

movieReview("강철비")
movieReview("신과 함께")
movieReview("1987")
