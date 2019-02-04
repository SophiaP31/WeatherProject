import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import json
import matplotlib.pyplot as plt


# Step 1: Webscrape the data
# Pick 1 state and get tempurature data by day for last 90 days

r = requests.get("https://www.usclimatedata.com/climate/alabama/united-states/3170")

# Nick's example
t = r.text
indexOf = t.find('var the_data = \'[{')
# print(t[indexOf: indexOf + 100])

indexEnd = t[indexOf:].find("var precipitation_max")
chunk = t[indexOf: indexOf+indexEnd-1]

start = chunk.find("'")
end = chunk.find("';")

ourList = chunk[start+1:end]

ourList = json.loads(ourList)

# print(type(ourList))
# print(ourList)

'''
soup = bs(r.content)
code = soup.find("script", attrs={"type":"text/javascript","language":"javascript"})
print(code)


the_data = '[{"Month": "Jan", "Low":36, "High":57, "Precipitation": 4.65},{"Month": "Feb", "Low":39, "High":62, "Precipitation": 5.28},{"Month": "Mar", "Low":45, "High":70, "Precipitation": 5.94},{"Month": "Apr", "Low":52, "High":77, "Precipitation": 4.02},{"Month": "May", "Low":61, "High":84, "Precipitation": 3.54},{"Month": "Jun", "Low":68, "High":90, "Precipitation": 4.06},{"Month": "Jul", "Low":71, "High":92, "Precipitation": 5.24},{"Month": "Aug", "Low":71, "High":92, "Precipitation": 3.98},{"Month": "Sep", "Low":65, "High":87, "Precipitation": 3.98},{"Month": "Oct", "Low":53, "High":78, "Precipitation": 2.91},{"Month": "Nov", "Low":44, "High":69, "Precipitation": 4.61},{"Month": "Dec", "Low":37, "High":60, "Precipitation": 4.84}]'
the_New_data = json.loads(the_data)
print(the_New_data[0])
'''



# Step 2: Put data into a pandas dataframe
df = pd.DataFrame(ourList)
#
# print(df)


#Step 3: Make a graph!

months =[]
for i in ourList:
    months.append(i["Month"])
precipitations =[]
for i in ourList:
    precipitations.append(i["Precipitation"])
#
# print(months)
# print(precipitations)

plt.plot(months,precipitations)
plt.show()
