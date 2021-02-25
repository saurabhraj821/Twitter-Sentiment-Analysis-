#Import libraries
import pandas as pd 
import datetime as dt 
from twitterscraper import query_tweets
import seaborn as sns
import matplotlib.mlab as mlab
from datetime import date
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from langdetect import detect 
import matplotlib.pyplot as plt

#Handle exception
def detector(x):
    try:
       return detect(x)
    except:
        None 
                
analyzer = SentimentIntensityAnalyzer()

#Dates before ban
begin_date = dt.date(2019,2,15)
end_date = dt.date(2019,5,12)

#Dates after ban
begin_date_ = dt.date(2019,5,15)
end_date_ = dt.date(2019,9,12)

tweets_before = query_tweets("#huawei", begindate = begin_date, enddate= end_date, limit = 10000)
tweets_after = query_tweets("#huawei", begindate = begin_date_, enddate = end_date_, limit = 10000)
                            
before = pd.DataFrame(t.__dict__ for t in tweets_before)
after = pd.DataFrame(t.__dict__ for t in tweets_after)

#Filter for english tweets
before['lang'] = df_before['text'].apply(lambda x:detector(x))
before = df_before[df_before['lang'] == 'en']
after['lang'] = df_after['text'].apply(lambda x: detector(x))
after = df_after[df_after['lang'] == 'en'] 

#Save files
before.to_csv('before_ban.csv')
after.to_csv('after_ban.csv')

analyzer = SentimentIntensityAnalyzer()

df_before = pd.read_csv('before_ban.csv')
df_after = pd.read_csv('after_ban.csv')

#Get sentiment scores
sentiment_before = df_before['text'].apply(lambda x: analyzer.polarity_scores(x))
sentiment_after = df_after['text'].apply(lambda x: analyzer.polarity_scores(x))

#Put sentiment into dataframe
df_before = pd.concat([df_before, sentiment_before.apply(pd.Series)],1)
df_after = pd.concat([df_after, sentiment_after.apply(pd.Series)],1)

#Get histogram
hist_bef = df_before['compound']
hist_bef.hist()
mean_bef = hist_bef.mean()

hist_aft = df_after['compound']
hist_aft.hist()
mean_aft = hist_aft.mean()
