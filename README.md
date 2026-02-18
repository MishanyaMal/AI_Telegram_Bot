# AI Telegram Bot via OpenRouter

A Telegram bot that connects to AI models via the OpenRouter API. The bot relays user messages to the AI and returns the model's response in the chat. Placeholder values must be replaced with your own API keys and configuration.

## Features

- **Telegram Integration:** Responds to direct messages in Telegram.
- **AI Backend:** Communicates with any AI model available on OpenRouter.
- **Conversation History:** Maintains a simple message history for context.
- **Easy Configuration:** All settings are in a single config file.
- **Error Handling:** Graceful handling of API errors and network issues.

## Technologies Used

- **Language:** `Python`
- **Telegram Bot API:** `python-telegram-bot` library
- **AI Module** `openai` library
- **API Provider:** OpenRouter (https://openrouter.ai)

### Prerequisites

- Python 3.8 or higher
- A Telegram account
- An OpenRouter account (https://openrouter.ai)
- API keys for both Telegram and OpenRouter

### Step‑by‑Step Guide

1. **Create a Telegram Bot:**
   - Message `@BotFather` on Telegram.
   - Use the `/newbot` command to create a new bot.
   - Copy the **API Token** provided by BotFather.

2. **Get Your OpenRouter Credentials:**
   - Sign up at https://openrouter.ai.
   - Navigate to your dashboard to find or create an **API Key**.
   - Note the **Model ID** of the AI model you want to use (e.g., `openai/gpt-3.5-turbo`).
