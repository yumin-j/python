import bs4
import requests

# https://finance.naver.com/marketindex/이 주소를 통해 환율이 얼마인지 가져오는 프로그램 작성
html = requests.get('https://finance.naver.com/marketindex/')
soup = bs4. BeautifulSoup(html.text, 'html.parser')
dollar = soup.select_one('#exchangeList > li:nth-child(1) > a.head.usd > div > span.value')

print(dollar.text)
