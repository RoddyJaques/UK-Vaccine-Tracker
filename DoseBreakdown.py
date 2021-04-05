from GetData import by_date
import matplotlib.pyplot as plt
import datetime
from VaxTraxFunctions import project_tl

#Get latest day only
today = by_date[by_date["date_real"]==by_date["date_real"].max()]
today_first = f'{int(today["newPeopleVaccinatedFirstDoseByPublishDate"].iloc[0]):,}'
today_second = f'{int(today["newPeopleVaccinatedSecondDoseByPublishDate"].iloc[0]):,}'

fig, ax = plt.subplots(1,1,figsize=[20,11.25],facecolor="#005EB8")
ax.set_facecolor("#005EB8")
ax.axis("off")

plt.text(0.005,0.95,("@VaccinationsUK")
         ,font="Arial",fontsize=30,color="white")

plt.text(0.5,0.35,("Today's dose breakdown:"
                 +"\n\nFirst doses"
                 +"\n\n\nSecond doses")
         ,font="Arial",fontsize=40,color="white", ha="center")


plt.text(0.5,0.47,today_first,
         font="Arial",fontweight="bold",fontsize=40,color="white", ha="center")


plt.text(0.5,0.27,today_second,
         font="Arial",fontweight="bold",fontsize=40,color="white", ha="center")


proj_file = "DoseBreakdown_" + datetime.datetime.today().strftime("%d%m%y")

plt.savefig(proj_file,bbox_inches="tight")