from bs4 import BeautifulSoup as bs
import requests

link = input("Enter the link of the professor you would look at the comments of: ")

r = requests.get(link)

soup = bs(r.content, features="html.parser")

comments = soup.find_all("div", {"class": "Comments__StyledComments-dzzyvm-0 gRjWel"})
prof_name = soup.find('div', {'class': 'NameTitle__Name-dowf0z-0 cfjPUG'})
ratings = soup.find_all('div', {'class': 'CardNumRating__CardNumRatingNumber-sc-17t4b9u-2'})



rating_index = 0
difficulty_index = 1
comment_index = 0
while difficulty_index < len(comments):
    rating = ratings[rating_index]
    difficulty = ratings[difficulty_index]
    comment = comments[comment_index]
    print('Rating: ', rating.get_text())
    print('Difficulty: ', difficulty.get_text())
    print('Comment: ', comment.get_text())
    print('\n')
    rating_index += 2
    difficulty_index += 2
    comment_index += 1

index = 0
total = 0

for quality in range(0, len(ratings), 2):
    index+=1
    total += float(ratings[quality].get_text())
    average_review = total / index

if (round(average_review, 0) <= 5.0 and round(average_review, 0) >= 4.0):
    message = 'W prof!'
elif (round(average_review, 0) <= 4.0 and round(average_review, 0) >= 3.0):
    message = 'Not too bad of a prof!'
else:
    message = 'Yikes!'

print('Professor', prof_name.get_text(), 'has an average review of', round(average_review, 2), 'out of 5 over the past',
      index, 'reviews.', message)
