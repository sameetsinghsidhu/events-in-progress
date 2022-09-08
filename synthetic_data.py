import datetime
from calendar import monthrange
from random import randrange

def generate_dataset(n: int) -> list:
    """
    Generates a list consisting of n dictionaries in the form:
    
        dict {
            "start": datetime.datetime object,
            "end": datetime.datetime object
        }
    
    end > start always.
    
    end will be greater than the start datetime by a minimum of 1hr 
    and upto a maximum of 11 hours 59 minutes and 59 seconds
    
    Parameter n: number of dictionaries in the list to produce
    
    Returns list[dict] of length n
    """
    
    def random_date_pair(year, month):
        """
        Given a year and month this function returns a single dictionary
        
        dict { "start": datetime, "end": datetime }, more details above
        
        As we can assume all plays occur in a single calendar month the exact
        year and month to be used will be generated outside of this function.
        Then this function can be repeatedly called to generate the n samples
        for that particular year, month
        """
        
        # Calculating the number of days in the random month we picked. This also accounts for leap years
        days_in_month = monthrange(year, month)[1]

        # Picking a random day from the month above
        day = randrange(1, days_in_month, 1)
        
        # Selecting a random hour
        hour = randrange(0, 24, 1)
        
        # Picking a random minute
        minute = randrange(0, 60, 1)
        
        # Picking a random second
        second = randrange(0, 60, 1)
        
        # Picking the hour, minute and second increment
        # Since we can assume a single play lasts a few hours I have picked a range of upto 12 hours
        added_hours = randrange(1, 12, 1)
        added_minutes = randrange(0, 60, 1)
        added_seconds = randrange(0, 60, 1)
        
        # Creating the start datetime object
        start = datetime.datetime(year = year, month = month, day = day, hour = hour, minute = minute, second = second)
        
        # Adding the increment to the start point
        end = start + datetime.timedelta(hours = added_hours, minutes = added_minutes, seconds = added_seconds)
        
        return {
                "start": start, 
                "end": end
               }

    
    # Picking a random year in this range. Since ITV started in 1955 :)
    year = randrange(1955, 2022, 1) 

    # Picking a random month of the year
    month = randrange(1, 13, 1)
    
    plays = []
    
    for _ in range(n):
        plays.append(random_date_pair(year, month))
        
    return plays