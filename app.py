from flask import Flask, request, render_template
from dotenv import load_dotenv
from openai import OpenAI
import os
import openai

load_dotenv() 
app = Flask(__name__)  

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
def generate_roast(user_input):
    prompt = f"Roast this person in a funny and sarcastic way: {user_input}"

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're a funny AI that roasts people in a lighthearted way."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        roast = generate_roast(user_input)
        return render_template("index.html", user_input=user_input, roast=roast)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
