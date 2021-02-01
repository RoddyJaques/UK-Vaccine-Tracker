# UK-Vaccine-Tracker
*A python program which plots the daily number of COVID19 vaccinations in the UK and tweets the result.*

GetData.py - Extracts data when it's uploaded to Gov.UK api

CumulativePlot.py - Plots cumulative vaccination numbers

DailyPlot.py - Plots daily vaccination numbers

Projections.py - Estimates when priority groups will be vaccinated by and creates figures with estimates

TweetPlots.py - Tweets figures created by CumulativePlot.py, DailyPlot.py and Projections.py in a thread

RetweetThread.py - ReTweets the first tweet of the previously created thread 

VaxTraxFunctions.py - Contains functions used to gather and format data

tweepy_auth.py - Python code to create tweepy API, access and consumer keys have been replaced by XXXXX's

