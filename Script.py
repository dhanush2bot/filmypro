class script(object):
    START_TXT = """<b>ʜᴇʏ {}, <i>{}</i>\n🤖 I sᴇʀᴠᴇ ᴀs ᴀ ᴘᴏᴡᴇʀғᴜʟ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ ᴡɪᴛʜ ᴀ ʟɪɴᴋ sʜᴏʀᴛᴇɴᴇʀ ʙᴏᴛ! 🚀 Aᴅᴅ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ, ᴀɴᴅ I'ʟʟ sʜᴀʀᴇ ᴍᴏᴠɪᴇs ᴡɪᴛʜ ʏᴏᴜʀ sʜᴏʀᴛᴇɴᴇᴅ ʟɪɴᴋs. 🎥💬 Eᴀsʏ ᴘᴇᴀsʏ! ♻️</b>"""

    MY_ABOUT_TXT = """★ Server: <a href=#>ᴠᴘꜱ</a>
★ ᴅᴀᴛᴀʙᴀꜱᴇ: <a href=https://www.mongodb.com>ᴍᴏɴɢᴏᴅʙ</a>
★ ʟᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>ᴘʏᴛʜᴏɴ</a>
★ ʟɪʙʀᴀʀʏ: <a href=https://pyrogram.org>ᴘʏʀᴏɢʀᴀᴍ</a>"""

    MY_OWNER_TXT = """★ ɴᴀᴍᴇ:👉  <spoiler> {mention} </spoiler> 
★ ᴜꜱᴇʀɴᴀᴍᴇ: @BotGeniusProbot
★ ᴄᴏɴᴛᴀᴄᴛ: <a href=https://t.me/BotGeniusProbot>ᴀᴅᴍɪɴ</a>
★ ᴄᴏᴜɴᴛʀʏ: ɪɴᴅɪᴀ 🇮🇳"""

    STATUS_TXT = """🗂 Total Files: <code>{}</code>
👤 ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ: <code>{}</code>
👥 ᴛᴏᴛᴀʟ ᴄʜᴀᴛꜱ: <code>{}</code>
✨ ᴜꜱᴇᴅ ꜱᴛᴏʀᴀɢᴇ: <code>{}</code>
⚡️ ꜰʀᴇᴇ ꜱᴛᴏʀᴀɢᴇ: <code>{}</code>
🚀 ᴜᴘᴛɪᴍᴇ: <code>{}</code>"""

    NEW_GROUP_TXT = """#NewGroup
★ Title: {}
★ ID: <code>{}</code>
★ Total Members: {}
★ Added by: {}"""

    NEW_USER_TXT = """#NewUser
★ Name: {}
★ ID: <code>{}</code>"""

    NO_RESULT_TXT = """#NoResult
★ Group Name: {}
★ Group ID: <code>{}</code>
★ Name: {}

★ Message: {}"""

    REQUEST_TXT = """★ Name: {}
★ ID: <code>{}</code>

★ Message: {}"""

    NOT_FILE_TXT = """👋 Hello {},

​🇮​ ​🇨​​🇦​​🇳​❜​🇹​ ​🇫​​🇮​​🇳​​🇩​ ​🇹​​🇭​​🇪​ <b>{}</b> 🇮​​🇳​ ​🇲​​🇾​ ​🇩​​🇦​​🇹​​🇦​​🇧​​🇦​​🇸​​🇪​ 🥲

👉 ɢᴏᴏɢʟᴇ ꜱᴇᴀʀᴄʜ ᴀɴᴅ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ꜱᴘᴇʟʟɪɴɢ ɪꜱ ᴄᴏʀʀᴇᴄᴛ.
👉 ᴘʟᴇᴀꜱᴇ ʀᴇᴀᴅ ᴛʜᴇ ɪɴꜱᴛʀᴜᴄᴛɪᴏɴꜱ ᴛᴏ ɢᴇᴛ ʙᴇᴛᴛᴇʀ ʀᴇꜱᴜʟᴛꜱ.
👉 ᴏʀ ɴᴏᴛ ʙᴇᴇɴ ʀᴇʟᴇᴀꜱᴇᴅ ʏᴇᴛ."""
    
    EARN_TXT = """<b>ʜᴏᴡ ᴛᴏ ᴇᴀʀɴ ꜰʀᴏᴍ ᴛʜɪs ʙᴏᴛ

➥ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴇᴀʀɴ ᴍᴏɴᴇʏ ʙʏ ᴜsɪɴɢ ᴛʜɪꜱ ʙᴏᴛ.

» sᴛᴇᴘ 1:- ғɪʀsᴛ ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴀᴅᴅ ᴛʜɪs ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴀᴅᴍɪɴ ᴘᴇʀᴍɪssɪᴏɴ.

» sᴛᴇᴘ 2:- ᴍᴀᴋᴇ ᴀᴄᴄᴏᴜɴᴛ ᴏɴ <a href=https://dashboard.shareus.io/signup/lifetime/xkUKOY>shareus.io</a> [ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴜsᴇ ᴏᴛʜᴇʀ sʜᴏʀᴛɴᴇʀ ᴡᴇʙsɪᴛᴇ ]

» sᴛᴇᴘ 3:- ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ɢɪᴠᴇɴ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ sʜᴏʀᴛɴᴇʀ ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ.

➥ ᴛʜɪꜱ ʙᴏᴛ ɪs ꜰʀᴇᴇ ꜰᴏʀ ᴀʟʟ, ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘs ғᴏʀ ꜰʀᴇᴇ ᴏꜰ ᴄᴏꜱᴛ.</b>"""

    HOW_TXT = """<b>ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ᴏᴡɴ sʜᴏʀᴛɴᴇʀ ‼️

➥ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ᴏᴡɴ sʜᴏʀᴛɴᴇʀ ᴛʜᴇɴ ᴊᴜsᴛ sᴇɴᴅ ᴛʜᴇ ɢɪᴠᴇɴ ᴅᴇᴛᴀɪʟs ɪɴ ᴄᴏʀʀᴇᴄᴛ ꜰᴏʀᴍᴀᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ

➥ ғᴏʀᴍᴀᴛ ↓↓↓

<code>/set_shortlink sʜᴏʀᴛɴᴇʀ sɪᴛᴇ sʜᴏʀᴛɴᴇʀ ᴀᴘɪ</code>

➥ ᴇxᴀᴍᴘʟᴇ ↓↓↓

<code>/set_shortlink shareus.io 0ft2s2mKCHOaLUKDZCcnDXCt8O63</code>

➥ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄʜᴇᴄᴋ ᴡʜɪᴄʜ sʜᴏʀᴛᴇɴᴇʀ ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛʜᴇɴ sᴇɴᴅ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴛʜᴇ ɢʀᴏᴜᴘ /get_shortlink

📝 ɴᴏᴛᴇ:- ʏᴏᴜ sʜᴏᴜʟᴅ ɴᴏᴛ ʙᴇ ᴀɴ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ ɪɴ ɢʀᴏᴜᴘ. sᴇɴᴅ ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜᴏᴜᴛ ʙᴇɪɴɢ ᴀɴ ᴀɴᴏɴʏᴍᴜs ᴀᴅᴍɪɴ.</b>"""

    IMDB_TEMPLATE = """✅ I Found: <code>{query}</code>

🏷 ᴛɪᴛʟᴇ: <a href={url}>{title}</a>
🎭 ɢᴇɴʀᴇꜱ: {genres}
📆 ʏᴇᴀʀ: <a href={url}/releaseinfo>{year}</a>
🌟 ʀᴀᴛɪɴɢ: <a href={url}/ratings>{rating} / 10</a>
☀️ ʟᴀɴɢᴜᴀɢᴇꜱ: {languages}
📀 ʀᴜɴᴛɪᴍᴇ: {runtime} Minutes

🗣 ʀᴇQᴜᴇꜱᴛᴇᴅ ʙʏ: {message.from_user.mention}
©️ ᴘᴏᴡᴇʀᴇᴅ ʙʏ: <b>{message.chat.title}</b>"""

    FILE_CAPTION = """<i>{file_name}</i>

🚫 ᴘʟᴇᴀsᴇ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ᴄʟᴏsᴇ ʙᴜᴛᴛᴏɴ ɪꜰ ʏᴏᴜ ʜᴀᴠᴇ sᴇᴇɴ ᴛʜᴇ ᴍᴏᴠɪᴇ 🚫"""

    WELCOME_TEXT = """👋 Hello {mention}, Welcome to {title} group! 💞"""

    HELP_TXT = """<b>Need a hand? Check out these commands! 👇 (Type without any argument for details) 😺</b>"""
    
    ADMIN_COMMAND_TXT = """<b>Here is bot admin commands 👇

/index_channels - to check how many index channel id added
/stats - to get bot status
/delete - to delete files using query
/delete_all - to delete all indexed file
/broadcast - to send message to all bot users
/grp_broadcast - to send message to all groups
/restart - to restart bot
/leave - to leave your bot from particular group
/unban_grp - to enable group
/ban_grp - to disable group
/ban_user - to ban a users from bot
/unban_user - to unban a users from bot
/users - to get all users details
/chats - to get all groups
/invite_link - to generate invite link
/logs - to check bot logs
/index - to index bot accessible channels</b>"""
    
    USER_COMMAND_TXT = """<b>Here is bot user commands 👇

/start - to check bot alive or not
/settings - to change group settings as your wish
/set_template - to set custom imdb template
/set_caption - to set custom bot files caption
/set_shortlink - group admin can set custom shortlink
/get_custom_settings - to get your group settings details
/set_welcome - to set custom new joined users welcome message for group
/set_tutorial - to set custom tutorial link in result page button
/connect - to connect group
/disconnect - to disconnect group
/connections - to check how many your groups connected by bot
/id - to check group or channel id
/openai - Find solution to any question with ChatGPT</b>"""

    SOURCE_TXT = """<b>
- 
ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴀ ᴘʀɪᴠᴀᴛᴇ ᴘʀᴏᴊᴇᴄᴛ.

- ꜱᴏᴜʀᴄᴇ - <a href=https://t.me/BotGeniusProbot>ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ📞</a>

ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ -
<a href=https://t.me/filmyspotupdate>ꜰɪʟᴍʏꜱᴘᴏᴛ ᴜᴘᴅᴀᴛᴇ </a></b>"""
