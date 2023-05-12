from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_gender(name):
    parameters = {
        "name" : name
    }
    response = requests.get(url = "https://api.genderize.io", params = parameters)
    response.raise_for_status()

    data = response.json()
    # print(data['gender'])
    return data['gender']

def get_age(name):
    parameters = {
        "name" : name
    }
    response = requests.get(url = "https://api.agify.io/", params = parameters)
    response.raise_for_status()

    data = response.json()
    print(data['age'])
    return data['age']

@app.route("/guess/<string:user_name>")
def home(user_name):
    name = user_name
    gender = get_gender(name)
    age = get_age(name)
    return render_template("index.html", name = name, age = age, gender = gender)

if __name__ == "__main__":
    app.run(debug=True)


