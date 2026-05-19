## Automated Alert Script

This minimal automation fetches the latest S&P 500 futures news and sends an email alert.

```python
import requests, smtplib, os

def fetch_news():
    url = "https://newsapi.org/v2/everything?q=\"S&P+500+futures\"&apiKey=YOUR_NEWSAPI_KEY"
    resp = requests.get(url)
    data = resp.json()
    return data.get('articles', [])[:1]

def send_email(article):
    sender = os.getenv('ALERT_SENDER')
    recipient = os.getenv('ALERT_RECIPIENT')
    subject = f"Alert: {article['title']}"
    body = f"{article['description']}\n\nRead more: {article['url']}"
    message = f"Subject: {subject}\n\n{body}"
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender, os.getenv('ALERT_PASSWORD'))
        server.sendmail(sender, recipient, message)

if __name__ == "__main__":
    articles = fetch_news()
    if articles:
        send_email(articles[0])
```