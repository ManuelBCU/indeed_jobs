import scraperwiki
import lxml.html
html = scraperwiki.scrape("https://www.indeed.co.uk/restaurant-jobs-in-England")
root = lxml.html.fromstring(html)
matchedlinks =root.cssselect("table tbody td div a")
for li in matchedlinks:
  #Store the text contents of li in a new variable listtext
  listtext = li.text_content()
  #print that
  print(listtext)
  
