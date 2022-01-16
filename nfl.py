from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from itertools import islice
import statistics

year = ''
stat_type = ''
category = ''

year = input("What year would you like to look at? Enter anything from 1990 through 2021.\n")

while (len(year) != 4) or (int(year) < 1990) or (int(year) > 2021):
    year = input("Choose a valid year between 1990 and 2021.\n")

stat_type = input("Enter what type of stats you want to look at. \nType in 'rushing', 'receiving', or 'passing'.\n")

while (stat_type != "rushing") and (stat_type != "receiving") and (stat_type != "passing"):
    stat_type = input("Choose a valid stat type. \nType in 'rushing', 'receiving', or 'passing'.\n")

if stat_type == 'rushing':
    category = input(""
                     "Which category would you like to see the descriptive statistics for? \nYour options are "
                     "Rushing Yards(type in 'Yds'), Rushing Attempts('Att'), and Rushing Touchdowns('TD').\n"
                     "")
    while (category != 'Yds') and (category != 'Att') and (category != 'TD'):
        category = input("Choose a valid category(type in 'Yds', 'Att', or 'TD').\n")
elif stat_type == 'receiving':
    category = input("Which category would you like to see the descriptive statistics for?\n"
                     "Your options are Receiving Yards(type in 'Yds'), Receptions('Rec'), and Receiving "
                     "Touchdowns('TD').\n")
    while (category != 'Yds') and (category != 'Rec') and (category != 'TD'):
        category = input("Choose a valid category(type in 'Yds', 'Rec', or 'TD').\n")
else:
    category = input(
        "Which category would you like to see the descriptive statistics for? \nYour options are Passing Yards(type "
        "in 'Yds'), Passing Touchdowns('TD'), and Interceptions('Int').\n")
    while (category != 'Yds') and (category != 'TD') and (category != 'Int'):
        category = input("Choose a valid category(type in 'Yds', 'TD', or 'Int').\n")

seasons_rushing = [
    'https://www.pro-football-reference.com/years/1990/rushing.htm',
    'https://www.pro-football-reference.com/years/1991/rushing.htm',
    'https://www.pro-football-reference.com/years/1992/rushing.htm',
    'https://www.pro-football-reference.com/years/1993/rushing.htm',
    'https://www.pro-football-reference.com/years/1994/rushing.htm',
    'https://www.pro-football-reference.com/years/1995/rushing.htm',
    'https://www.pro-football-reference.com/years/1996/rushing.htm',
    'https://www.pro-football-reference.com/years/1997/rushing.htm',
    'https://www.pro-football-reference.com/years/1998/rushing.htm',
    'https://www.pro-football-reference.com/years/1999/rushing.htm',
    'https://www.pro-football-reference.com/years/2000/rushing.htm',
    'https://www.pro-football-reference.com/years/2001/rushing.htm',
    'https://www.pro-football-reference.com/years/2002/rushing.htm',
    'https://www.pro-football-reference.com/years/2003/rushing.htm',
    'https://www.pro-football-reference.com/years/2004/rushing.htm',
    'https://www.pro-football-reference.com/years/2005/rushing.htm',
    'https://www.pro-football-reference.com/years/2006/rushing.htm',
    'https://www.pro-football-reference.com/years/2007/rushing.htm',
    'https://www.pro-football-reference.com/years/2008/rushing.htm',
    'https://www.pro-football-reference.com/years/2009/rushing.htm',
    'https://www.pro-football-reference.com/years/2010/rushing.htm',
    'https://www.pro-football-reference.com/years/2011/rushing.htm',
    'https://www.pro-football-reference.com/years/2012/rushing.htm',
    'https://www.pro-football-reference.com/years/2013/rushing.htm',
    'https://www.pro-football-reference.com/years/2014/rushing.htm',
    'https://www.pro-football-reference.com/years/2015/rushing.htm',
    'https://www.pro-football-reference.com/years/2016/rushing.htm',
    'https://www.pro-football-reference.com/years/2017/rushing.htm',
    'https://www.pro-football-reference.com/years/2018/rushing.htm',
    'https://www.pro-football-reference.com/years/2019/rushing.htm',
    'https://www.pro-football-reference.com/years/2020/rushing.htm',
    'https://www.pro-football-reference.com/years/2021/rushing.htm']
seasons_passing = [
    'https://www.pro-football-reference.com/years/1990/passing.htm',
    'https://www.pro-football-reference.com/years/1991/passing.htm',
    'https://www.pro-football-reference.com/years/1992/passing.htm',
    'https://www.pro-football-reference.com/years/1993/passing.htm',
    'https://www.pro-football-reference.com/years/1994/oassing.htm',
    'https://www.pro-football-reference.com/years/1995/passing.htm',
    'https://www.pro-football-reference.com/years/1996/passing.htm',
    'https://www.pro-football-reference.com/years/1997/passing.htm',
    'https://www.pro-football-reference.com/years/1998/passing.htm',
    'https://www.pro-football-reference.com/years/1999/passing.htm',
    'https://www.pro-football-reference.com/years/2000/passing.htm',
    'https://www.pro-football-reference.com/years/2001/passing.htm',
    'https://www.pro-football-reference.com/years/2002/passing.htm',
    'https://www.pro-football-reference.com/years/2003/passing.htm',
    'https://www.pro-football-reference.com/years/2004/passing.htm',
    'https://www.pro-football-reference.com/years/2005/passing.htm',
    'https://www.pro-football-reference.com/years/2006/passing.htm',
    'https://www.pro-football-reference.com/years/2007/passing.htm',
    'https://www.pro-football-reference.com/years/2008/passing.htm',
    'https://www.pro-football-reference.com/years/2009/passing.htm',
    'https://www.pro-football-reference.com/years/2010/passing.htm',
    'https://www.pro-football-reference.com/years/2011/passing.htm',
    'https://www.pro-football-reference.com/years/2012/passing.htm',
    'https://www.pro-football-reference.com/years/2013/passing.htm',
    'https://www.pro-football-reference.com/years/2014/passing.htm',
    'https://www.pro-football-reference.com/years/2015/passing.htm',
    'https://www.pro-football-reference.com/years/2016/passing.htm',
    'https://www.pro-football-reference.com/years/2017/passing.htm',
    'https://www.pro-football-reference.com/years/2018/passing.htm',
    'https://www.pro-football-reference.com/years/2019/passing.htm',
    'https://www.pro-football-reference.com/years/2020/passing.htm',
    'https://www.pro-football-reference.com/years/2021/passing.htm']
seasons_receiving = [
    'https://www.pro-football-reference.com/years/1990/receiving.htm',
    'https://www.pro-football-reference.com/years/1991/receiving.htm',
    'https://www.pro-football-reference.com/years/1992/receiving.htm',
    'https://www.pro-football-reference.com/years/1993/receiving.htm',
    'https://www.pro-football-reference.com/years/1994/receiving.htm',
    'https://www.pro-football-reference.com/years/1995/receiving.htm',
    'https://www.pro-football-reference.com/years/1996/receiving.htm',
    'https://www.pro-football-reference.com/years/1997/receiving.htm',
    'https://www.pro-football-reference.com/years/1998/receiving.htm',
    'https://www.pro-football-reference.com/years/1999/receiving.htm',
    'https://www.pro-football-reference.com/years/2000/receiving.htm',
    'https://www.pro-football-reference.com/years/2001/receiving.htm',
    'https://www.pro-football-reference.com/years/2002/receiving.htm',
    'https://www.pro-football-reference.com/years/2003/receiving.htm',
    'https://www.pro-football-reference.com/years/2004/receiving.htm',
    'https://www.pro-football-reference.com/years/2005/receiving.htm',
    'https://www.pro-football-reference.com/years/2006/receiving.htm',
    'https://www.pro-football-reference.com/years/2007/receiving.htm',
    'https://www.pro-football-reference.com/years/2008/receiving.htm',
    'https://www.pro-football-reference.com/years/2009/receiving.htm',
    'https://www.pro-football-reference.com/years/2010/receiving.htm',
    'https://www.pro-football-reference.com/years/2011/receiving.htm',
    'https://www.pro-football-reference.com/years/2012/receiving.htm',
    'https://www.pro-football-reference.com/years/2013/receiving.htm',
    'https://www.pro-football-reference.com/years/2014/receiving.htm',
    'https://www.pro-football-reference.com/years/2015/receiving.htm',
    'https://www.pro-football-reference.com/years/2016/receiving.htm',
    'https://www.pro-football-reference.com/years/2017/receiving.htm',
    'https://www.pro-football-reference.com/years/2018/receiving.htm',
    'https://www.pro-football-reference.com/years/2019/receiving.htm',
    'https://www.pro-football-reference.com/years/2020/receiving.htm',
    'https://www.pro-football-reference.com/years/2021/receiving.htm']
base_year = 1990
year_index = int(year) - base_year
if stat_type == 'rushing':
    url = seasons_rushing[year_index]
elif stat_type == 'receiving':
    url = seasons_receiving[year_index]
else:
    url = seasons_passing[year_index]
html = urlopen(url)
stats_page = BeautifulSoup(html)
if stat_type == 'rushing':
    col = stats_page.findAll('tr')[1]
    col = [i.getText() for i in col.findAll('th')]
    rows = stats_page.findAll('tr')[2:]
else:
    col = stats_page.findAll('tr')[0]
    col = [i.getText() for i in col.findAll('th')]
    rows = stats_page.findAll('tr')[1:]
stats = []
for i in range(len(rows)):
    stats.append([col.getText() for col in rows[i].findAll('td')])
data = pd.DataFrame(stats, columns=col[1:])
if stat_type == 'rushing':
    categories = ['Age', 'Att', 'Yds', 'TD']
elif stat_type == 'receiving':
    categories = ['Age', 'Rec', 'Yds', 'TD']
else:
    categories = ['Age', 'Yds', 'TD', 'Int']

data_compressed = data[['Player', 'Tm'] + categories]
for i in categories:
    data_compressed[i] = pd.to_numeric(data[i])
if stat_type == 'rushing':
    if category == 'Att':
        df = data_compressed.sort_values(by=['Att'], ascending=False)
    elif category == 'Yds':
        df = data_compressed.sort_values(by=['Yds'], ascending=False)
    else:
        df = data_compressed.sort_values(by=['TD'], ascending=False)
elif stat_type == 'passing':
    if category == 'Yds':
        df = data_compressed.sort_values(by=['Yds'], ascending=False)
    elif category == 'TD':
        df = data_compressed.sort_values(by=['TD'], ascending=False)
    else:
        df = data_compressed.sort_values(by=['Int'], ascending=False)
else:
    if category == 'Rec':
        df = data_compressed.sort_values(by=['Rec'], ascending=False)
    elif category == 'Yds':
        df = data_compressed.sort_values(by=['Yds'], ascending=False)
    else:
        df = data_compressed.sort_values(by=['TD'], ascending=False)
s = df['Age']
s20 = islice(s, 20)
s20 = [int(x) for x in s20]
avg_age = statistics.mean(s20)
median = statistics.median(s20)
st_dev = statistics.stdev(s20, None)

if stat_type == 'rushing':
    if category == 'Att':
        print("The average age of the top twenty rushing attempts leaders in " + str(year) + " was " + str(avg_age))
        print("The standard deviation is " + str(st_dev))
        print("The median is " + str(median))
    elif category == 'Yds':
        print("The average age of the top twenty rushing yards leaders in " + str(year) + " was " + str(avg_age))
        print("The standard deviation is " + str(st_dev))
        print("The median is " + str(median))
    else:
        print("The average age of the top twenty rushing touchdown leaders in " + str(year) + " was " + str(avg_age))
        print("The standard deviation is " + str(st_dev))
        print("The median is " + str(median))
elif stat_type == 'passing':
    if category == 'Yds':
        print("The average age of the top twenty passing yards leaders in " + str(year) + " was " + str(avg_age))
        print("The standard deviation is " + str(st_dev))
        print("The median is " + str(median))
    elif category == 'TD':
        print("The average age of the top twenty passing touchdown leaders in " + str(year) + " was " + str(avg_age))
        print("The standard deviation is " + str(st_dev))
        print("The median is " + str(median))
    else:
        print("The average age of the top twenty interception leaders in " + str(year) + " was " + str(avg_age))
        print("The standard deviation is " + str(st_dev))
        print("The median is " + str(median))
else:
    if category == 'Rec':
        print("The average age of the top twenty reception leaders in " + str(year) + " was " + str(avg_age))
        print("The standard deviation is " + str(st_dev))
        print("The median is " + str(median))
    elif category == 'Yds':
        print("The average age of the top twenty receiving yards leaders in " + str(year) + " was " + str(avg_age))
        print("The standard deviation is " + str(st_dev))
        print("The median is " + str(median))
    else:
        print("The average age of the top twenty receiving touchdown leaders in " + str(year) + " was " + str(avg_age))
        print("The standard deviation is " + str(st_dev))
        print("The median is " + str(median))
