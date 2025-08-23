import random

class JokeBot:
    def __init__(self):
        self.jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don't programmers like nature? It has too many bugs.",
            "What do you call fake spaghetti? An impasta!",
            "Why did the math book look sad? Because it had too many problems.",
            "What do you call cheese that isn't yours? Nacho cheese!",
            "Why was the computer cold? It left its Windows open!",
            "Why did the bicycle fall over? Because it was two-tired!",
            "What do you get when you cross a snowman and a vampire? Frostbite!",
            "Why do seagulls fly over the ocean? Because if they flew over the bay, they'd be bagels!",
            "What did one snowman say to the other snowman? It smells like carrots over here!",
            "Why did Beethoven get rid of his chickens? All they ever said was, “Bach, Bach, Bach!”",
            "What did 20 do when it was hungry? Twenty-eight.",
            "Why is grass so dangerous? Because it's full of blades!",
            "Why are mountains so funny? They’re hill areas.",
            "Why wasn’t the cactus invited to hang out with the mushrooms? He wasn’t a fungi.",
            "Why shouldn’t you fundraise for marathons? They just take the money and run.",
            "Why did the crab cross the road? It didn’t—it used the sidewalk.",
            "Why does it take pirates a long time to learn the alphabet? Because they can spend years at C!",
            "Why can't a nose be 12 inches long? Because then it would be a foot.",
            "Why can’t you put two half-dollars in your pocket? Because two halves make a hole, and your money will fall out!",
            "Why does a moon rock taste better than an Earth rock? It’s a little meteor.",
            "How much do rainbows weigh? Not much. They’re actually pretty light.",
            "What is the most popular fish in the ocean? The starfish.",
            "A slice of apple pie costs $2.50 in Jamaica, $3.75 in Bermuda, and $3 in the Bahamas. Those are the pie-rates of the Caribbean.",
            "Why did the football coach yell at the vending machine? He wanted his quarter back!",
            "I had a joke about paper today, but it was tearable.",
            "What kind of job can you get at a bicycle factory? A spokesperson",
            "What does a condiment wizard perform? Saucery",
            "What's the difference in an alligator and a crocodile? You’ll see one later and one in a while.",
            "What’s the difference between the bird flu and the swine flu? One requires tweetment and the other an oinkment."
        ]

    def tell_joke(self):
        return random.choice(self.jokes)

if __name__ == "__main__":
    joke_bot = JokeBot()
    print("Here's a joke for you:")
    print(joke_bot.tell_joke())
