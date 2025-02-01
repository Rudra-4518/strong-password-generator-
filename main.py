from flask import Flask, render_template, request # type: ignore
import random
import string

app = Flask(__name__)

def generate_password(length, include_uppercase, include_lowercase, include_digits, include_symbols):
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:  # Handle case where no character type is selected
        return "Please select at least one character type."

    password = ''.join(random.choice(characters) for i in range(length))
    return password


@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    if request.method == "POST":
        length = int(request.form.get("length"))
        include_uppercase = request.form.get("uppercase") == "on"
        include_lowercase = request.form.get("lowercase") == "on"
        include_digits = request.form.get("digits") == "on"
        include_symbols = request.form.get("symbols") == "on"

        password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_symbols)

    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)  # debug=True for development; set to False in production