import datetime
import tweepy_auth
from DailyPlot import today_n, wkavg_n, vax_per_min, past_7days
from CumulativePlot import today_total, pop_pct
from VaxTraxFunctions import project_tl

if __name__ == "__main__":
    api = tweepy_auth.twitter_api()

    # Tweet daily plot
    daily_file_name = "DailyPlot_" + datetime.datetime.today().strftime("%d%m%y")
    media1 = api.media_upload(daily_file_name+".png")      
    daily_tweet = ("Today's reported #COVID19 #vaccinations. \n\n" 
                + "\U0001F489 " + f'{today_n:,}' + " jabs recorded today!" 
                + "\n\n\U0001F489 That's " + str(vax_per_min) + " jabs per minute!" 
                + "\n\nStay positive everyone, we're getting there!" ) 
    daily_plot_tweet = api.update_status(status=daily_tweet, media_ids=[media1.media_id])

    # Tweet cumulative plot
    cum_file_name = "TotalPlot_" + datetime.datetime.today().strftime("%d%m%y")
    #Get tweet text
    cum_tweet = ("Today's total reported vaccinations." 
            +"\n\n\U0001F489 " + f'{today_total:,}' + " people have recieved at least a first dose of a #COVID19 #vaccine in the UK." 
            + "\n\n\U0001F489 " + f'{past_7days:,}' + " people have been #vaccinated in the past 7 days." 
           + "\n\n\U0001F489 " + str(pop_pct) + "%" + " of adults in the UK have now recieved at least one dose.")    
    media2 = api.media_upload(cum_file_name+".png")
    cum_plot_tweet = api.update_status(status=cum_tweet, media_ids=[media2.media_id])

    #Tweet projected vaccination timelines
    #Numbers for projected timelines tweet
    daily_15m = project_tl(today_n,15000000,today_total)
    daily_o50 = project_tl(today_n,32000000,today_total)
    #daily_all = project_tl(today_n,53000000,today_total)

    wkavg_15m = project_tl(wkavg_n,15000000,today_total)
    wkavg_o50 = project_tl(wkavg_n,32000000,today_total)
    #wkavg_all = project_tl(wkavg_n,53000000,today_total)


    #Tweet text
    proj_text = ("If we keep up today's rate, we'll have given a first #COVID19 #vaccine dose to..." 
                + "\n\n\U0001F489 Top 4 Priority Groups by " + daily_15m
                + "\n\n\U0001F489 All Vulnerable groups by " + daily_o50
                + "\n\nThese are very rough guesses, don't take them too seriously")   
    proj_tweet1 = api.update_status(status=proj_text)

    proj_text2 = ("If we keep up the 7 day average rate, we'll have given a first #COVID19 #vaccine dose to..." 
                + "\n\n\U0001F489 Top 4 Priority Groups by " + wkavg_15m
                + "\n\n\U0001F489 All Vulnerable groups by " + wkavg_o50
                + "\n\nThese are very rough guesses, don't take them too seriously")  
    proj_tweet2 = api.update_status(status=proj_text2, in_reply_to_status_id=proj_tweet1.id_str)