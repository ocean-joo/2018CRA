# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 19:42:37 2018

@author: hyeOn
"""

import urllib.request
key = "5c099619fc8751d5693b8a368b769a79"

def getDailyRanking(date) :
	api_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?"
	api_option = "key=" + key + "&targetDt" + str(date)
	url = api_url + api_option

	response = urllib.request.urlopen(url)

	if response.getcode() != 200 :
		print("Error Code : " + str(response.getcode()))
	
	import json
	content = json.loads(response.read())
	
	return content


getDailyRanking(20180709)
