import os
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
# openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        character_name = request.form["character_name"]
        return render_template("story.html") #, result=response.choices[0].text))

    #result = request.args.get("result")
    return render_template("index.html") #, result=result)


def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )
