"""
/// save_list.py ///

project file that saves list of movies and crawls the reviews.
list of movies -> movieList.txt
reviews -> reviewData.txt

"""


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
