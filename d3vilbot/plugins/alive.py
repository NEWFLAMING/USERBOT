from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"


edit_time = 16
""" =======================CONSTANTS====================== """
#file1 = "https://telegra.ph/file/e441ee749e930d4f99a6d.jpg"
file1 = Config.ALIVE_PIC
file2 = "https://telegra.ph/file/4cc2b6c2702a1a9c96469.mp4"
file3 = "https://telegra.ph/file/c00cbf9a5331faad7913d.mp4"
file4 = "https://telegra.ph/file/4da06dc332ded806e2705.mp4"
""" =======================CONSTANTS====================== """
pm_caption = "  __**๐ฃ๐ฃFLAMING BOT IS ALIVE๐ฃ๐ฃ**__\n\n"
pm_caption += f"**โโโโโโโโโโโโโโโโโโโโ**\n\n"
pm_caption += (
    f"                 ๐ผ๐ฐ๐๐๐ด๐\n  **ใ {d3vil_mention} ใ**\n\n"
)
pm_caption += f"โโโโโโโโโโโโโโโโโโโโ\n"
pm_caption += f"โ โขโณโ  `๐ณ๐พ๐๐พ๐๐๐๐:` `{tel_ver}` \n"
pm_caption += f"โ โขโณโ  `๐ต๐พ๐๐๐๐๐:` `{d3vil_ver}`\n"
pm_caption += f"โ โขโณโ  `๐ฒ๐๐ฝ๐:` `{is_sudo}`\n"
pm_caption += f"โ โขโณโ  `๐ข๐๐บ๐๐๐พ๐:` [๐น๐๐๐](https://t.me/flamingchat)\n"
pm_caption += f"โ โขโณโ  `๐ข๐๐พ๐บ๐๐๐:` [๐ณ3๐บ๐๐ธ๐๐ท](https://t.me/flamingsupport)\n"
pm_caption += f"โ โขโณโ  `๐ฎ๐๐๐พ๐:` [๐ณ3๐๐ธ๐ป๐ถ๐๐ป๐๐ท๐ฐ๐ฝ](https://t.me/flamingai)\n"
pm_caption += f"โโโโโโโโโโโโโโโโโโโโ\n"
pm_caption += " [โกREPOโก](https://github.com/FLAMING-AI/FLAMING-1) ๐น [๐License๐](https://github.com/FLAMING-AI/FLAMING-1/blob/main/LICENSE)"

 # @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    
    on = await borg.send_file(alive.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(alive.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(alive.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(alive.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(alive.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(alive.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(alive.chat_id, ok5, file=file4)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(alive.chat_id, ok6, file=file1)
    
    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(alive.chat_id, ok7, file=file2) 

    await asyncio.sleep(edit_time)
    ok9 = await borg.edit_message(alive.chat_id, ok8, file=file3)

    await asyncio.sleep(edit_time)
    ok10 = await borg.edit_message(alive.chat_id, ok9, file=file1)
    
    await asyncio.sleep(edit_time)
    ok11 = await borg.edit_message(alive.chat_id, ok10, file=file3)
    
    await asyncio.sleep(edit_time)
    ok12 = await borg.edit_message(alive.chat_id, ok11, file=file2)
    
    await asyncio.sleep(edit_time)
    ok13 = await borg.edit_message(alive.chat_id, ok12, file=file4)
    
    await asyncio.sleep(edit_time)
    ok14 = await borg.edit_message(alive.chat_id, on, file=file1)

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()
    
msg = f"""
**โก ๐3๐๐๐๐๐๐ ๐๐ ๐๐๐๐๐๐ โก**
{Config.ALIVE_MSG}
**๐ ๐ฑ๐๐ ๐๐๐๐๐๐ ๐**
**โผ๐ ๐๐ฆ๐ง๐๐ฅโ   :**  **ใ{d3vil_mention}ใ**
**โโโโโโโโโโโโโโโโโโโโ**
**โ โณโ  TELETHON :**  `{tel_ver}`
**โ โณโ  FLAMINGBOT  :**  **{d3vil_ver}**
**โ โณโ  UPTIME   :**  `{uptime}`
**โ โณโ  ABUSE    :**  **{abuse_m}**
**โ โณโ  SUDO      :**  **{is_sudo}**
**โโโโโโโโโโโโโโโโโโโโ
"""
botname = Config.BOT_USERNAME

@d3vilbot.on(d3vil_cmd(pattern="d3vil$"))
@d3vilbot.on(sudo_cmd(pattern="d3vil$", allow_sudo=True))
async def d3vil_a(event):
    try:
        d3vil = await bot.inline_query(botname, "alive")
        await d3vil[0].click(event.chat_id)
        if event.sender_id == d3krish:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "d3vil", None, "Shows Inline Alive Menu with more details."
).add()
