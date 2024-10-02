from openai import OpenAI
import os
from flask import Flask, render_template, request

client = OpenAI(api_key="sk-proj-tUnAZtfzplDfntstmguRT3BlbkFJO1JI8xCo9Gm0gR3GWNyF")

def generate_tutorial(components):
    response = client.images.generate(
        model="dall-e-3",
        prompt=components,
        n=1,
        size="1024x1024"
    )
    image_url = response.data[0].url
    return image_url  

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    components = request.form['components']
    image_url = generate_tutorial(components)
    return image_url

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
