#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, render_template
from song_search import song_search

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    song_title = request.args.get('song_title')
    position = song_search(song_title)

    if position == -1:
        result = f"The song '{song_title}' was not found in the chart."
    else:
        result = f"The song '{song_title}' is ranked #{position} in the chart."

    return render_template('search.html', result=result)

if __name__ == '__main__':
    app.run(port=8000)

