from flask import Flask
from redis import Redis
import os
app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return ('Welcome to my app on Docker, served by {}! ' 'There were {} visitors on this page.'
             .format(os.environ['HOSTNAME'], redis.get('hits')))

if __name__== "__main__":
    app.run(host="0.0.0.0", debug=True)



