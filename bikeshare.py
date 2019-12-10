import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
print("Hello these is heba project")
    City = input('choose a city: ').strip().title()
    while(not City in ('Chicago', 'New York City','Washington')):
        City = input('choose a city: ').strip().title()

    # TO DO: get user input for month (all, january, february, ... , june)
    Month = input('choose a month or all: ').strip().title()
    while(not Month in ('All', 'January', 'February','March','April','May','June','July','August','September','October','November','December')):
        Month = input('choose a month or all: ').strip().title()
# we can use number instead of month name
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    Day = input('choose a day: ').strip().title()
    while(not Day in ('All','Mon','Tue','Wed','Thu','Fri','Sat','Sun')):
        Day = input('choose a day "short name": ').strip().title()


    print('-'*40)
    return City, Month, Day


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
    df = pd.read_csv(CITY_DATA[city.lower()])

    print(df.columns)

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    df['day'] = df['Start Time'].dt.day_name()
    df['month'] = df['Start Time'].dt.month_name()

    if month != 'All':
        df = df[df['month'] == month]

    if day != 'All':
        df = df[df['day'] == day]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("Most common month:\n{} \n".format(popular_month))

    # TO DO: display the most common day of week
    popular_day = df['day'].mode()[0]
    print("Most common day of the week:\n{} \n".format(popular_day))


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("Most common start hour:\n{} \n".format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most common start start station:\n{} \n".format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The most common ending station:\n{} \n".format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Combination Station'] = df['End Station'] + df['Start Station']
    popular_station = df['Combination Station'].mode()[0]
    print("The most common station:\n{} \n".format(popular_station))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(df['Trip Duration'].sum())


    # TO DO: display mean travel time
    print(df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())


    # TO DO: Display counts of gender
    print(df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
    print(df['Birth Year'].min())
    print(df['Birth Year'].max())
    print(df['Birth Year'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month,day =get_filters()
        df = load_data(city, month, day)

        raw_data = input('do you want to see the raw data? ').strip().lower()
        start = 0
        end =5
        while(raw_data == 'yes'):
            print(df.iloc[start:end])
            start += 5
            end += 5
            raw_data = input('do you want to see the raw data? ').strip().lower()

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()
