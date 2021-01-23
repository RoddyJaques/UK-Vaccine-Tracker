import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as tick
import seaborn as sns
import datetime
from requests import get

def get_data(url):
    """ Taken from the GOV.UK COVID developer page, gets JOSN data from GOV.UK API
        
        Args:
            url: API URL for GOV.UK COVID data 

        Returns:
            response: JSON data requested from url
    """
    response = get(url, timeout=10)
    
    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: { response.text }')
        
    return response.json()


def today_anno(data):
    """ Return's the most recent day's data and creates the annotation text
         
         Args:
            data: Dataset with vaccination data

         Returns:
            today: Pandas DataFrame with only the most recent day's data
            anno: Annotation text for the most recent point on the plot
    """

    today = data[data["date_real"]==data["date_real"].max()]
    
    if today["date_real"].iloc[0].weekday() in [0,1,2,3,6]:
        return today, f'{int(today["vaxes"].iloc[0]):,}' + " vaccinations"
        
    elif today["date_real"].iloc[0].weekday() in [4,5]:
        return today, f'{int(today["vaxes"].iloc[0]):,}' + " vaccinations\n(excl Scotland and Wales)"

def y_fmt(tick_val,pos):
    """ Function to format y axis ticks as e.g. 100,000 = 100k
         
         Args:
            tick_val: Tick value
            pos: position of tick

         Returns:
            String for tick value
    """
    
    if tick_val > 1000000:
        val = int(tick_val/1000000)
        return '{:d}M'.format(val)
    
    elif tick_val > 1000:
        val = int(tick_val/1000)
        return '{:d}k'.format(val) 
    
    else: 
        return int(tick_val)