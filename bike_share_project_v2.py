#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
import pandas as pd
import numpy as np


# In[3]:


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


# In[4]:
##Git test changes

def get_filters():
    """
    
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter city name chicago, new york city, washington): ").lower()
    print(city)

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Enter month (all, january, february, ... , june):").lower()
    print(month)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter Day of Week (all, monday, tuesday, ... sunday): ").lower()
    print(day)

    print('-'*40)
    return city, month, day


# In[5]:


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


# In[6]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    popular_month = df['month'].mode()[0]    
    print('\nThe Most Common Month:\n', popular_month)
     
    
    # TO DO: display the most common day of week
    ############################################
    popular_day_week = df['day_of_week'].mode()[0]
    print('\nThe Most Common day of Week:\n', popular_day_week)
    
    

    # TO DO: display the most common start hour
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour[0]
    popular_hour = df['hour'].mode()[0]
    print('\nThe Most Popular Hour:\n', popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[7]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('\nMost Commonly Used Start Station:\n', popular_start_station)
    
    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('\nMost Commonly Used End Station:\n', popular_end_station)
    
    # display most frequent combination of start station and end station trip
    popular_startend_station = df.groupby(['Start Station','End Station']).size().idxmax()
    print('\nMost Frequent Combination of Start Station and End Station:\n', popular_startend_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[8]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = pd.to_timedelta(pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).sum()
    print('\nTotal Travel Time:\n', total_travel_time)
    
    # display mean travel time
    mean_travel_time = pd.to_timedelta(pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).mean()
    print('\nMean Travel Time:\n', mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[9]:


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nUser Types: \n', user_types)

    # Display counts of gender
    if city != 'washington':
        gender_count = df['Gender'].value_counts()
        print('\nGender Counts: \n', gender_count)
    else:
        print('\nThere is no Gender column in this city\n')

    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[12]:


def df_view(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while (view_data.lower() == 'yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input('\nDo you wish to continue? Enter yes or no.: \n').lower()                                    
        if view_display.lower() != 'yes':
            break 


# In[13]:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        
        df_view(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break                           
    


# In[ ]:


if __name__ == "__main__":
    main()


# In[ ]:


no

