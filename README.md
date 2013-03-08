heroku-flask-rq-worker
======================

This is just to show how to retrieve the queue and wait until the job is finished from JavaScript.


First install everything you need by doing this command. You might want to install redis as well if you haven't done it already.
You can follow the steps from this. https://devcenter.heroku.com/articles/python-rq


```
pip install -r requirements.txt
```

Run worker in one window. This will be our worker to fetch the job from RQ and process it.

```
python worker.py
```

Then start up the app
```
python app.py
```

Then go to http://localhost:5000 and type something in the textbox, if you have firebug open you can see the requests coming back as 202 and then after the job is done it'll be 200

