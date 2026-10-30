from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# توکن ربات شما با موفقیت جایگذاری شد
TOKEN = "9240190897:AAEzafgrLuY6NFCT2XJ6u4c0Ho5-IvbIIoY"

# لینک موقت مینی‌اپ (در مرحله بعد این لینک را با لینک واقعی جایگزین می‌کنیم)
MINI_APP_URL = "https://hamidipoorali-eng.github.io/mental-discipline-bot/" 

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
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("ربات با موفقیت روشن شد. منتظر ورود کاربران...")
    app.run_polling()

if __name__ == "__main__":
    main()
