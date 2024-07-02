

import re

from . import *

STRINGS = {
    1: """🎇 **Tʜᴀɴᴋs ғᴏʀ Dᴇᴘʟᴏʏɪɴɢ BᴀᴅBᴏʏ Usᴇʀʙᴏᴛ!**

• Hᴇʀᴇ, ᴀʀᴇ ᴛʜᴇ Sᴏᴍᴇ Bᴀsɪᴄ sᴛᴜғғ ғʀᴏᴍ, ᴡʜᴇʀᴇ ʏᴏᴜ ᴄᴀɴ Kɴᴏᴡ, ᴀʙᴏᴜᴛ ɪᴛs Usᴀɢᴇ.""",
    2: """🎉**Aʙᴏᴜᴛ BᴀᴅBᴏʏ**

🧿 BᴀᴅBᴏʏ ɪs Pʟᴜɢɢᴀʙʟᴇ ᴀɴᴅ ᴘᴏᴡᴇʀғᴜʟ Tᴇʟᴇᴛʜᴏɴ Usᴇʀʙᴏᴛ, ᴍᴀᴅᴇ ɪɴ Pʏᴛʜᴏɴ ғʀᴏᴍ Sᴄʀᴀᴛʜ. Iᴛ ɪs Aɪᴍᴇᴅ ᴛᴏ Iɴᴄʀᴇᴀsᴇ Sᴇᴄᴜʀɪᴛʏ ᴀʟᴏɴɢ ᴡɪᴛʜ Aᴅᴅɪᴛɪᴏɴ ᴏғ Oᴛʜᴇʀ Usᴇғᴜʟ Fᴇᴀᴛᴜʀᴇs.

❣ **Mᴀᴅᴇ ʙʏ** 🎉 @PBX_PERMOT """,
    3: """**💡• FAQs •**

-> [Username Tracker](https://t.me/BADBOYPLUGIN/63)
-> [Keeping Custom Addons Repo](soon)
-> [Disabling Deploy message](https://t.me/BADBOYPLUGIN/64)
-> [About Inline PmPermit](https://t.me/BADBOYPLUGIN/65)
-> [About Dual Mode](https://t.me/BADBOYPLUGIN/66)
-> [Custom Thumbnail](https://t.me/BADBOYPLUGIN/67)
-> [About FullSudo](https://t.me/BADBOYPLUGIN/68)
-> [Setting Up PmBot](https://t.me/BADBOYPLUGIN/69)
-> [Also Check](https://t.me/BADBOYPLUGIN/70)

**• Tᴏ Kɴᴏᴡ Aʙᴏᴜᴛ Uᴘᴅᴀᴛᴇs**
  - Join @PBX_PERMOT """,
    4: f"""• `Tᴏ Kɴᴏᴡ Aʟʟ Aᴠᴀɪʟᴀʙʟᴇ Cᴏᴍᴍᴀɴᴅs`

  - `{HNDLR}ʜᴇʟᴘ`
  - `{HNDLR}ᴄᴍᴅs`""",
    5: """• **Fᴏʀ Aɴʏ Oᴛʜᴇʀ Qᴜᴇʀʏ ᴏʀ Sᴜɢɢᴇsᴛɪᴏɴ**
  - ᴍᴏᴠᴇ ᴛᴏ **@PBX_CHAT**.

• Tʜᴀɴᴋs ғᴏʀ Rᴇᴀᴄʜɪɴɢ ᴛɪʟʟ END.""",
}


@callback(re.compile("initft_(\\d+)"))
async def init_depl(e):
    CURRENT = int(e.data_match.group(1))
    if CURRENT == 5:
        return await e.edit(
            STRINGS[5],
            buttons=Button.inline("<< Back", "initbk_4"),
            link_preview=False,
        )

    await e.edit(
        STRINGS[CURRENT],
        buttons=[
            Button.inline("<<", f"initbk_{str(CURRENT - 1)}"),
            Button.inline(">>", f"initft_{str(CURRENT + 1)}"),
        ],
        link_preview=False,
    )


@callback(re.compile("initbk_(\\d+)"))
async def ineiq(e):
    CURRENT = int(e.data_match.group(1))
    if CURRENT == 1:
        return await e.edit(
            STRINGS[1],
            buttons=Button.inline("Start Back >>", "initft_2"),
            link_preview=False,
        )

    await e.edit(
        STRINGS[CURRENT],
        buttons=[
            Button.inline("<<", f"initbk_{str(CURRENT - 1)}"),
            Button.inline(">>", f"initft_{str(CURRENT + 1)}"),
        ],
        link_preview=False,
    )
    
