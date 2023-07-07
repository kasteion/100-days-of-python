import os
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCKS_APIKEY = os.environ.get("ALPHAVANTAGE_APIKEY")
NEWS_APIKEY = os.environ.get("NEWS_APIKEY")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN")
TWILIO_PHONE = os.environ.get("TWILIO_PHONE")
PHONE = os.environ.get("PHONE")


def get_stock_data():
    parameters = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK,
        "apikey": STOCKS_APIKEY,
    }
    response = requests.get("https://www.alphavantage.co/query", params=parameters)
    response.raise_for_status()
    data = [v for v in response.json()["Time Series (Daily)"].values()]
    open_price = float(data[0]["4. close"])
    close_price = float(data[1]["4. close"])

    if open_price >= close_price:
        icon = "🔺"
    else:
        icon = "🔻"

    percentage_diff = round((abs(open_price - close_price) / ((open_price + close_price) / 2)) * 100)

    return {
        "icon": icon,
        "percentage_diff": percentage_diff,
    }


def get_relevant_news():
    parameters = {
        "q": COMPANY_NAME,
        "from": "2023-05-06",
        "sortBy": "relevancy",
        "apiKey": NEWS_APIKEY,
    }
    response = requests.get("https://newsapi.org/v2/everything", params=parameters)
    response.raise_for_status()
    news = response.json()["articles"][:3]
    return news

def send_message(client, article):
    # Optional: Format the SMS message like this:
    # """
    # TSLA: 🔺2%
    # Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
    # Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    # or
    # "TSLA: 🔻5%
    # Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
    # Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    # """
    # headline = news["title"]
    # brief = a["description"]
    message = client.messages.create(
        body=f"{STOCK}: {article['icon']} {article['percentage_diff']}%\nHeadline: {article['headline']}\n"
             f"Brief: {article['brief']}",
        from_=TWILIO_PHONE,
        to=PHONE,
    )


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_data = get_stock_data()
if stock_data["percentage_diff"] >= 1:
    # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    # https://newsapi.org/v2/everything?q=tesla&from=2023-05-06&sortBy=relevancy&apiKey=API_KEY
    news = get_relevant_news()
    client = Client(TWILIO_SID, TWILIO_TOKEN)
    for n in news:
        # STEP 3: Use https://www.twilio.com
        # Send a separate message with the percentage change and each article's title and description
        # to your phone number.
        article = {
            "icon": stock_data["icon"],
            "percentage_diff": stock_data["percentage_diff"],
            "headline": n["title"],
            "brief": n["description"]
        }
        send_message(client, article)



