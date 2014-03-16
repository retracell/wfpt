from application_only_auth import Client
import nltk

#cred file

with open('twitter.cred') as f:
    CONSUMER_KEY = f.readline().strip()
    CONSUMER_SECRET = f.readline().strip()

client = Client(CONSUMER_KEY, CONSUMER_SECRET)

url = "https://api.twitter.com/1.1/search/tweets.json?q="

# returns a tuple of high, mean, low of price
def get_price(args):
    query = url + args
    query = query.replace(' ', '%20')
    tweets =  client.request(query)
    statuses = tweets['statuses']
    tokenized_texts = [nltk.word_tokenize(status['text']) for status in statuses]
    tagged_texts = [nltk.pos_tag(text) for text in tokenized_texts]
    high = 0
    low = 0
    sum = 0
    count = 0
    for tagged_text in tagged_texts:
        for index, (token, tag) in enumerate(tagged_text):
            # Look for cardinal numbers and avoid retweets
            if tag == 'CD' and tagged_text[0][0] != 'RT':
                # Avoid a in "a dollar to b dollar" and "a to b dollar"
                if index != len(tagged_text) - 1 and tagged_text[index+1][1] != 'TO' \
                    and index != len(tagged_text) - 2 and tagged_text[index+2][1] != 'TO':
                    if float(token) > high:
                        high = float(token)
                    if float(token) < low:
                        low = float(token)
                    sum += float(token)
                    count += 1
    mean = sum/count
    print mean
    return (high, mean, low)

if __name__ == '__main__':
    get_price("bread lira")
