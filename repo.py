# COPYRIGHT  BY mayank1rajput

"""
�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7@mayank1rajput�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7
�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7@mayank1rajput�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7
�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7@mayank1rajput�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7
�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7@mayank1rajput�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7�9�7
                 MADE BY mayank1rajput
                 PLEASE KEEP CREDITS -_-
"""



from telethon import events, Button, custom
from marcus import BOT
import os,re
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
@tgbot.on(events.InlineQuery(pattern=r"repo"))
async def inline_id_handler(event: events.InlineQuery.Event):
 marcus = event.builder
 💀= [[custom.Button.inline( CLICK ME",data="obhai")]]
 query = event.text
 result = marcus.article("marcus",text="REPO AND SUPPORT",buttons=💀,link_preview=False)
 await event.answer([result])
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ohhh")))
async def callback_query_handler(event):

# inline by mayank1rajput
  await event.edit(text=f"{BOT} REPO AND GROUP LINK",buttons=[[Button.url(f{BOT} REP", url="https://github.com/hackelite01/marcus-userbot"), Button.url(f"⚡{BOT} SUPPORT⚄1�7", url="https://t.me/marcususerbot_support")]])