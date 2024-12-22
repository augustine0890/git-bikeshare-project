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

    # Define valid cities, months, and days
    cities = ['chicago', 'new york city', 'washington']
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    # Get user input for city
    while True:
        city = input('Please enter a city (chicago, new york city, washington): ').lower()
        if city in cities:
            break
        else:
            print("Invalid input. Please enter a valid city.")

    # Get user input for month
    while True:
        month = input('Please enter a month (all, january, february, ..., june): ').lower()
        if month in months:
            break
        else:
            print("Invalid input. Please enter a valid month.")

    # Get user input for day of week
    while True:
        day = input('Please enter a day of week (all, monday, tuesday, ..., sunday): ').lower()
        if day in days:
            break
        else:
            print("Invalid input. Please enter a valid day of the week.")

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

    # Valdiate the city input
    if city not in CITY_DATA:
        print(f"Error: '{city}' is not a valid city. Please choose from {list(CITY_DATA.keys())}.")
        return pd.DataFrame()  # Return an empty DataFrame
    
    try:
        # Load data for the specified city
        df = pd.read_csv(CITY_DATA[city])
    except FileNotFoundError:
        print(f"Error: The data file for '{city}' could not be found. Please check the file path or name.")
        return pd.DataFrame()  # Return an empty DataFrame
    except Exception as e:
        print(f"An unexpected error occurred while loading the data for '{city}': {e}")
        return pd.DataFrame()  # Return an empty DataFrame

    # Convert the 'Start Time' and 'End Time' columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'], errors='coerce')
    df['End Time'] = pd.to_datetime(df['End Time'], errors='coerce')
    
    # Extract month and day of week from 'Start Time'
    df['Month'] = df['Start Time'].dt.month_name().str.lower()
    df['Day of Week'] = df['Start Time'].dt.day_name().str.lower()
    
    # Filter by month if applicable
    if month != 'all':
        df = df[df['Month'] == month]
    
    # Filter by day of week if applicable
    if day != 'all':
        df = df[df['Day of Week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    most_common_month = df['Month'].mode()[0]
    print('Most Common Month:', most_common_month.title())

    # Display the most common day of week
    most_common_day = df['Day of Week'].mode()[0]
    print('Most Common Day of Week:', most_common_day.title())

    # Extract hour from 'Start Time' and display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    most_common_hour = df['Hour'].mode()[0]
    print('Most Common Start Hour:', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display the most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station:', most_common_start_station)

    # Display the most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('Most Common End Station:', most_common_end_station)

    # Display the most frequent combination of start station and end station trip
    most_common_start_end_trip = (df['Start Station'] + " to " + df['End Station']).mode()[0]
    print('Most Frequent Start to End Station Trip:', most_common_start_end_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time: {:.2f} seconds'.format(total_travel_time))

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time: {:.2f} seconds'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of User Types:\n', user_types)

    # Display counts of gender (if available)
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('\nCounts of Gender:\n', gender_counts)
    else:
        print('\nGender data not available for this city.')

    # Display earliest, most recent, and most common year of birth (if available)
    if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        
        print('\nEarliest Year of Birth:', earliest_year)
        print('Most Recent Year of Birth:', most_recent_year)
        print('Most Common Year of Birth:', most_common_year)
    else:
        print('\nBirth Year data not available for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """
    Displays 5 rows of raw data at a time upon user request.

    Args:
        df (DataFrame): The dataset to display rows from.
    """
    start_loc = 0
    while True:
        show_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no: ').lower()
        if show_data == 'yes':
            print(df.iloc[start_loc:start_loc + 5])
            start_loc += 5
            if start_loc >= len(df):
                print("You've reached the end of the data.")
                break
        elif show_data == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        if df.empty:
            print("No data available for the given filters. Please try again.")
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break
            else:
                continue
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
