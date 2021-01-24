from requests import get
import datetime

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

def suffix(d):
    """ Function to return day month suffix
         
         Args:
            d: Numeric day of month 

         Returns:
            Correct suffix for day of month
    """ 
    return "th" if 11<=d<=13 else {1:"st",2:"nd",3:"rd"}.get(d%10, "th")

def custom_strftime(format, t):
    """ Function to format date with day month suffix
         
         Args:
            format: Desired format for date

         Returns:
            Date formatted with day of month suffixed
    """ 
    return t.strftime(format).replace("{S}", str(t.day) + suffix(t.day))

def project_tl(rate, target, current):
    """ Function to project dates at which targets will be vaccinated
         
         Args:
            rate: number of vaccinations per day
            target: target total number of vaccinations
            current: current total number of vaccinations

         Returns:
            date_text: string of date the target will be reached
    """ 

    days_to_target = (target-current)/rate
    date_target = datetime.datetime.today() + datetime.timedelta(days = days_to_target)

    date_text = custom_strftime("{S} %B %Y", date_target)
    return date_text
