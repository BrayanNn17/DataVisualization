import csv
from datetime import datetime
from matplotlib import pyplot as plt
# Get dates and high temperatures from file.
filename = 'death_valley_2014.csv'
with open(filename) as f:
 reader = csv.reader(f)
 header_row = next(reader)
 
 dates, highs, lows = [], [], []
 for row in reader:
  try:
   current_date = datetime.strptime(row[0], "%Y-%m-%d")
   high = int(row[1])
   low = int(row[3])
  except ValueError:
   print(current_date, 'missing data')
 else:
  dates.append(current_date)
  highs.append(high)
  lows.append(low)


# Format plot.
title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize=20)