import pandas as pd
import numpy as np
import datetime
import time
from VaxTraxFunctions import get_data
from requests import get


#Import data from API and put it in a pandas dataframe
endpoint = (
'https://api.coronavirus.data.gov.uk/v1/data?'
'filters=areaType=overview&'
'structure={"date":"date",'
            '"newPeopleVaccinatedFirstDoseByPublishDate":"newPeopleVaccinatedFirstDoseByPublishDate"'
            ',"newPeopleVaccinatedSecondDoseByPublishDate":"newPeopleVaccinatedSecondDoseByPublishDate"'
            ',"cumPeopleVaccinatedFirstDoseByPublishDate":"cumPeopleVaccinatedFirstDoseByPublishDate"'
            ',"cumPeopleVaccinatedSecondDoseByPublishDate":"cumPeopleVaccinatedSecondDoseByPublishDate"'
            '}'
)

#Only run once data has been updated
response = get(endpoint, timeout=10)
LastUpdated = datetime.datetime.strptime(response.headers['Last-Modified'][5:16], "%d %b %Y").date()
while(LastUpdated < datetime.datetime.now().date()):
    print("Data not yet updated")
    time.sleep(120)
    response = get(endpoint, timeout=10)
    LastUpdated = datetime.datetime.strptime(response.headers['Last-Modified'][5:16], "%d %b %Y")

print("Data updated at " + response.headers['Last-Modified'])

data = get_data(endpoint)
df=pd.json_normalize(data,"data")

#Change date from index to datetime variable and sum 1st and 2nd doses for overall doses per day 
by_date = df.groupby("date").sum().reset_index()
by_date["date_real"] = pd.to_datetime(by_date["date"]).dt.date
by_date["vaxes"] = by_date["newPeopleVaccinatedFirstDoseByPublishDate"] + by_date["newPeopleVaccinatedSecondDoseByPublishDate"]

by_date["FirstDoseOnly"] = by_date["cumPeopleVaccinatedFirstDoseByPublishDate"] - by_date["cumPeopleVaccinatedSecondDoseByPublishDate"]
by_date["TotalDoses"] = by_date["cumPeopleVaccinatedFirstDoseByPublishDate"] + by_date["cumPeopleVaccinatedSecondDoseByPublishDate"]

#calculate 7 day rolling average
by_date["7day_avg"] = by_date["vaxes"].rolling(7).mean()

#Create numpy array of dates starting from 11/01/21 
start_date = datetime.date(2021, 1 , 11)

#Extends x-axis by 2 weeks every 2 weeks
diff = (datetime.date.today() - datetime.date(2021,1,30)).days
AxisAdd = (diff/14) + 1
end_date = start_date + datetime.timedelta(days=28 + 14*AxisAdd)
end_datetime = datetime.datetime.combine(end_date, datetime.datetime.min.time()) #Keep a datetime of the end date so annoations can be plotted precisely 
number_of_days = (end_date - start_date).days + 1
date_list = np.asarray([(start_date + datetime.timedelta(days = day)) for day in range(number_of_days)])

