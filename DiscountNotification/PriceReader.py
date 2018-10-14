from bs4 import BeautifulSoup
import urllib.request

def removeComma(s):
	s = s.split(",")
	return "".join(s)

x = urllib.request.urlopen('https://www.amazon.in/dp/B07GVMTWWX/ref=cm_sw_r_cp_ep_dp_YUKWBbV1ZQ1KW')
soup =BeautifulSoup(x,'html.parser')
a = soup.find('span',id='priceblock_dealprice')
price=a.text
price = (removeComma(price))
price=float(price)
print(price)