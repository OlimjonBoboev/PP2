from datetime import datetime, timedelta

# Subtract five days from current date
d = datetime.today() - timedelta(days=5)
print("Five days ago:", d.date())

# Print yesterday, today, tomorrow
t = datetime.today()
print("Yesterday:", (t - timedelta(days=1)).date())
print("Today:", t.date())
print("Tomorrow:", (t + timedelta(days=1)).date())

# Drop microseconds from datetime
now = datetime.now().replace(microsecond=0)
print("Without microseconds:", now)

# Calculate difference between two dates in seconds
d1 = datetime(2024, 3, 1, 12, 0, 0)
d2 = datetime(2024, 3, 5, 15, 30, 0)
diff = (d2 - d1).total_seconds()
print("Difference in seconds:", diff)
