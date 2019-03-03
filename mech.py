import mechanicalsoup

url = "https://www.bloomberg.com/news/articles/2019-03-02/square-inc-co-founder-tristan-o-tierney-dies-at-35"

# Create a browser object
# browser = mechanicalsoup.Browser()
browser = mechanicalsoup.StatefulBrowser()
r = browser.open(url)
curr_page = browser.get_current_page()
print(type(r))
print(curr_page)
