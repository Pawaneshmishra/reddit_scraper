#use this to install praw library
#pip install praw --quiet

import praw 

client_id = input('give client id : ')
client_secret = input('give client secret key : ')
username = input('give reddit username : ')
password = input('give reddit password : ')

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent='API')

import pandas as pd

keyword = input('give keyword to search : ')

#this pandas dataframe saves our data
posts=[]

#this performs search and creates an object
python_reddit = reddit.subreddit('all').search(keyword,time_filter='day',limit=10000)

#appends items to our dataframe
for i in python_reddit:
  posts.append([i.title,i.subreddit,i.author,i.ups,i.upvote_ratio,i.num_comments,i.url])

posts = pd.DataFrame(posts,columns=['Title','Subreddit_Name','Author_Name','Upvotes', 'Upvote_Ratio', 'Number_of_Comments','Url_of_Post'])

#prints shape of our collected dataframe
#posts.shape

#prints first 5 elements of our collected dataframe
#posts.head()

#can give any location
posts.to_csv(r'C:\Users\mpawa\OneDrive\Desktop\file3.csv', index=False)