class script(object):
    START_TXT = """<b>Mʏ Nᴀᴍᴇ Is #Minato, I Cᴀɴ Pʀᴏᴠɪᴅᴇ 
<a href='https://t.me/The_Happy_Hour_Hindi'>Mᴏᴠɪᴇs</a>, Jᴜsᴛ Aᴅᴅ Mᴇ Tᴏ <a href='https://t.me/ThappyHour'>Yᴏᴜʀ Gʀᴏᴜᴘ
</a> Aɴᴅ Eɴᴊᴏʏ.

ᴅᴇᴠʟᴏᴘᴇᴅ ʙʏ : <a href=https://t.me/The_Happy_Hours>The Happy Hour</a></b>"""
    HELP_TXT = """○ Available Commands
     
 /start - Check I'm Alive..
 /status - Bot Status
 /info - User info 
 /id - User id
 /stats - Db status  
 /broadcast - Broadcast (owner only)
"""
    ABOUT_TXT = """<b>◎ Nᴀᴍᴇ: ᴋᴜᴛᴛᴜ ʙᴏᴛ™
◎ Cʀᴇᴀᴛᴏʀ: <a href=https://t.me/MAster_Jiraya_Bot>Master Jiraya</a>
◎ Lᴀɴɢᴜᴀɢᴇ: Pʏᴛʜᴏɴ 3
◎ Dᴀᴛᴀ Bᴀsᴇ: Mᴏɴɢᴏ DB
◎ Bᴏᴛ Sᴇʀᴠᴇʀ: Heroku</b>"""
    SOURCE_TXT = """Nai Duga...😘😘"""
    MANUELFILTER_TXT = """
<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. This Botsupports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format
"""
    AUTOFILTER_TXT = """
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes."""
    CONNECTION_TXT = """
- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> """
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    RESULT_TXT="""Here are list of files"""

    CUSTOM_FILE_CAPTION = """<b><a href="https://t.me/ThappyHour">{CUSTOM_FILE_CAPTION}</a></b>"""

    
    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ</b>"""
    
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
    SPOLL_NOT_FND="""Plzzz Select True Name...✅"""
#SPELL CHECK LANGUAGES TO KNOW callback
    ENG_SPELL="""Sᴇᴀʀᴄʜ Mᴏᴠɪᴇ Wɪᴛʜ Cᴏʀʀᴇᴄᴛ Sᴘᴇʟʟɪɴɢ :

› ᴀᴠᴀᴛᴀʀ ✅
› ᴀᴠᴀᴛᴀʀ 2009 ✅

Sᴇᴀʀᴄʜ Wᴇʙ Sᴇʀɪᴇs Iɴ ᴛʜɪs Fᴏʀᴍᴀᴛᴇ : 

› ᴠɪᴋɪɴɢs S01 ✅
› ᴠɪᴋɪɴɢs S01E01 ✅

🔹 ᴅᴏɴ'ᴛ sᴇɴᴅ ᴀɴʏ ᴋɪɴᴅ ᴏғ ᴘʜᴏᴛᴏ, ᴠɪᴅᴇᴏ ᴅᴏᴄᴜᴍᴇɴᴛs, ᴜʀʟ ᴇᴛᴄ..."""
    MAL_SPELL="""ദ"""
    HIN_SPELL="""Sᴇᴀʀᴄʜ Mᴏᴠɪᴇ Wɪᴛʜ Cᴏʀʀᴇᴄᴛ Sᴘᴇʟʟɪɴɢ :

› ᴀᴠᴀᴛᴀʀ ✅
› ᴀᴠᴀᴛᴀʀ 2009 ✅

Sᴇᴀʀᴄʜ Wᴇʙ Sᴇʀɪᴇs Iɴ ᴛʜɪs Fᴏʀᴍᴀᴛᴇ : 

› ᴠɪᴋɪɴɢs S01 ✅
› ᴠɪᴋɪɴɢs S01E01 ✅

🔹 ᴅᴏɴ'ᴛ sᴇɴᴅ ᴀɴʏ ᴋɪɴᴅ ᴏғ ᴘʜᴏᴛᴏ, ᴠɪᴅᴇᴏ ᴅᴏᴄᴜᴍᴇɴᴛs, ᴜʀʟ ᴇᴛᴄ..."""
    TAM_SPELL="""m"""

    CHK_MOV_ALRT="""♻️ ᴄʜᴇᴄᴋɪɴɢ ꜰɪʟᴇ ᴏɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ... ♻️"""
    
    OLD_MES="""𝐘𝐨𝐮 𝐚𝐫𝐞 𝐮𝐬𝐢𝐧𝐠 𝐨𝐧𝐞 𝐨𝐟 𝐦𝐲 𝐨𝐥𝐝 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬🤔, 𝐩𝐥𝐞𝐚𝐬𝐞 𝐬𝐞𝐧𝐝 𝐭𝐡𝐞 𝐫𝐞𝐪𝐮𝐞𝐬𝐭 𝐚𝐠𝐚𝐢𝐧"""
    
    MOV_NT_FND="""<b>Tʜɪs Mᴏᴠɪᴇ Is Nᴏᴛ Yᴇᴛ Tᴏ DB</b>
"""
