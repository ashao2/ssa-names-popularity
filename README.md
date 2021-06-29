# ssa-names-popularity
ssa_scrape.py is a Python script for scraping baby name data from the Social Security Administration, accessible [here](https://www.ssa.gov/OACT/babynames/index.html) or [here](https://www.ssa.gov/cgi-bin/popularnames.cgi).

This code is based on the script by [swupnil](https://github.com/swupnil/2014-ssa-scraper/blob/master/ssa_scraper.py). I also consulted materials from [That1Guy](https://stackoverflow.com/questions/17220997/a-presumably-basic-web-scraping-of-http-www-ssa-gov-cgi-bin-popularnames-cgi/17221642) and [Johnathan Soma](http://jonathansoma.com/lede/foundations/classes/friday%20sessions/advanced-scraping-form-submissions-completed/) along the way.

Users can specify _n_, the number of top names they want (1-1000). This means _n_ names will be retrieved for both males and females each.

Users can also specify the year range of interest with _s_, the starting year, and _e_, the ending year. Currently, the maximum range possible is 1880-2020.

The results will be written to a csv file with the columns _year, gender, rank, name, percent_. Please note that _percent_ refers to the percent of births in a year with the name in question for one gender. Thus, if in 2020 the percent given for the name Emily is 0.5%, this means 0.5% of girls (not babies overall) were named Emily.

A csv file called _babynames1880-2020.csv_ is provided with the top 100 per year from 1880 to 2020.

BeautifulSoup is needed to run this script.
