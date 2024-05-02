import requests
import config

# api key
api_key = config.api_key
url = f"https://newsapi.org/v2/everything?q=apple&from=2024-05-01&to=2024-05-01&sortBy=popularity&apiKey={api_key}"

# make request
request = requests.get(url)

# getting content using a dictionary with data
content = request.json()

# accessing article and or descriptions
for article in content['articles']:
    print(article['title'])
    print()
    print(article['description'])
