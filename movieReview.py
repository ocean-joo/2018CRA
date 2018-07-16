# -*- coding: utf-8 -*-

def crawlReview(Mname, Myear, maxPage=10, sort='sympathyScore') :
        
    import urllib.request, urllib.parse
    
    client_ID = "iPiLUtbmWB3Ml5f8Ay3A"
    client_secret = "WH0MRvrfmm"
    encoded_movie_name = urllib.parse.quote(Mname)
    
    api_url = "https://openapi.naver.com/v1/search/movie.json"
    api_option = "?display=1&yearfrom=" + Myear + "&yearto=" + Myear + "&query="
    api = api_url + api_option + encoded_movie_name
    
    request = urllib.request.Request(api)
    request.add_header("X-Naver-Client-Id",client_ID)
    request.add_header("X-Naver-Client-Secret",client_secret)
    
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    
    if rescode != 200 :
        print("Error Code : " + str(rescode))	
	
    import json
    content = json.loads(response.read())
	
    if not content :
        msg = "save fail %s" %Mname	
        print(msg)
        return -1

    try :
        url = content['items'][0]['link']
    except :
        print("save fail %s") %Mname
	    return -1	
    # rating = content['items'][0]['userRating']
    
    str2 = url.split('code=')[1]
    str1 = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code='
    str3 = '&type=after&onlyActualPointYn=N&order=' + sort
    # to change order, add option //order=sympathyScore// or newest or highest or lowest
    
    import requests
    from bs4 import BeautifulSoup
      
    text_result = []
    rating_result = []
    
    for i in range(1, maxPage+1) :
        inputStr = str1 + str2 + str3 + '&page=' + str(i)
        html = requests.get(inputStr).text
        soup = BeautifulSoup(html, 'html.parser')
    
        text_list = soup.select('body > div > div > div.score_result > ul div.score_reple > p')

        for j in text_list :
            temp = j.text
            temp = temp.rstrip()
            if temp.startswith("관람객") :
                temp = temp.split("관람객")[1]
            text_result.append(temp)

        rating_list = soup.select('body > div > div > div.score_result > ul div.star_score > em')

        for k in rating_list :
            temp = k.text
            rating_result.append(temp)

    result = list(zip(text_result, rating_result))
    return result

def crawl_byUrl(url, maxPage=10, sort="sympathyScore") :
    str2 = url.split('code=')[1]
    str1 = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code='
    str3 = '&type=after&onlyActualPointYn=N&order=' + sort
	# to change order, add option //order=sympathyScore// or newest or highest or lowest
	  
    import requests
    from bs4 import BeautifulSoup
     
    text_result = []
    rating_result = []
						    
    for i in range(1, maxPage+1) :
        inputStr = str1 + str2 + str3 + '&page=' + str(i)
        html = requests.get(inputStr).text
        soup = BeautifulSoup(html, 'html.parser')
							     
        text_list = soup.select('body > div > div > div.score_result > ul div.score_reple > p')

        for j in text_list :
            temp = j.text
            temp = temp.rstrip()
            if temp.startswith("관람객") :
                temp = temp.split("관람객")[1]
                text_result.append(temp)

        rating_list = soup.select('body > div > div > div.score_result > ul div.star_score > em')

        for k in rating_list :
            temp = k.text
            rating_result.append(temp)

    result = list(zip(text_result, rating_result))
    return result
