from random import choice

questions = ["Why is the sky blue? ","Why are there so many houses? ","Why does everyone wear clothes? ",]
question = choice(questions)
answer = input(question).lower().strip()


while answer != "just because":
    answer = input("Why?: ").strip().lower()

print("Oh...okay")
