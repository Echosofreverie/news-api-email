import requests

api_key = "7......"  #去https://newsapi.org/登录使用自己的API
url = ("https://newsapi.org/v2/everything?q=tesla&"\
       "from=2025-02-18&sortBy=publishedAt&apiKey="\
       "7......")
# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Get a list of articles
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
