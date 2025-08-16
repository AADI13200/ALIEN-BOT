from google import genai

# Replace with your actual Gemini API key
API_KEY = "AIzaSyCJQeEqaLriyZVHozq-sweGF9QDG3f4-oI"

client = genai.Client(api_key=API_KEY)

def gpt():
    print("🤖 Gemini Chatbot is ready! Type 'exit' to quit.\n")
    
    history = []

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Bot: Goodbye! 👋")
            break

        history.append({"role": "user", "parts": [{"text": user_input}]})

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=history
        )

        bot_reply = response.text
        print("Bot:", bot_reply, "\n")

        history.append({"role": "model", "parts": [{"text": bot_reply}]})



def calculator():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print(" Select the operation to be performed \n"," 1. Additon\n"," 2. Subtracton\n", " 3. multiplication\n"," 4. division\n"," 5. module\n")
    s = input("Enter the operation :")
    s = s.lower()
    if "additon" in s or '1' in s:
        c = a+b
        print("Addition of given numbers are : ", c )
    elif "subtraction" in s or '2' in s:
        c = a-b
        print("Subtraction of given numbers are: ", c)
    elif "multiplication" in s or '3' in s:
        c = a*b
        print("Multiplication of given nummbers are : ", c)
    elif "division" in s or '4' in s:
        c = a/b
        print("Division of given numbers are : ", c)
    elif "module" in s or '5' in s:
        c = a%b
        print("Reminder you recieve after the division of given numbers are : ", c)
    else: 
        print(" Invalid operation input \n"," please enter valid operation number from menu")
    
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "weather" in user_input or '1' in user_input:
        return "You can check today's weather using OpenWeather API."
    elif "gpt" in user_input or '4' in user_input:
        gpt()
        return "  Returning to the main menu ..."
    elif "news" in user_input or '2' in user_input:
        return " code to be written "
    elif "movie" in user_input or '3' in user_input:
        return " code to be written "
    elif "restuarents" in user_input or '5' in user_input:
        return " code to be written "
    elif "calculator" in user_input or '6' in user_input:
        while True:
            h = input("Type 'start' to run calculator or 'exit' to quit calculator: ")
            if h.lower() == "exit":
                print("  Exiting calculator  ")
                break
            elif h.lower() == "start":
                calculator()
            else:
                print("Invalid input. Type 'start' or 'exit'.")
        return "  Returning to the main menu ... "

    else:
        return "Sorry, I didn't get that. You can ask about weather or jokes."

# Start chatbot loop
print(" Hello ! \n"," I am <title> bot \n"," Please select the Domain\n \n ", "1. weather\n"," 2. news\n"," 3. movie recommendation\n"," 4. GPT\n"," 5. restuarents\n"," 6. Calculator\n \n"," Type exit or quit to stop")
while True:
    user_msg = input("You: ")
    user_msg = user_msg.lower()

    if user_msg in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
        break

    response = chatbot_response(user_msg)
    print("Chatbot:", response)
