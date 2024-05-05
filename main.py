import requests
import config
from email_server import send_email_script

# api key
api_key = config.api_key
url = f'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={api_key}'


# make request
request = requests.get(url)

# getting content using a dictionary with data
content = request.json()
# accessing article and or descriptions
body = ''
for article in content['articles']:
    if article['description'] is not None:
        body = body + article['title'] + "\n" + article['description'] + 2*"\n"

body = body.encode('utf-8')
send_email_script(message=body)