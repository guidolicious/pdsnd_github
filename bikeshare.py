# Gary Fudala Bikeshare Working Version 3
# Comment for GitHub Improve Documentation Section III

import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv'}

def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        cities = ['chicago','new york city','washington']
        city = input("\nWhich city would you like to assess? Choose between: 'Chicago', 'New York City', or 'Washington'.\n").lower()

        if city in cities:
            break

        else:
            print("\nPlease enter a valid city name.")

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        month = input("\nWhich month would you like to assess? Choose between: 'January', 'February', 'March', 'April', 'May', or 'June'. Enter 'All' to select all 6 months. \n").lower()

        if month in months:
            break

        else:
            print("\nPlease enter a valid month, or enter 'All' to select all 6 months.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
        day = input("\nWhich day of the week would you like to assess? Choose between: 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', or 'Saturday'? Type 'All' to select all 7 days \n").lower()

        if day in days:
            break

        else:
            print("\nPlease enter a valid day, or enter 'All' to select every day of the week")

    print('-'*40)
    print("\nThe chosen filters are: city = {}, month(s) = {}, day(s) of week = {}\n".format(city, month, day))
    print('-'*40)

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

    # NOTE: Read chosen city's csv file into dataframe

    df = pd.read_csv(CITY_DATA[city])

    # NOTE: need to gather month and day of week - but also need to convert Start Time into datetime datatype

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # NOTE: determine month and day of week from Start Time, and create dataframes
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # NOTE: adding a print(df) line to help debug tz error(s)
    #print(df) - tz error has been corrected

    # NOTE: If necessary, filter by month - so entire city data is not computed

    if month != 'all':
        month = month.title()
        months = ['January','February','March','April','May','June']
        # NOTE: index months list to obtain proper location within list, and increment
        month = months.index(month) + 1

        # NOTE: create a new dataframe from filtered monthly data
        df = df[df['month'] == month]
        #print(df) - dataframe successfully filtered by month

    # NOTE: if necessary, filter by day of week - so entire month is not computed

    if day != 'all':

    # NOTE: create new dataframe based upon day of week - dataframe was not showing selected day of week, so using pandas DataFrame.loc command
        #df = df[df['day_of_week'] == day.title()] - code was not populating correct day of week within dataframe
        df = df.loc[df['day_of_week'] == day.title()]
        #print(df) - dataframe successfully filtered by day of week

    return df


def time_stats(df, month, day):

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    if month == 'all':

        popular_month = df['month'].mode()[0]
    # NOTE: no data between July and December within all 3 csv files
        months = ['january','february','march','april','may','june']
    # NOTE: remember to eliminate 'All' or 'all' from entries, and need to subtract 1 since months list indexed from 0 to 5
        popular_month = months[popular_month - 1]
        print("The most popular month, based upon the selected criteria, is:", (popular_month).title())


    # TO DO: display the most common day of week

    if day == 'all':

        popular_day = df['day_of_week'].mode()[0]
        print("The most popular day of the week, based upon the selected critria, is: " + popular_day)


    # TO DO: display the most common start hour

    df['start_hour'] = df['Start Time'].dt.hour
    popular_hour = df['start_hour'].mode()[0]
    print("The most popular start hour, based upon the selected criteria, is at the {}:00 hour ".format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):

    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    popular_start_station = df['Start Station'].mode()[0]
    print("The most popular start station, based upon the selected criteria, is {}.".format(popular_start_station))

    # TO DO: display most commonly used end station

    popular_end_station= df['End Station'].mode()[0]
    print("\nThe most popular end station, based upon the selected criteria, is {}.".format(popular_end_station))

    # TO DO: display most frequent combination of start staion and end staion trip

    df['start_and_end_station'] = df['Start Station'] + " to " + df['End Station']
    popular_station_ends = df['start_and_end_station'].mode()[0]
    print("\nThe most frequent combination of start and end stations, \nbased upon the selected criteria, is: {}.".format(popular_station_ends))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_time = df['Trip Duration'].sum()

    print("The total travel time, based upon the selected criteria, is {:,} ".format(total_time) + "seconds.")

    # NOTE: convert the many seconds into more readable years, days, hours, minutes and seconds - use divmod, iteratively, to produce a quotient and a remainder
    minute,second = divmod(total_time, 60)
    hour,minute = divmod(minute, 60)
    day,hour = divmod(hour, 24)
    year,day = divmod(day, 365)

    print("This total travel time equals: {:.0f} year(s) : {:.0f} day(s) : {:.0f} hour(s) : {:.0f} minute(s) : {:.0f} second(s)".format(year,day,hour,minute,second))

    # TO DO: display mean travel time

    mean_travel_time = df['Trip Duration'].mean()
    # NOTE: Round the mean travel time to nearest integer to avoid partial seconds clutter
    mean_travel_time = round(mean_travel_time)

    print("\nThe mean travel time, based upon the selcted criteria, is: " + str(mean_travel_time) + " seconds")

    # NOTE: convert seconds to hrs, mins, sec
    minute,second = divmod(mean_travel_time, 60)
    hour,minute = divmod(minute, 60)
    print("This mean travel time equals: {:.0f} hour(s) : {:.0f} minute(s) : {:.0f} second(s)".format(hour,minute,second))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):

    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types below:

def bikeshare_users(df):

    #NOTE: count the blank User Type entries within the source .csv file
    user_types = df['User Type'].value_counts(dropna=False)
    print("The count of user types, based upon the selected criteria:\n" + str(user_types))

    # TO DO: Display counts of gender

    # NOTE: No gender data in washington.csv file - so print an exception when washington chosen

def gender_stats(df, city):

    start_time = time.time()

    try:
        gender_counts = df['Gender'].value_counts(dropna=False)
        print("\nThe gender counts, based upon the seleced criteria:\n" + str(gender_counts))

    except:

        print('\nThere is no gender data in the source "{}.csv" file.'.format(city))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    # TO DO: Display earliest, most recent, and most common year of birth.  Added median birth year to test this python capability and to see this stat

    start_time = time.time()
    try:

        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]
        # NOTE: add Median Birth Year as a new statistic
        median_birth_year = df['Birth Year'].median()

        print('\nEarliest birth year, based upon the selected criteria, is: {:.0f}'.format(earliest_birth_year))
        print('Most recent birth year, based upon the selected criteria, is: {:.0f}'.format(most_recent_birth_year))
        print('Most common birth year, based upon the selected criteria, is: {:.0f}'.format(most_common_birth_year))
        print('BONUS: Median birth year, based upon the selected criteria, is: {:.0f}'.format(median_birth_year))

    # NOTE: There is no Birth Year within the washington.csv file - need to print an exception when washington chosen

    except:
        print('\nThere is no birth year within the source "{}.csv" file.'.format(city))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        bikeshare_users(df)
        gender_stats(df, city)

        # NOTE: not modifying original restart code, as it is performing well
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
