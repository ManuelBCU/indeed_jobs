import scraperwiki
import lxml.html
html = scraperwiki.scrape("https://www.indeed.co.uk/restaurant-jobs-in-England")
root = lxml.html.fromstring(html)
root.cssselect("div a title")
