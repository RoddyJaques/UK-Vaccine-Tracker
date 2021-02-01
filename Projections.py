from DailyPlot import wkavg_n
from CumulativePlot import today_total
import matplotlib.pyplot as plt
import datetime
from VaxTraxFunctions import project_tl


wkavg_15m = project_tl(wkavg_n,15000000,today_total)
wkavg_o50 = project_tl(wkavg_n,32000000,today_total)

fig, ax = plt.subplots(1,1,figsize=[20,11.25],facecolor="#005EB8")
ax.set_facecolor("#005EB8")
ax.axis("off")

plt.text(0.005,0.95,("@VaccinationsUK")
         ,font="Arial",fontsize=30,color="white")

plt.text(0.5,0.35,("If we carry on vaccinating as many people as we did over\nthe past week we'll be able to give a first dose to:"
                 +"\n\nTop 4 priority groups by"
                 +"\n\n\nAll vulnerable groups by")
         ,font="Arial",fontsize=40,color="white", ha="center")


plt.text(0.5,0.47,wkavg_15m,
         font="Arial",fontweight="bold",fontsize=40,color="white", ha="center")


plt.text(0.5,0.27,wkavg_o50,
         font="Arial",fontweight="bold",fontsize=40,color="white", ha="center")

plt.text(0.5,0.05,"This is a projection, not a prediction, based on a very rough calculation",
         font="Arial",fontsize=35,color="white", ha="center")

proj_file = "WeekProject_" + datetime.datetime.today().strftime("%d%m%y")

plt.savefig(proj_file,bbox_inches="tight")