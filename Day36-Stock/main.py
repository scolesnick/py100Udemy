import smtplib
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_URL = 'https://www.alphavantage.co/query'
ALPHA_KEY = ''
ALPHA_PARAMS = {
    'function':'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey':ALPHA_KEY
}
NEWS_URL = 'https://newsapi.org/v2/everything'
NEWS_KEY = ''
NEWS_PARAMS = {
    'apiKey':NEWS_KEY,
    'q':COMPANY_NAME
}
PERCENT_THRESHOLD = 5.0
APP_EMAIL = ''
APP_PSW = ''
TARGET_EMAIL = ''

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get the data from the API
# response = requests.get(url=ALPHA_URL, params=ALPHA_PARAMS)
# response.raise_for_status()
# data = response.json()

# Grab open price from yesterday and the day before yesterday
# listed_data = list(data['Time Series (Daily)'].items())
# yesterday_data = listed_data[1][1]
# before_data = listed_data[2][1]

# Get percent change between the two days
# yesterday_open = float(yesterday_data['1. open'])
# before_open = float(before_data['1. open'])

# Daily limit on Alpha API is 25 calls - Including hard coded values for testing
yesterday_open = 244.48
before_open = 247.55

change = (yesterday_open / before_open)*100 - 100
# print(f'The last two opens were ${yesterday_open} and ${before_open}. The percent change was {change:.2f}%')

# Print 'Get News' if difference is above threshold
above_threshold = False
if abs(change) >= PERCENT_THRESHOLD:
    above_threshold = True

if above_threshold:

    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_response = requests.get(url=NEWS_URL, params=NEWS_PARAMS)
    news_data = news_response.json()

    # Get first 3 articles
    all_articles = news_data['articles']
    top_news = all_articles[:3]
    # for news in top_news:
    #     print(news)

    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    ## Sending message to email rather than phone number
    def send_quote(message):
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=APP_EMAIL, password=APP_PSW)
            connection.sendmail(
                from_addr=APP_EMAIL,
                to_addrs=TARGET_EMAIL,
                msg=f'Subject:{COMPANY_NAME} ({STOCK}) News Update \n\n{message}'.encode('utf-8')
            )
    msg = ''
    if change > 0:
        msg = f'{STOCK}: 🔺{change:.2f}%\n\n'
    else:
        msg = f'{STOCK}: 🔻{abs(change):.2f}%\n\n'
    for article in top_news:
        headline = article['title']
        body = article['description']
        url = article['url']
        msg = msg + f'Headline: {headline}\nBrief: {body}\nUrl: {url}\n\n'
    send_quote(msg)
    #Optional: Format the SMS message like this:
    """
    TSLA: 🔺2%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    or
    "TSLA: 🔻5%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    """

