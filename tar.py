from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)
API_KEY = ""

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather Chatbot</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap" rel="stylesheet">
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #6dd5ed, #2193b0);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            padding: 30px;
            border-radius: 15px;
            width: 90%;
            max-width: 400px;
            text-align: center;
            box-shadow: 0px 8px 20px rgba(0,0,0,0.2);
            color: white;
        }
        h1 {
            font-weight: 700;
            font-size: 2em;
            margin-bottom: 10px;
        }
        p {
            font-weight: 300;
        }
        input {
            padding: 10px;
            width: 80%;
            border-radius: 5px;
            border: none;
            outline: none;
            margin-top: 15px;
            font-size: 16px;
        }
        button {
            background-color: #ff9800;
            border: none;
            padding: 10px 20px;
            color: white;
            font-size: 16px;
            border-radius: 5px;
            margin-top: 15px;
            cursor: pointer;
            transition: background 0.3s ease;
        }
        button:hover {
            background-color: #e68900;
        }
        .result {
            margin-top: 20px;
            font-size: 1.2em;
            animation: fadeIn 0.5s ease-in-out;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .icon {
            font-size: 50px;
            margin-top: 10px;
            animation: bounce 1s infinite alternate;
        }
        @keyframes bounce {
            to { transform: translateY(-5px); }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌤 Weather Chatbot</h1>
        <p>Hello! Please enter a city name to check its weather:</p>
        <form method="post">
            <input type="text" name="city" placeholder="e.g. Delhi" required>
            <br>
            <button type="submit">Check Weather</button>
        </form>
        {% if weather %}
            <div class="result">
                <div class="icon">☀️</div>
                {{ weather }}
            </div>
        {% endif %}
    </div>
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