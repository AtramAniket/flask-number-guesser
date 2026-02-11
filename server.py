from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 10)
print(random_number)

@app.route('/')
def hello_world():
	return "<h1>Guess a number between 0 and 9</h1>" \
		   '<img src = "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGh2cXNqNDg4Mmh3ZDJhdWc0bHFzN3VsZW0wcnZ0YmdsZDhwbDZlNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/pH1swuo2JsnACovyRA/giphy.gif" alt="number-gif" />'

@app.route('/<int:input_number>')
def check_number(input_number):
	if input_number < random_number:
		return '<h2 style = "color: red">Too low, Try again!</h2>' \
		'<img src = "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOXp4amVlbTR4YWlzOWs2ejE2a216bG9vYm5hanpwNzdzY3Z3d3NlcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/P3ataVxTgFOimQeC0S/giphy.gif" alt = "number-guessed-is-too-low"/>'
	elif input_number > random_number:
		return '<h2 style = "color: magenta">Too high, Try again!</h2>' \
		'<img src = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdTBrNW1jeGV4bnI5MXBqYzgwNGtuN2ZvYXRqcnI1bmNnMmI3azd2aSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ijgLeINIH40Jor6TD1/giphy.gif" alt = "number-guessed-is-too-high"/>'
	else:
		return '<h2 style = "color: green">You found me!!</h2>' \
		'<img src = "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdzFxM2ZrbmNuNnB5Ymd4c3Q2dDczYmczZ2ZlZm1lY2huNzZueXJzOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/bXpgshfh5uxupxGFqd/giphy.gif" alt = "number-guessed-correctly"/>'



if __name__ == "__main__":
	app.run(debug=True)
