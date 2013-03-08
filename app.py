import os
import sys, logging
import json
from flask import Flask
from flask import render_template
from flask import request

from rq import Queue
from rq.job import Job
from rq import get_current_job
from worker import conn

from lib.word_counter import WordCounter

q = Queue(connection=conn)
app = Flask(__name__)
word_counter = WordCounter()

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/get_word_count', methods=['POST'])
def get_word_count():
    data_json = json.loads(request.data)
    job = q.enqueue(word_counter.count_words, data_json["sentence"])
    return job.key

@app.route("/get_word_count_result/<job_key>", methods=['GET'])
def get_word_count_result(job_key):
    job_key = job_key.replace("rq:job:", "")
    job = Job.fetch(job_key, connection=conn)

    if(not job.is_finished):
        return "Not yet", 202
    else:
        return str(job.result), 200

if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
