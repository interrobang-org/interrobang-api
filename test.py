import requests
from bs4 import BeautifulSoup
import mechanicalsoup

url = "https://www.bloomberg.com/news/articles/2019-03-02/square-inc-co-founder-tristan-o-tierney-dies-at-35"
# url = "https://httpbin.org/get"
# browser = mechanicalsoup.Browser()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
html = requests.get(url,headers=headers).content
# html = browser.get(url).soup()
# print(html)

# browser = mechanicalsoup.StatefulBrowser()
# r = browser.open(url)
# print(r.content)
# html = str(browser.get_current_page())
# print(type(html))
soup = BeautifulSoup(html)

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out
# print(soup)
# get text
text = soup.get_text()
# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)
# print(len(text))
print(text)