import os
import asyncio
from openai import OpenAI
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from example import example

bot = Bot(token='7743168459:AAE99PqqLdqeSmgn3qQWFWXG5DlQ5pMzopA')  
dp = Dispatcher()
client = OpenAI(api_key="sk-proj-tUnAZtfzplDfntstmguRT3BlbkFJO1JI8xCo9Gm0gR3GWNyF")

example()

@dp.message(CommandStart())
async def welcome(message: Message):
    await message.answer('Hello! I am GPT Chat BOT. You can ask me anything :)')

@dp.message()
async def gpt(message: Message):
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
