heroku-flask-rq-worker
======================

* **How**

1. 

```
pip install -r requirements.txt
```

2. Run worker in one window. This will be our worker to fetch the job from RQ and process it.

```
python worker.py
```

3. Then start up the app
```
python app.py
```

4. Then go to http://localhost:5000 and type something in the textbox, if you have firebug open you can see the requests coming back as 202 and then after the job is done it'll be 200

