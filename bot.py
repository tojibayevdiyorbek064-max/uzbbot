import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("📚 Ma'lumot", callback_data="info"),
            InlineKeyboardButton("🆘 Yordam", callback_data="help")
        ],
        [
            InlineKeyboardButton("📞 Aloqa", callback_data="contact"),
            InlineKeyboardButton("ℹ️ Bot haqida", callback_data="about")
        ]
    ]

    text = (
        "👋 Assalomu alaykum!\n\n"
        "🤖 UzbBot'ga xush kelibsiz!\n"
        "Kerakli bo'limni tanlang 👇"
    )

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "info":
        await query.message.reply_text(
            "📚 MA'LUMOT\n\n"
            "🤖 Bu UzbBot.\n"
            "🇺🇿 O'zbek foydalanuvchilari uchun yaratilgan bot.\n\n"
            "Bu yerda kerakli ma'lumotlarni olishingiz mumkin."
        )

    elif query.data == "help":
        await query.message.reply_text(
            "🆘 YORDAM\n\n"
            "Botdan foydalanish juda oson!\n\n"
            "📚 Ma'lumot — bot haqida ma'lumot\n"
            "📞 Aloqa — admin bilan bog'lanish\n"
            "ℹ️ Bot haqida — bot haqida batafsil\n\n"
            "Kerakli tugmani tanlang 👇"
        )

    elif query.data == "contact":
        await query.message.reply_text(
       "📞 ALOQA\n\n"
        "Savol yoki takliflaringiz bo'lsa, admin bilan bog'laning 👇\n\n"
        "👤 Admin: @odiljanov_d"
        )

    elif query.data == "about":
        await query.message.reply_text(
        "ℹ️ UZBBOT HAQIDA\n\n"
        "🤖 UzbBot — o'zbek foydalanuvchilari uchun yaratilgan bot.\n\n"
        "🇺🇿 Bot orqali turli foydali ma'lumotlardan foydalanishingiz mumkin.\n"
        "📚 Kerakli bo'limni tanlab ma'lumot olishingiz mumkin.\n"
        "📞 Admin bilan Aloqa bo'limi orqali bog'lanishingiz mumkin.\n\n"
        "✨ UzbBot doimo rivojlantirib boriladi!"
              )        
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("🤖 Bot ishga tushdi!")
    app.run_polling()

if __name__ == "__main__":
    main()
