import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# توکن شما
TOKEN = "9240190897:AAEzafgrLuY6NFCT2XJ6u4c0Ho5-IvbIIoY"

# لینک مینی‌اپ شما (حتما چک کن که لینک نهایی گیت‌هابت اینجا باشه)
MINI_APP_URL = "https://hamidipoorali-eng.github.io/mental-discipline-bot/" # اینجا رو با لینک اصلی خودت عوض کن

# === این بخش برای فریب دادن سرور رندر و استفاده از پلن رایگان است ===
class DummyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive and running!")

def run_dummy_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), DummyHandler)
    server.serve_forever()
# =================================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    
    welcome_message = (
        f"سلام {user.first_name}.\n\n"
        "من معلم ریاضی نیستم. من فقط یاد گرفتم چطور مغزم را از اسارت ماشین‌حساب رها کنم تا در لحظات حساس، سریع‌تر و دقیق‌تر عمل کنم. "
        "اینجا باشگاه تمرین و دیسپلین روزانه من است.\n\n"
        "اگر تو هم می‌خواهی سرعت و دقت پردازش ذهنت را بالا ببری، با من هم‌مسیر شو."
    )
    
    keyboard = [
        [InlineKeyboardButton("ورود به باشگاه 🧠", web_app=WebAppInfo(url=MINI_APP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)

def main():
    # روشن کردن سرور جعلی در یک رشته (Thread) جداگانه
    threading.Thread(target=run_dummy_server, daemon=True).start()
    
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("ربات با موفقیت روشن شد. منتظر ورود کاربران...")
    app.run_polling()

if __name__ == "__main__":
    main()
