import scraperwiki
import lxml.html
html = scraperwiki.scrape("https://www.indeed.co.uk/restaurant-jobs-in-England")
root = lxml.html.fromstring(html)
matchedlinks =root.cssselect("td div a title")
print (matchedlinks)
