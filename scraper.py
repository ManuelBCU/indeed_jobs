import scraperwiki
import lxml.html
html = scraperwiki.scrape("https://www.indeed.co.uk/restaurant-jobs-in-England")
root = lxml.html.fromstring(html)
matchedlinks =root.cssselect(" td div summary")
for li in matchedlinks:
  #Store the text contents of li in a new variable listtext
  listtext = li.text_content()
  #print that
  print(listtext)
  
