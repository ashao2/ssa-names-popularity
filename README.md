# ssa-names-popularity
ssa_scrape.py is a Python script for scraping baby name data from the Social Security Administration, accessible via https://www.ssa.gov/OACT/babynames/index.html or https://www.ssa.gov/cgi-bin/popularnames.cgi.

Users can specify _n_, the number of top names they want (1-1000). This means _n_ names will be retrieved for both males and females each.

One can also specify the year range of interest with _s_, the starting year, and _e_, the ending year. Currently, the maximum range possible is 1880-2020.

The results will be written to a csv file with the columns _year, gender, rank, name, percent_. Please note that _percent_ refers to the percent of births in a year with the name in question for one gender. Thus, if in 2020 the percent given for the name Emily is 0.5%, this means 0.5% of girls (not babies overall) were named Emily.

A csv file called babynames1880-2020.csv is provided with the top 100 per year from 1880 to 2020.

BeautifulSoup is needed to run this script.
