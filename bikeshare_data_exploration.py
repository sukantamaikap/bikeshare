import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

MONTHS = {'JAN': '1',
          "FEB": "2",
          'MAR': '3',
          'APR': '4',
          'MAY': '5',
          'JUN': '6',
          'JUL': '7',
          'AUG': '8',
          'SEP': '9',
          'OCT': '10',
          'NOV': '11',
          'DEC': '12'}

DAY = {'MON': 'Monday',
       'TUE': 'Tuesday',
       'WED': 'Wednesday',
       'THU': 'Thursday',
       'FRI': 'Friday',
       'SAT': 'Saturday',
       'SUN': 'Sunday'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print("Press Ctrl + c if you want to exit at any moment !!!!")

    city_found, month_found, day_found = False, False, False

    while True:
        print('\n\n')

        # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        if not city_found:
            city = input("We have 3 cities available to explore : Chicago, Washington, New York City. Please choose "
                         "one : ")
            city = city.lower()
            if city not in CITY_DATA:
                print("Invalid city or data not available, please choose one of the 3 : Chicago, Washington, "
                      "New York City")
                continue
            else:
                city_found = True

        print('\n\n')

        # get user input for month (all, january, february, ... , june)
        if not month_found:
            month = input("Enter month you want to explore. Choose one of : "
                          "JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC :")
            month = month.upper()
            if month not in MONTHS:
                print("Invalid month entered!!! Enter a valid month!!!!")
                continue
            else:
                month_found = True

        print('\n\n')

        # get user input for day of week (all, monday, tuesday, ... sunday)
        if not day_found:
            day = input("Enter day you want to explore. Choose one of : MON, TUE, WED, THU, FRI, SAT, SUN :")
            day = day.upper()
            if day not in DAY:
                print("Invalid day entered!!! Enter a valid day!!!!")
                continue
            else:
                day_found = True
                break

    print('-' * 40)
    print('\n')
    return city, month, day


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
    df = pd.read_csv(CITY_DATA.get(city))

    # extract start month from the Start time column to create Start Month column
    df['Start Month'] = pd.DatetimeIndex(df['Start Time']).month

    # extract end month from the Start time column to create Start Month column
    df['End Month'] = pd.DatetimeIndex(df['End Time']).month

    #extract start day from the Start time column to create Start Day column
    df['Start Day'] = pd.DatetimeIndex(df['Start Time']).day

    # extract start day from the Start time column to create Start Day column
    df['End Day'] = pd.DatetimeIndex(df['End Time']).day

    # extract start hour from the Start Time column to create an Start Hour column
    df['Start Hour'] = pd.DatetimeIndex(df['Start Time']).hour

    # extract end hour from the End Time column to create an End Hour column
    df['End Hour'] = pd.DatetimeIndex(df['End Time']).hour

    #filter month
    if month != '':

    # filter day
    if day != '':

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    # display the most common day of week

    # display the most common start hour

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    # display most commonly used end station

    # display most frequent combination of start station and end station trip

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    # display mean travel time

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    # Display counts of gender

    # Display earliest, most recent, and most common year of birth

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        print("Input to be processed -> City : {}, Month : {}, Day : {}".format(city, month, day))

        df = load_data(city, month, day)

        # time_stats(df)
        # station_stats(df)
        # trip_duration_stats(df)
        # user_stats(df)
        #
        # restart = input('\nWould you like to restart? Enter yes or no.\n')
        # if restart.lower() != 'yes':
        #     break


if __name__ == "__main__":
    main()
