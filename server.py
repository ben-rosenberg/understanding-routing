from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world() -> str:
    return 'Hello, world!'

@app.route('/dojo')
def dojo() -> str:
    return 'Dojo!'

# NOTE For the "ninja bonus" problem, I'm assuming when they say, "ensure
# the names provided are string" they mean ensure the input contains only
# letters, no numbers. It'll always be a string, even if numbers are entered.
@app.route('/say/<name>')
def say(name) -> str:
    if not name.isalpha():
        return 'Error: Must enter letters only'
    return 'Hi ' + name + '!'

@app.route('/repeat/<repetitions>/<input_str>')
def repeat(repetitions, input_str) -> str:
    if not repetitions.isnumeric():
        return 'Error: First input must be a positive integer'
    if not input_str.isalpha():
        return 'Error: Second input must only contain letters'

    repetitions_int = int(repetitions)
    str_to_display = ""
    for x in range(repetitions_int):
        str_to_display += input_str
    return str_to_display

# NOTE Probably not the best way to do this.
@app.route('/<error>')
def error(error) -> str:
    return f'Error: /{error} is not a valid route, try again.'


if __name__ == '__main__':
    app.run(debug = True)