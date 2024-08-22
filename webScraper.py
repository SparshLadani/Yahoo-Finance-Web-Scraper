from bs4 import BeautifulSoup
import csv
import requests
import time
from datetime import date
import emailing

urls = ["https://finance.yahoo.com/quote/GOOGL?p=GOOGL&.tsrc=fin-srch", "https://finance.yahoo.com/quote/AMZN/", "https://finance.yahoo.com/quote/MSFT/", "https://finance.yahoo.com/quote/CTSH/"]
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
file_name = "StockPrice" + str(date.today()) + ".csv"
csv_file = open(file_name, "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Stock Name', 'Current Price', 'Previous Close', 'Open', 'Bid', 'Ask', 'Day Range', '52 Week Range', 'Volume', 'Avg. Volume', 'Martket Cap (intraday)', 'Beta (5Y Monthly)', 'PE Ratio (TTM)', 'EPS (TTM)', 'Earnings Date', 'Forward Dividend & Yield', 'Ex-Dividend Date', '1y Target Est'])

for url in urls:
    stock = []
    html_page = requests.get(url, headers=headers)

    soup = BeautifulSoup(html_page.content, 'lxml')

    stock_title = soup.find_all("div", class_="top yf-ezk9pj")[0].find("h1").get_text()
    current_price = soup.find_all("div", class_="bottom yf-ezk9pj")[0].find("span").get_text()

    stock.append(stock_title)
    stock.append(current_price)

    ul_information = soup.find("ul", class_="yf-tx3nkj").find_all("li")
    length = ul_information.__len__()

    print("Company:",stock_title, "\n")
    print("Current Price:",current_price, "\n")


    for i in range(0,length):

        value = ul_information[i].find_all("span")[1].get_text()
        stock.append(value)

        print(value)
        print()
    
    csv_writer.writerow(stock)
    time.sleep(5)

csv_file.close()
emailing.send(filename=file_name)