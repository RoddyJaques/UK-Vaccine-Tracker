import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as tick
from matplotlib import font_manager as fm, rcParams
import seaborn as sns
import datetime
from VaxTraxFunctions import y_fmt
from GetData import by_date, date_list, number_of_days, end_datetime, start_date, end_date
from DailyPlot import past_7days

today_total = int(by_date[by_date["date_real"]==by_date["date_real"].max()]["cumPeopleVaccinatedFirstDoseByPublishDate"])
past_7days = int(by_date["TotalDoses"].iloc[-1] - by_date["TotalDoses"].iloc[-7])
pop_pct = int(100*today_total/53000000)

# Find out which priority group has been vaccinated
groups = [[1000000,"Care home residents + their carers"],[6500000,"over 80 + frontline health workers"],
          [8700000,"over 75"],[13400000,"over 70 and extremely vulnerable"],[16800000,"over 65"],
          [20600000,"over 60"],[25000000,"Over 55"],[29700000,"over 50"]]

#Set y_limit based on number of vaccinations
if today_total < 16800000: 
    y_limit = 25000000
else:
    y_limit = 35000000

for i in range(len(groups)):
    if today_total < groups[i][0]:
        current_group = groups[i][1]
        break

#Plot cumulative vaccinations per day and reference lines
fig, ax = plt.subplots(1,1,figsize=[20,11.25],facecolor="white")
ax.set_facecolor("white")

ax.stackplot(date_list[date_list <= by_date["date_real"].max() ], 
             by_date[by_date["date_real"]>= start_date]["cumPeopleVaccinatedSecondDoseByPublishDate"], 
             by_date[by_date["date_real"]>= start_date]["FirstDoseOnly"], 
            labels=["Fully vaccinated","First dose only"], colors= ["green","orangered"])

width = 1

biglabel_x = end_datetime-datetime.timedelta(days = 0.32*number_of_days)
shortlabel_x = end_datetime-datetime.timedelta(days = 0.09*number_of_days)

ax.plot(date_list, np.full(date_list.shape,1000000),label='_nolegend_',lw=width,c='black')
ax.text(biglabel_x,1300000,
        "Care home residents + their carers", fontsize=20)  


ax.plot(date_list, np.full(date_list.shape,6500000),label='_nolegend_',lw=width,c='black')
ax.text(biglabel_x,6800000,
        "Over 80s + frontline health workers", fontsize=20)


ax.plot(date_list, np.full(date_list.shape,8700000),label='_nolegend_',lw=width,c='black')
ax.text(shortlabel_x,9000000,
        "Over 75s", fontsize=20)

ax.plot(date_list, np.full(date_list.shape,13400000),label='_nolegend_',lw=width,c='black')
ax.text(biglabel_x,13700000,
        "Over 70s and extremely vulnerable", fontsize=20)

ax.plot(date_list, np.full(date_list.shape,16800000),label='_nolegend_',lw=width,c='black')
ax.text(shortlabel_x,17100000,
        "Over 65s", fontsize=20)

if today_total > 16800000: 
    ax.plot(date_list, np.full(date_list.shape,20600000),label='_nolegend_',lw=width,c='black')
    ax.text(shortlabel_x,20900000,
            "Over 60s", fontsize=20)

if today_total > 16800000:
    ax.plot(date_list, np.full(date_list.shape,25000000),label='_nolegend_',lw=width,c='black')
    ax.text(shortlabel_x,25300000,
            "Over 55s", fontsize=20)

if today_total > 16800000:
    ax.plot(date_list, np.full(date_list.shape,29700000),label='_nolegend_',lw=width,c='black')
    ax.text(shortlabel_x,30000000,
            "Over 50s", fontsize=20)

ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
ax.set_xlim(start_date, end_date)
ax.set_xticks(date_list[::2])

ax.set_ylim([0,y_limit])
ax.yaxis.set_major_formatter(tick.FuncFormatter(y_fmt))

ax.legend(loc='upper left',frameon=False, fontsize=20)

ax.tick_params(axis='y',labelsize=15)
ax.tick_params(axis='x',labelsize=13)

plt.title("Roddy's COVID19 vaccine tracker",
        fontsize=30, color='g' )
plt.xlabel('Date',fontsize=20)
plt.ylabel('Total vaccinations',fontsize=25)

sns.despine(top=True, right=True)

file_name = "TotalPlot_" + datetime.datetime.today().strftime('%d%m%y')

plt.savefig(file_name,bbox_inches="tight")