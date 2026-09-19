from datetime import datetime, date

print("===== DAY 16: PYTHON DATE & TIME EXERCISES =====\n")

# --------------------------------------------------
# 1. Get current day, month, year, hour, minute, timestamp
# --------------------------------------------------
now = datetime.now()

print("1) Current date and time info")
print("Day:", now.day)
print("Month:", now.month)
print("Year:", now.year)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Timestamp:", now.timestamp())
print()

# --------------------------------------------------
# 2. Format current date
# Format: "%m/%d/%Y, %H:%M:%S"
# --------------------------------------------------
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print("2) Formatted current date:")
print(formatted_date)
print()

# --------------------------------------------------
# 3. Convert string to time
# Today is "5 December, 2019"
# --------------------------------------------------
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")

print("3) String to datetime")
print("Original string:", date_string)
print("Converted datetime:", date_object)
print()

# --------------------------------------------------
# 4. Time difference between now and New Year
# --------------------------------------------------
current_time = datetime.now()
new_year = datetime(year=current_time.year + 1, month=1, day=1)

time_left = new_year - current_time
print("4) Time left until New Year:")
print(time_left)
print()

# --------------------------------------------------
# 5. Time difference between 1 January 1970 and now
# --------------------------------------------------
epoch = datetime(1970, 1, 1)
time_since_epoch = current_time - epoch

print("5) Time since 1 January 1970:")
print(time_since_epoch)
print()

# --------------------------------------------------
# 6. Uses of datetime module
# --------------------------------------------------
print("6) Uses of datetime module:")
print("- Time series analysis")
print("- Logging user activity timestamps")
print("- Scheduling tasks")
print("- Blog post timestamps")
print("- Measuring execution time")

print("\n===== END OF DAY 16 =====")