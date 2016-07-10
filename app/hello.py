#!flask/bin/python
from flask import render_template
from flask import Flask
from flask import jsonify
import psycopg2
import psycopg2.extras
import os
import logging

logging.basicConfig(filename='./log/twetter_ws.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s]: %(message)s')

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')
    
@app.route('/tesla_tweets')
def tesla_tweets():
    conn = get_db_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    query_str = """
        SELECT created_at, 
            tweet AS text, 
            label_s AS positive,
            pred_s AS predict,
            pred_p AS predict_prob
        FROM tweets
        ORDER BY created_at DESC
        LIMIT 1000
    """
    try:
        cur.execute(query_str)
    except:
        logging.info("Error executing select")
    result = {'tweets': cur.fetchall()}
    return jsonify(**result)

@app.route('/tesla_tweets/count')
def tesla_count():
    conn = get_db_conn()
    cur = conn.cursor()
    try:
        cur.execute('select count(*) from tweets')
    except:
        logging.info("Error executing select")
    result = cur.fetchall()
    return render_template('tweets_count.html', counts=result)

def get_db_conn():
    # Getting database connection
    db_host = os.getenv('DB_HOST', "192.168.99.100")
    db_port = os.getenv('DB_PORT', "5435")
    db_user = os.getenv('DB_USER', "postgres")
    db_name = os.getenv('DB_NAME', "twitter_tesla")
    db_pass = os.getenv('DB_PASS', "password")
    
    try:
        return psycopg2.connect(
            dbname=db_name,
            user=db_user,
            host=db_host,
            port=db_port,
            password=db_pass)
            
    except Exception as e:
        print "I am unable to connect to the database"
        print str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
