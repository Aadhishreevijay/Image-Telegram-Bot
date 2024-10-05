import os
import asyncio
import logging
from openai import OpenAI
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from example import example
from image_gen import generate_image 

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token='8144765662:AAFMFCwriAsKQhYYZrmDEmVB1wiZAoDEMbM')
dp = Dispatcher()
client = OpenAI(api_key="sk-proj-tUnAZtfzplDfntstmguRT3BlbkFJO1JI8xCo9Gm0gR3GWNyF")

example()

@dp.message(CommandStart())
async def welcome(message: Message):
    logger.info("Received /start command.")
    await message.answer('Hello! I am GPT Chat BOT. You can ask me anything, including generating images! Just type "generate an image" followed by your description.')

@dp.message()
async def gpt(message: Message):
    logger.info(f"Received message: {message.text}")
    if message.text.lower().startswith('generate an image'):
        prompt = message.text[len('generate an image '):].strip()
        logger.info(f"Image generation prompt: {prompt}")
        if prompt:
            image_url = generate_image(prompt) 
            logger.info(f"Generated image URL: {image_url}")
            await message.answer(f"Here is your generated image: {image_url}")
        else:
            await message.answer("Please provide a description after 'generate an image'.")
    else:
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message.text}
        ]
        completion = client.chat.completions.create(
            messages=messages,
            model="gpt-3.5-turbo",
        )
        reply_content = completion.choices[0].message.content
        await message.answer(reply_content)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
