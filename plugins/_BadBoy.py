# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from telethon.errors import (
    BotMethodInvalidError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
)

from . import LOG_CHANNEL, LOGS, Button, asst, eor, get_string, ultroid_cmd

REPOMSG = """
• **ʙᴀᴅʙᴏʏ ʀᴇᴘᴏ** •\n
• Repo - [Click Here](https://github.com/Badhacker98/BadBoy)
• Addons - [Click Here](https://github.com/TeamUltroid/UltroidAddons)
• Support - @PBX_CHAT
"""

RP_BUTTONS = [
    [
        Button.url(get_string("bot_3"), "https://github.com/TeamUltroid/Ultroid"),
        Button.url("Addons", "https://github.com/badmunda98/BadBoyAddons"),
    ],
    [Button.url("Support Group", "https://t.me/PBX_CHAT")],
]

ULTSTRING = """🎇 **ᴛʜᴀɴᴋs ғᴏʀ Dᴇᴘʟᴏʏɪɴɢ Uʟᴛʀᴏɪᴅ Usᴇʀʙᴏᴛ!**

• ʜᴇʀᴇ, ᴀʀᴇ ᴛʜᴇ Sᴏᴍᴇ Bᴀsɪᴄ sᴛᴜғғ ғʀᴏᴍ, ᴡʜᴇʀᴇ ʏᴏᴜ ᴄᴀɴ Kɴᴏᴡ, ᴀʙᴏᴜᴛ ɪᴛs Usᴀɢᴇ."""


@ultroid_cmd(
    pattern="repo$",
    manager=True,
)
async def repify(e):
    try:
        q = await e.client.inline_query(asst.me.username, "")
        await q[0].click(e.chat_id)
        return await e.delete()
    except (
        ChatSendInlineForbiddenError,
        ChatSendMediaForbiddenError,
        BotMethodInvalidError,
    ):
        pass
    except Exception as er:
        LOGS.info(f"Error while repo command : {str(er)}")
    await e.eor(REPOMSG)


@ultroid_cmd(pattern="ultroid$")
async def useUltroid(rs):
    button = Button.inline("Start >>", "initft_2")
    msg = await asst.send_message(
        LOG_CHANNEL,
        ULTSTRING,
        file="https://telegra.ph/file/312778d594ebfda4ae8d4.jpg",
        buttons=button,
    )
    if not (rs.chat_id == LOG_CHANNEL and rs.client._bot):
        await eor(rs, f"**[Click Here]({msg.message_link})**")
