from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

# Replace with your NewsAPI key
API_KEY = ""

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>News Chatbot</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
        input, button { padding: 10px; font-size: 16px; margin-top: 10px; }
        .result { margin-top: 20px; font-size: 18px; text-align: left; display:inline-block; }
    </style>
</head>
<body>
    <h1> News Chatbot</h1>
    <p>Enter a topic you want the latest news about:</p>
    <form method="post">
        <input type="text" name="topic" placeholder="e.g. Technology, Sports, Delhi" required>
        <button type="submit">Get News</button>
    </form>
    {% if news %}
        <div class="result">
            <h2>Top News on "{{ topic }}"</h2>
            <ul style="list-style:none; padding:0;">
                {% for n in news %}
                    <li>
                        <b>{{ n['title'] }}</b><br>
                        <a href="{{ n['url'] }}" target="_blank">Read more</a><br><br>
                    </li>
                {% endfor %}
            </ul>
        </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    news_articles = None
    topic = None
    if request.method == "POST":
        topic = request.form.get("topic")
        if topic:
            url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=popularity&apiKey={API_KEY}"
            res = requests.get(url)
            data = res.json()

            if data.get("status") == "ok":
                news_articles = data.get("articles", [])[:10]

    return render_template_string(HTML_PAGE, news=news_articles, topic=topic)

if __name__ == "__main__":
    app.run(debug=True)
