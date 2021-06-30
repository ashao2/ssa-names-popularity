# ssa-names-popularity

scrape_by_year.py and scrape_by_name.py are Python scripts for scraping baby name data from the Social Security Administration, accessible [here](https://www.ssa.gov/OACT/babynames/index.html) or [here](https://www.ssa.gov/cgi-bin/popularnames.cgi).

Using the top 5 names (for each gender) from 2000-2010, here is an example of the data provided by the output of scrape_by_year.py:

| year | gender | rank | name | percent |
| ---  | ---    | ---  | ---  | ---     |
| 2000 | Male | 1 | Jacob | 1.6516 |
| 2000 | Female | 1 | Emily | 1.3009 |
| 2000 | Male | 2 | Michael | 1.5345 |
| 2000 | Female | 2 | Hannah | 1.1569 |
| 2000 | Male | 3 | Matthew | 1.3685 |
| 2000 | Female | 3 | Madison | 1.0007 |
| 2000 | Male | 4 | Joshua | 1.3189 |
| 2000 | Female | 4 | Ashley | 0.9020 |
| 2000 | Male | 5 | Christopher | 1.1942 |
| 2000 | Female | 5 | Sarah | 0.8874 |
| 2001 | Male | 1 | Jacob | 1.5742 |
| 2001 | Female | 1 | Emily | 1.2652 |
| 2001 | Male | 2 | Michael | 1.4355 |
| 2001 | Female | 2 | Madison | 1.1192 |
| 2001 | Male | 3 | Matthew | 1.2965 |
| 2001 | Female | 3 | Hannah | 1.0462 |
| 2001 | Male | 4 | Joshua | 1.2583 |
| 2001 | Female | 4 | Ashley | 0.8345 |
| 2001 | Male | 5 | Christopher | 1.1185 |
| 2001 | Female | 5 | Alexis | 0.8282 |
| 2002 | Male | 1 | Jacob | 1.4800 |
| 2002 | Female | 1 | Emily | 1.2391 |
| 2002 | Male | 2 | Michael | 1.3674 |
| 2002 | Female | 2 | Madison | 1.1027 |
| 2002 | Male | 3 | Joshua | 1.2582 |
| 2002 | Female | 3 | Hannah | 0.9533 |
| 2002 | Male | 4 | Matthew | 1.2174 |
| 2002 | Female | 4 | Emma | 0.8380 |
| 2002 | Male | 5 | Ethan | 1.0702 |
| 2002 | Female | 5 | Alexis | 0.7919 |
| 2003 | Male | 1 | Jacob | 1.4111 |
| 2003 | Female | 1 | Emily | 1.2807 |
| 2003 | Male | 2 | Michael | 1.2912 |
| 2003 | Female | 2 | Emma | 1.1320 |
| 2003 | Male | 3 | Joshua | 1.1948 |
| 2003 | Female | 3 | Madison | 1.0069 |
| 2003 | Male | 4 | Matthew | 1.1428 |
| 2003 | Female | 4 | Hannah | 0.8792 |
| 2003 | Male | 5 | Andrew | 1.0546 |
| 2003 | Female | 5 | Olivia | 0.8052 |
| 2004 | Male | 1 | Jacob | 1.3199 |
| 2004 | Female | 1 | Emily | 1.2412 |
| 2004 | Male | 2 | Michael | 1.2051 |
| 2004 | Female | 2 | Emma | 1.0713 |
| 2004 | Male | 3 | Joshua | 1.1457 |
| 2004 | Female | 3 | Madison | 1.0225 |
| 2004 | Male | 4 | Matthew | 1.0828 |
| 2004 | Female | 4 | Olivia | 0.7984 |
| 2004 | Male | 5 | Ethan | 1.0511 |
| 2004 | Female | 5 | Hannah | 0.7737 |
| 2005 | Male | 1 | Jacob | 1.2149 |
| 2005 | Female | 1 | Emily | 1.1801 |
| 2005 | Male | 2 | Michael | 1.1200 |
| 2005 | Female | 2 | Emma | 1.0029 |
| 2005 | Male | 3 | Joshua | 1.0937 |
| 2005 | Female | 3 | Madison | 0.9646 |
| 2005 | Male | 4 | Matthew | 1.0095 |
| 2005 | Female | 4 | Abigail | 0.7763 |
| 2005 | Male | 5 | Ethan | 1.0022 |
| 2005 | Female | 5 | Olivia | 0.7735 |
| 2006 | Male | 1 | Jacob | 1.1339 |
| 2006 | Female | 1 | Emily | 1.0245 |
| 2006 | Male | 2 | Michael | 1.0330 |
| 2006 | Female | 2 | Emma | 0.9149 |
| 2006 | Male | 3 | Joshua | 1.0187 |
| 2006 | Female | 3 | Madison | 0.8914 |
| 2006 | Male | 4 | Ethan | 0.9362 |
| 2006 | Female | 4 | Isabella | 0.8722 |
| 2006 | Male | 5 | Matthew | 0.9277 |
| 2006 | Female | 5 | Ava | 0.8106 |
| 2007 | Male | 1 | Jacob | 1.0970 |
| 2007 | Female | 1 | Emily | 0.9150 |
| 2007 | Male | 2 | Michael | 0.9938 |
| 2007 | Female | 2 | Isabella | 0.9047 |
| 2007 | Male | 3 | Ethan | 0.9498 |
| 2007 | Female | 3 | Emma | 0.8686 |
| 2007 | Male | 4 | Joshua | 0.9329 |
| 2007 | Female | 4 | Ava | 0.8532 |
| 2007 | Male | 5 | Daniel | 0.9147 |
| 2007 | Female | 5 | Madison | 0.8490 |
| 2008 | Male | 1 | Jacob | 1.0371 |
| 2008 | Female | 1 | Emma | 0.9038 |
| 2008 | Male | 2 | Michael | 0.9467 |
| 2008 | Female | 2 | Isabella | 0.8944 |
| 2008 | Male | 3 | Ethan | 0.9276 |
| 2008 | Female | 3 | Emily | 0.8375 |
| 2008 | Male | 4 | Joshua | 0.8816 |
| 2008 | Female | 4 | Olivia | 0.8206 |
| 2008 | Male | 5 | Daniel | 0.8723 |
| 2008 | Female | 5 | Ava | 0.8186 |
| 2009 | Male | 1 | Jacob | 0.9992 |
| 2009 | Female | 1 | Isabella | 1.1023 |
| 2009 | Male | 2 | Ethan | 0.9362 |
| 2009 | Female | 2 | Emma | 0.8846 |
| 2009 | Male | 3 | Michael | 0.8938 |
| 2009 | Female | 3 | Olivia | 0.8615 |
| 2009 | Male | 4 | Alexander | 0.8603 |
| 2009 | Female | 4 | Sophia | 0.8373 |
| 2009 | Male | 5 | William | 0.8455 |
| 2009 | Female | 5 | Ava | 0.7842 |
| 2010 | Male | 1 | Jacob | 1.0782 |
| 2010 | Female | 1 | Isabella | 1.1698 |
| 2010 | Male | 2 | Ethan | 0.8769 |
| 2010 | Female | 2 | Sophia | 1.0536 |
| 2010 | Male | 3 | Michael | 0.8455 |
| 2010 | Female | 3 | Emma | 0.8854 |
| 2010 | Male | 4 | Jayden | 0.8371 |
| 2010 | Female | 4 | Olivia | 0.8690 |
| 2010 | Male | 5 | William | 0.8307 |
| 2010 | Female | 5 | Ava | 0.7877 |

Here is the result of the data above after using convert_year_name.py, which can also be obtained by using scrape_by_name.py:

 |name | 2000 | 2001 | 2002 | 2003 | 2004 | 2005 | 2006 | 2007 | 2008 | 2009 | 2010 |
 | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
 |Jacob | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
 |Emily | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 3 |  |  |
 |Michael | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 |
 |Hannah | 2 | 3 | 3 | 4 | 5 |  |  |  |  |  |  |
 |Matthew | 3 | 3 | 4 | 4 | 4 | 4 | 5 |  |  |  |  |
 |Madison | 3 | 2 | 2 | 3 | 3 | 3 | 3 | 5 |  |  |  |
 |Joshua | 4 | 4 | 3 | 3 | 3 | 3 | 3 | 4 | 4 |  |  |
 |Ashley | 4 | 4 |  |  |  |  |  |  |  |  |  |
 |Christopher | 5 | 5 |  |  |  |  |  |  |  |  |  |
 |Sarah | 5 |  |  |  |  |  |  |  |  |  |  |
 |Alexis |  | 5 | 5 |  |  |  |  |  |  |  |  |
 |Emma |  |  | 4 | 2 | 2 | 2 | 2 | 3 | 1 | 2 | 3 |
 |Ethan |  |  | 5 |  | 5 | 5 | 4 | 3 | 3 | 2 | 2 |
 |Andrew |  |  |  | 5 |  |  |  |  |  |  |  |
 |Olivia |  |  |  | 5 | 4 | 5 |  |  | 4 | 3 | 4 |
 |Abigail |  |  |  |  |  | 4 |  |  |  |  |  |
 |Isabella |  |  |  |  |  |  | 4 | 2 | 2 | 1 | 1 |
 |Ava |  |  |  |  |  |  | 5 | 4 | 5 | 5 | 5 |
 |Daniel |  |  |  |  |  |  |  | 5 | 5 |  |  |
 |Alexander |  |  |  |  |  |  |  |  |  | 4 |  |
 |Sophia |  |  |  |  |  |  |  |  |  | 4 | 2 |
 |William |  |  |  |  |  |  |  |  |  | 5 | 5 |
 |Jayden |  |  |  |  |  |  |  |  |  |  | 4 |

This code is based on the script by [swupnil](https://github.com/swupnil/2014-ssa-scraper/blob/master/ssa_scraper.py). I also consulted materials from [That1Guy](https://stackoverflow.com/questions/17220997/a-presumably-basic-web-scraping-of-http-www-ssa-gov-cgi-bin-popularnames-cgi/17221642) and [Johnathan Soma](http://jonathansoma.com/lede/foundations/classes/friday%20sessions/advanced-scraping-form-submissions-completed/) along the way.

For scrape_by_year.py and scrape_by_name.py, users can use the flag _-n_ to specify the number of top names they want (1-1000). This means that number of names will be retrieved for both males and females each.

Users can also specify the year range of interest with _-s_ for the starting year and _-e_ for the ending year. Currently, the maximum range possible is 1880-2020.

For scrape_by_year.py, the results will be written to a CSV file with the columns _year, gender, rank, name, percent_. Please note that _percent_ refers to the percent of births in a year with the name in question for one gender. Thus, if in 2020 the percent given for the name Emily is 0.5%, this means 0.5% of girls (not babies overall) were named Emily.

For scrape_by_name.py, the results will be written to a CSV file with the columns _name, year1,...,yearn_.

convert_year_name.py requires the flag _-f_ for the file path of the a CSV file in the by-years format.

Two CSV files called _byname1880-2020.csv_ and _byyear1880-2020_ are provided with the top 100 male & female names per year from 1880 to 2020.

BeautifulSoup and Numpy are needed to run these scripts.
