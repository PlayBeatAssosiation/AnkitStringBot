from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""Hᴇʏ {msg.from_user.mention},

Tʜɪs ɪs {me2},
Aɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.

Mᴀᴅᴇ ᴡɪᴛʜ 🖤 ʙʏ : [𝐀𝐧𝐤𝐢𝐭](https://t.me/NoMoreAnkit) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="🙄 ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ ʜᴇʀᴇ ❤", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("❣️ sᴏᴜʀᴄᴇ ❣️", url="https://te.legra.ph/file/f20356d6f6ee0a0efd7b8.mp4"),
                    InlineKeyboardButton("🥀 ᴘʀᴏ ᴅᴇᴇʙʟᴏᴘᴇʀ 😎 🥀", user_id=OWNER_ID)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
