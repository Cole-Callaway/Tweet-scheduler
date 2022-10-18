from os import environ
from flask import Flask, render_template, request, redirect
from datetime import datetime, timedelta
import gspread
from dotenv import load_dotenv
app = Flask(__name__)

gc = gspread.service_account(filename='tweet-scheduler-sheet-fc9a11fd5e29.json')

sh = gc.open_by_key('1dkipGqPO1ZQPIQKd6zd-UXiU10f0QGGEPX7pZ4kHam0')
worksheet = sh.sheet1

load_dotenv()

PASSWORD = environ['PASSWORD']

class Tweet:
    def __init__(self, message, time, done, row_idx):
        self.message = message
        self.time = time
        self.done = done
        self.row_idx = row_idx
def get_date_time(date_time_str):
    date_time_obj = None
    error_code = None
    try:
        date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
    except ValueError as e:
        error_code = f'Error {e}'
    
    if date_time_obj is not None:
        now_time_mst = datetime.utcnow() + timedelta(hours=-6)
        
        if not date_time_obj >= now_time_mst:
            error_code ="Error! time must be in the future"
    return date_time_obj, error_code


@app.route('/')
def tweet_list():
    tweet_records = worksheet.get_all_records()
    tweets = []
    for idx, tweet in enumerate(tweet_records, start=2):
        tweet = Tweet(**tweet, row_idx=idx)
        tweets.append(tweet)
    tweets.reverse()
    n_open_tweets = sum(1 for tweet in tweets if not tweet.done)
    return render_template('base.html', tweets=tweets, n_open_tweets=n_open_tweets)


@app.route('/tweet', methods=['POST'])
def add_tweet():
    message = request.form['message']
    if not message:
        return 'ERROR! No message'
    time = request.form['time']
    if not time:
        return 'ERROR! No time added'
    pw = request.form['pw']
    if not pw or pw != PASSWORD:
        return 'ERROR! wrong password'
    
    if len(message) > 280:
        return 'ERROR! message to long'
    
    date_time_obj, error_code = get_date_time(time)
    if error_code is not None: 
        return error_code
    
    tweet = [str(date_time_obj), message, 0] 
    worksheet.append_row(tweet)
    return redirect('/')

@app.route('/delete/<int:row_idx>')
def delete_tweet(row_idx):
    worksheet.delete_rows(row_idx)
    return redirect('/')