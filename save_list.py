"""
/// save_list.py ///

project file that saves list of movies and crawls the reviews.
list of movies -> movieList.txt
reviews -> reviewData.txt



import movieReview as mr
import ListofMovie as lm
import get_api as ga

data = lm.get_movie_list() # length = 675

listF = open("/home/hyewon/2018CRA/movieList.txt", 'w')
reviewF = open("/home/hyewon/2018CRA/reviewData.txt", 'w')

for i in data :
    listF.write(' '.join(i))
    listF.write('\n')

listF.close()

num = 1
for i in data :
    pyear = ga.get_info(i[0], i[1])['prdtYear']
    sympathy = mr.crawlReview(i[0], pyear, maxPage=10)
    lowest = mr.crawlReview(i[0], pyear, maxPage=7, sort="lowest")
    msg = "%d 번째 영화 -  %s\n공감순\n" % (num, i[0])
    reviewF.write(msg)
    for j in sympathy :
        reviewF.write(' '.join(j) + '\n')
    reviewF.write("\n\n낮은평점순\n")
    for k in lowest :
        reviewF.write(' '.join(k) + '\n')
    reviewF.write("\n\n\n")
    num = num + 1

reviewF.close()


# change the file form (.txt -> .csv)


import movieReview as mr
import ListofMovie as lm
import get_api as api
import csv

data = lm.get_movie_list()

reviewF = open("/home/hyewon/2018CRA/CSVmovie.csv", 'w', encoding='utf-8', newline='')

rf = csv.writer(reviewF)

# making movie list
rf.writerow(['Movie Name', 'Review', 'Sentiment'])

for i in data :
	pyear = api.get_info(i[0], i[1])['prdtYear']
	sympathy = mr.crawlReview(i[0], pyear, maxPage=10)
	lowest = mr.crawlReview(i[0], pyear, maxPage=7, sort='lowest')
	for j in sympathy :
		rf.writerow([i[0], j[0], j[1]])
	for k in lowest :
		rf.writerow([i[0], k[0], k[1]])
reviewF.close()

"""


# crawling many review....

import movieReview as mr
import ListofMovie as lm
import get_api as api
import csv

data = lm.get_movie_list()

tempF = open("/home/hyewon/2018CRA/allReview.csv", 'a', encoding='utf-8', newline='')

f = csv.writer(tempF)
#f.writerow(['Movie Name', 'Review', 'Sentiment'])

for i in data[32] :
    pyear = api.get_info(i[0], i[1])['prdtYear']
    Rlist = mr.crawlReview(i[0], i[1], pyear, maxPage=500)
    for j in Rlist :
        f.writerow([i[0], j[0], j[1]])

tempF.close()
