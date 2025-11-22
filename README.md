## 🛠️ Telegram Bot for Product Sales

This project is a Telegram bot designed to showcase and sell hardware products.  
Users can easily browse product categories, view items forwarded from a dedicated channel, and contact support directly through inline buttons.

### ✨ Features
- Welcome message with an inline main menu  
- Product categories (cabinet accessories, dish racks, lighting, fittings, etc.)  
- Product display using **copy_message** from a Telegram channel (no need to re-upload media)  
- Inline support button to send product codes directly to the admin  
- Modular structure for adding new categories  
- Secure token management with `.env`  

### 📂 Project Structure
```
telegram-bot/
│
├── bot.py              # Main bot code
├── requirements.txt    # Dependencies
├── .env      # Example environment file (no real token)
├── .gitignore          # Prevents sensitive files from being uploaded
```

### ⚙️ Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/USERNAME/telegram-bot.git
   cd telegram-bot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file and add your bot token:
   ```env
   API_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
   ```
4. Run the bot:
   ```bash
   python bot.py
   ```


