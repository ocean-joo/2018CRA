"""
/// save_list.py ///

project file that saves list of movies and crawls the reviews.
list of movies -> movieList.txt
reviews -> reviewData.txt

"""


import movieReview as mr
import listofMovie as lm

data = lm.get_movie.list() # length = 675

listF = open("/home/hyewon/2018CRA/movieList.txt", 'w')
reviewF = open("/home/hyewon/2018CRA/reviewData.txt", 'w')

for i in data :
    listF.write(' '.join(i))
	listF.write('\n')

listF.close()

num = 1
for i in data :
    sympathy = mr.crawlReview(i[0], i[1], maxPage=10)
    lowest = mr.crawlReview(i[], i[], maxPage=7, sort="lowest")
    msg = "%d 번째 영화 -  %s" % (num, i[0])
    reviewF.write(msg)
	for j in sympathy :
        reviewF.write(' '.join(j))
        reviewF.write('\n')
    reviewF.write("\n\n낮은평점순\n")
    for k in lowest :
        reviewF.write(' '.join(k))
        reviewF.write("\n")
    reviewF.write("\n\n\n")
    num = num + 1

reviewF.close()
