# import the python datetime module to help us create a timestamp
from datetime import date
from slithering import BlackMamba, Copperhead, Python, RatSnake, Snail
from swimming import Catfish, ClownFish, Goldfish, Mallard, Turtle
from walking import Bear, Donkey, Goat, Horse, Llama


miss_fuzz = Llama("Miss Fuzz", "domestic llama", "midday", "llama chow")

yogi = Bear("Yogi", "black bear", "morning", "honey")


eeyore = Donkey("Eeyore", "donkey", "afternoon", "antidepressants")

gabby = Goat("Gabby", "goat", "midday", "lizards")


hunter = Catfish("Hunter", "cat fish", "chicken livers")


kale = Copperhead("Kale", "copperhead snake", "pennies")


steve = Snail("Steve", "snail", "beer")


franklin = Turtle("Franklin", "turtle", "butter lettuce")


bojack = Horse("Bojack", "horse", "afternoon", "a martini")


marty = ClownFish("Marty", "clown fish", "jokes")


daffy = Mallard("Daffy", "mallard", "spinach")


fudge = Goldfish("Fudge", "gold fish", "golden-o's")


randall = RatSnake("Randall", "rat snake", "rats")


patrick = Python("Patrick", "python", "code")


kobe = BlackMamba("Kobe", "black mamba", "passes")


print(
    f"{yogi.name} the {yogi.species} is available to pet during the {yogi.shift} shift."
)

print(miss_fuzz.feed())
print(bojack.feed())

print(bojack)
