from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	return "<h1>Guess a number between 0 and 9</h1>" \
		   '<img src = "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGh2cXNqNDg4Mmh3ZDJhdWc0bHFzN3VsZW0wcnZ0YmdsZDhwbDZlNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/pH1swuo2JsnACovyRA/giphy.gif" alt="number-gif" />'


if __name__ == "__main__":
	app.run(debug=True)
