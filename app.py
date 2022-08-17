from flask import Flask
from flask import render_template
from flask import request
from rss.Feed import *

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return showResults(request.form['url'])
    else:
        return render_template('index.html')

def showResults(url=None):
    feed = Feed(url)
    title = feed.getTitle()
    description = feed.getDescription()
    published = feed.getPublished()
    length = feed.getLength()
    entries = feed.getEntries()
    results = [{'title':entry.getTitle(), 'description':entry.getDescription(), 'published':entry.getPublished(), 'link':entry.getLink()} for entry in entries]
    return render_template('results.html', title=title, description=description, published=published, results=results)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)