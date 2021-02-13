import datetime
import tweepy_auth
from DailyPlot import today_n, wkavg_n, vax_per_min
from CumulativePlot import today_total, pop_pct, past_7days
from VaxTraxFunctions import project_tl

if __name__ == "__main__":
    api = tweepy_auth.twitter_api()

    # Tweet daily plot
    daily_file_name = "DailyPlot_" + datetime.datetime.today().strftime("%d%m%y")
    media1 = api.media_upload(daily_file_name+".png")      
    daily_tweet = ("Today's #COVID19 #vaccine update thread. \U0001F9F5 \n\n" 
                + "\U0001F489 " + f'{today_n:,}' + " jabs recorded today!" 
                + "\n\n\U0001F489 That's " + str(vax_per_min) + " jabs per minute!" 
                + "\n\nStay positive everyone, we're getting there!" ) 
    tweet1 = api.update_status(status=daily_tweet, media_ids=[media1.media_id])

    # Tweet cumulative plot
    cum_file_name = "TotalPlot_" + datetime.datetime.today().strftime("%d%m%y")
    #Get tweet text
    cum_tweet = ("Today's total reported vaccinations." 
            +"\n\n\U0001F489 " + f'{today_total:,}' + " people have recieved at least a first dose of a #COVID19 #vaccine in the UK." 
            + "\n\n\U0001F489 " + f'{past_7days:,}' + " people have been #vaccinated in the past 7 days." 
           + "\n\n\U0001F489 " + str(pop_pct) + "%" + " of adults in the UK have now recieved at least one dose.")    
    media2 = api.media_upload(cum_file_name+".png")
    tweet2 = api.update_status(status=cum_tweet, media_ids=[media2.media_id],in_reply_to_status_id=tweet1.id_str)

    with open("tweet_id.txt","w") as tweet_id:
        tweet_id.write(tweet1.id_str)

