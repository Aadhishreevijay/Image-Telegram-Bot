# Image Telegram Bot with OpenAI and DALL-E Integration

This repository combines the OpenAI's GPT-3.5-Turbo model and DALL-E for text-based assistance and image generation, enabling users to interact with a chatbot and generate images directly through Telegram.

## Features

- **GPT-3.5 Turbo**: A conversational chatbot that responds to user queries using OpenAI's model.
- **DALL-E Image Generation**: Generates images based on user-provided prompts via Telegram.
- **Integrated Bot**: Combines both text-based assistance and image generation into a single bot for a seamless experience.
- **Flask Server**: A simple Flask server for hosting the bot and handling image generation.

## Repository Structure

The repository is divided into three key sections:

1. **Telegram Bot using OpenAI**  
   - A Telegram bot that uses GPT-3.5-Turbo for conversation and query responses.
   - [View Source Code](https://github.com/Aadhishreevijay/Image-Telegram-Bot/tree/main/telegram-bot%20using%20openAI)
     
   - **Example Output**:
     
     <img width="360" alt="Tele_bot final output" src="https://github.com/user-attachments/assets/258c0ad4-da70-4a54-a741-fd6ce904092e">

2. **Image Generation using DALL-E**  
   - A web interface for generating images based on text descriptions using DALL-E.
   - [View Source Code](https://github.com/Aadhishreevijay/Image-Telegram-Bot/tree/main/image-generation%20using%20DALL-e)
     
   - **Example Output**:
     
     [Create new issues](https://github.com/Aadhishreevijay/Image-Telegram-Bot/issues/new) 

3. **Integrated Bot (OpenAI-DALL-E with Telegram)**  
   - Combines the functionality of the chatbot and image generation into a single bot.
   - Can also be integrated using Make.com for low-code automation.
   - [View Source Code](https://github.com/Aadhishreevijay/Image-Telegram-Bot/tree/main/Integrated-bot%20(OpenAI-DALL-e%20with%20Telegram))
     
   - **Example Output**:
     
     - **Make.com Output**:
       
       <img width="419" alt="make com output" src="https://github.com/user-attachments/assets/12142e91-ad2f-40ad-ab61-78f4db1384a4">
       
     - **Code Integration Output**:
       
       <img width="238" alt="output" src="https://github.com/user-attachments/assets/6d127151-7cb9-4bce-b443-013da3f3e109">

## How to Use

### Prerequisites
- Python 3.7+
- Telegram bot token
- OpenAI API key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Aadhishreevijay/Image-Telegram-Bot.git
   cd Image-Telegram-Bot
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables for the Telegram bot token and OpenAI API key:
   ```bash
   export TELEGRAM_TOKEN='your-telegram-bot-token'
   export OPENAI_API_KEY='your-openai-api-key'
   ```

### Running the Telegram Bot

To run the bot that handles both GPT-3.5 Turbo and DALL-E image generation:

```bash
python main.py
```

### Web Interface for Image Generation

For the DALL-E image generator web app:

```bash
cd image-generation
python main.py
```

Visit `http://localhost:8080` in your browser to generate images based on text prompts.
