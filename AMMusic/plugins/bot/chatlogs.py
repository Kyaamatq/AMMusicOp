import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import LOG, LOGS, LOG_GROUP_ID
from AMMusic import app  

photo = [
    "https://graph.org/file/44083bf7d2fd4ca820196.jpg",
    "https://graph.org/file/cbce6e62048c493020ca4.jpg",
    "https://graph.org/file/dc55b785e3e2c7b0026fa.jpg",
    "https://graph.org/file/9256adef6b49b1ffeadf6.jpg",
    "https://graph.org/file/63cfa711a7d395aab4e29.jpg",
    "https://graph.org/file/7cce9b4b285e80716d8b3.jpg",
]


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    
    for members in message.new_chat_members:
        if members.id == app.id:
            count = await app.get_chat_members_count(chat.id)
            username = message.chat.username if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐆ʀᴏᴜᴘ"
            msg = (
                f"**📝ꜱʜɪᴢᴜᴋᴀ 乂 ᴍᴜꜱɪᴄ 𝐁ᴏᴛ 𝐀ᴅᴅᴇᴅ 𝐈ɴ 𝐀 𝐍ᴇᴡ 𝐆ʀᴏᴜᴘ**\n\n"
                f"**📌𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ:** {message.chat.title}\n"
                f"**🍂𝐂ʜᴀᴛ 𝐈ᴅ:** {message.chat.id}\n"
                f"**🔐𝐂ʜᴀᴛ 𝐔sᴇʀɴᴀᴍᴇ:** @{username}\n"
                f"**📈𝐆ʀᴏᴜᴘ 𝐌ᴇᴍʙᴇʀs:** {count}\n"
                f"**🤔𝐀ᴅᴅᴇᴅ 𝐁ʏ:** {message.from_user.mention}\n"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"➕ ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))



@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        left = f"**✫** <b><u>#𝐋ᴇғᴛ_𝐆ʀᴏᴜᴘ</u></b> **✫**\n\n**𝐂ʜᴀᴛ 𝐓ɪᴛʟᴇ :** {title}\n\n**𝐂ʜᴀᴛ 𝐈ᴅ :** {chat_id}\n\n**𝐑ᴇᴍᴏᴠᴇᴅ 𝐁ʏ :** {remove_by}\n\n**𝐁ᴏᴛ : @{app.username}\n"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)
