from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)
API_KEY = ""

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Weather Chatbot</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
        input, button { padding: 10px; font-size: 16px; margin-top: 10px; }
        .result { margin-top: 20px; font-size: 18px; }
    </style>
</head>
<body>
    <h1>Weather Chatbot</h1>
    <p>Hello! Please enter a city name to know its weather:</p>
    <form method="post">
        <input type="text" name="city" placeholder="e.g. Delhi" required>
        <button type="submit">Check Weather</button>
    </form>
    {% if weather %}
        <div class="result">{{ weather }}</div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    weather_info = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            res = requests.get(url)
            data = res.json()

            if data.get("cod") != 200:
                weather_info = f"Sorry, I couldn't find weather info for '{city}'."
            else:
                temp = data["main"]["temp"]
                desc = data["weather"][0]["description"]
                weather_info = f"The weather in {city.title()} is {temp}°C with {desc}."

    return render_template_string(HTML_PAGE, weather=weather_info)

if __name__ == "__main__":
    app.run(debug=True)
