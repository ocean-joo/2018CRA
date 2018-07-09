# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 13:19:50 2018

@author: hyeOn
"""
 
def moiveReview(moive_name, maxPage=10) :
    import urllib

    client_ID = 'iPiLUtbmWB3Ml5f8Ay3A'
    client_secret = 'WH0MRvrfmm'
    encoded_moive_name = urllib.parse.quote(moive_name)
    
    query = "https://openapi.naver.com/v1/search/movie.json"
    option = "?display=1&yearfrom=2000&yearto=2018&query="
    
    url_query = query + option + encoded_moive_name
    
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

    result = []

    for j in range(1,maxPage+1) :
        inputStr = str1 + str2 + str3 + '&page=' + str(j)
        html = requests.get(inputStr).text
        soup = BeautifulSoup(html, 'html.parser')
        
        text_list = soup.select('body > div > div > div.score_result > ul div.score_reple > p')
        
        for i in text_list :
            temp = i.text
            temp = temp.rstrip()
            if temp.startswith("관람객") :
                temp = temp.split('관람객')[1]
            result.append(temp)
    
    
    return result


