from openai import OpenAI
import os

client = OpenAI(api_key="sk-proj-tUnAZtfzplDfntstmguRT3BlbkFJO1JI8xCo9Gm0gR3GWNyF")

def generate_image(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response.data[0].url
    return image_url
