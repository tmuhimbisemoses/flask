import feedparser
from flask import Flask
import jinja2
from flask import render_template
app = Flask(__name__)
BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"

@app.route("/")
def get_news():
  feed = feedparser.parse(BBC_FEED)
  first_article = feed['entries'][0]
  return render_template("temp.html")

if __name__ == "__main__":
  app.run(port=5000, debug=True)