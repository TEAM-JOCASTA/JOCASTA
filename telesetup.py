# Error Fixed by @krish1303y
#!/usr/bin/env python3
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.
print("""
 ──╔╦═══╦═══╦═══╦═══╦════╦═══╗
 ──║║╔═╗║╔═╗║╔═╗║╔═╗║╔╗╔╗║╔═╗║
 ──║║║─║║║─╚╣║─║║╚══╬╝║║╚╣║─║║
 ╔╗║║║─║║║─╔╣╚═╝╠══╗║─║║─║╚═╝║
 ║╚╝║╚═╝║╚═╝║╔═╗║╚═╝║─║║─║╔═╗║
 ╚══╩═══╩═══╩╝─╚╩═══╝─╚╝─╚╝─╚╝ """)
                         
print("Telethon (docs.telethon.dev)")
print("Telethon UserBot https://t.me/JOCASTA_SUPPORT")
print("Generating Jocasta  String Session\n\n")
try:
    from telethon.sessions import StringSession
    from telethon.sync import TelegramClient
except Exception:
    print("Telethon Not Found. Installing Now.")
    import os
    os.system("pip3 install telethon")
    from telethon.sessions import StringSession
    from telethon.sync import TelegramClient
print("Put Your APP_ID Here Get It With telegram.org")
APP_ID = int(input("Enter APP ID here: \n"))
print("\n\nPut your API_HASH Which u will get with your APP_ID")
API_HASH = input("Enter API HASH here: \n")
with TelegramClient(StringSession(), APP_ID, API_HASH) as joca:
    string_jocasta = joca.session.save()
    jocasta = joca.send_message(
        "me",
        f"__Your Jocasta String Session__\n\n`{string_jocasta}`\n\n**For Support @JOCASTA_SUPPORT**"
    )
    jocasta.reply(
        "⬆️**Thanks For Choosing \n  `Jocasta!` \n Pls give us feed back [Here] https://t.me/TBH_NETWORK It mean a lot for us **"
    )
    print(
        "\n\nThanks For Using Jocasta Repl\n\n For Support Join @JOCASTA_SUPPORT"
    )
