## **Date Project and README.md file created:**

9/10/2021

###

## **Project:**

Bikeshare - Project 2 for Udacity Data Science Using Python Class

###

## **Summary:**

###

*Python code displays Bikeshare statistics based upon selections prompted from end-users.  These prompts and selections include:*
###

- The city to query and report
- The month to query and report
- The day of the week to query and report

###

*The statistics displayed, where applicable, are:*
###

  - Most Common Month
  - Most Common Day of Week
  - Most Common Start Hour
###

  - Most Common Start Station
  - Most Common End Station
  - Most Common Combination of Start and End Station
###

  - Total Travel Time
  - Mean Travel Time
  - Count by User Type
###

*...and, if the source data is available, report:*
###

  - Count by Gender
  - Earliest Birth Year
  - Most Recent Birth Year
  - Most Common Birth Year
  - Median Birth Year (bonus statistic)

###

## **Files Used:**

####

- *bikeshare.py*
####

The python logic reads the source bikeshare data contained in the following files:
####

- *chicago.csv*
- *new york city.csv*
- *washington.csv*

**Note: These .csv source data files _will not be pushed to GitHub_ due to their size**

###

## **Credits:**

This *README.md* file was built using trial and error, and using the information available at: [Github Basic Writing and Formatting Syntax](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

*bikeshare.py* was built using trial and error, and by using:

- The Mentor help on [Udacity Mentor Help](https://knowledge.udacity.com) to address a recurring tz error.
- *stackoverflow.com* to learn how to add a thousands separator to a number.
- Read sections on Lists and Dataframes within Eric Matthes' *"Python Crash Course - 2nd Edition"* for general guidance.
- Examined *pandas.pydata.org* website to learn how to access a group of rows/columns, via the *DataFrame.loc* command.  This resolved recurring issues with the day_of_week dataframe.
