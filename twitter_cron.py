from application_only_auth import Client

#cred file

with open('twitter.cred') as f:
    CONSUMER_KEY = f.readline().strip()
    CONSUMER_SECRET = f.readline().strip()

client = Client(CONSUMER_KEY, CONSUMER_SECRET)

url = "https://api.twitter.com/1.1/search/tweets.json?"

client.request(url)

# returns a tuple of high, low, mean of price
def get_price(query):
    query_url = url + query
    result =  client.request(query_url)
    
