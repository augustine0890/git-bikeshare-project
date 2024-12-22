# Bikeshare Data Analysis
This project is a Python program designed to explore and analyze US bikeshare data for selected cities. The program allows users to filter data by city, month, and day, and view various statistics about bikeshare usage.

### Features
- **Filter Data**: Choose a city (Chicago, New York City, or Washington), a month, and a day of the week to analyze.
- **Statistics**:
    - Most popular stations and trips.
    - Trip duration statistics.
    - User statistics including user types, gender, and birth year (if available).
- **Raw Data**: View raw data upon request, 5 rows at a time.

### Usage
1. Clone the repository and navigate to the project directory.
2. Ensure the required data files (`chicago.csv`, `new_york_city.csv`, `washington.csv`) are in the project directory.
3. Run the program:
    ```bash
        python bikeshare.py
    ```
4. Follow the on-screen prompts to filter data and view statistics.

### Example Commands
- When prompted, enter the city, month, and day of the week you want to analyze (e.g., "chicago", "january", "monday").
- To view raw data, respond with "yes" when asked.
