<p align="center">
  <img src="./resources/extras/logo_readme.jpg" alt="Badhacker98.logo">
</p>
<h1 align="center">
  <b>ʙᴀᴅʙᴏʏ - ᴜsᴇʀʙᴏᴛ</b>
</h1>

<b>ᴀ sᴛᴀʙʟᴇ ᴘʟᴜɢɢᴀʙʟᴇ Tᴇʟᴇɢʀᴀᴍ ᴜsᴇʀʙᴏᴛ + Vᴏɪᴄᴇ & Vɪᴅᴇᴏ Cᴀʟʟ ᴍᴜsɪᴄ ʙᴏᴛ, ʙᴀsᴇᴅ ᴏɴ Tᴇʟᴇᴛʜᴏᴛ.</b>

[![](https://img.shields.io/badge/Badhacker98/BadBoy-v0.8-crimson)](#)
[![Stars](https://img.shields.io/github/stars/Badhacker98/BadBoy?style=flat-square&color=yellow)](https://github.com/Badhacker98/BadBoy/stargazers)
[![Forks](https://img.shields.io/github/forks/Badhacker98/BadBoy?style=flat-square&color=orange)](https://github.com/Badhacker98/BadBoy/fork)
[![Size](https://img.shields.io/github/repo-size/Badhacker98/BadBoy?style=flat-square&color=green)](https://github.com/Badhacker98/BadBoy/)   
[![Python](https://img.shields.io/badge/Python-v3.10.3-blue)](https://www.python.org/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/Badhacker98/BadBoy/graphs/commit-activity)
[![Docker Pulls](https://img.shields.io/docker/pulls/theBadhacker98/BadBoy?style=flat-square)](https://img.shields.io/docker/pulls/theBadhacker98/BadBoy?style=flat-square)   
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/Badhacker98/BadBoy)
[![Contributors](https://img.shields.io/github/contributors/Badhacker98/BadBoy?style=flat-square&color=green)](https://github.com/Badhacker98/BadBoy/graphs/contributors)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)
[![License](https://img.shields.io/badge/License-AGPL-blue)](https://github.com/Badhacker98/BadBoy/blob/main/LICENSE)   
[![Sparkline](https://stars.medv.io/Badhacker98/BadBoy.svg)](https://stars.medv.io/Badhacker98/BadBoy)
----

# Deploy
- [Heroku](#deploy-to-heroku)
- [Okteto](#deploy-to-okteto)
- [Local Machine](#deploy-locally)

# Documentation 
[![Documentation](https://img.shields.io/badge/Documentation-Badhacker98/BadBoy-blue)](http://Badhacker98/BadBoy.tech/)

# Tutorial 
- Full Tutorial - [![Full Tutorial](https://img.shields.io/badge/Watch%20Now-blue)](https://www.youtube.com/watch?v=0wAV7pUzhDQ)

- Tutorial to get Redis URL and password - [here.](./resources/extras/redistut.md)
---

## Deploy to Heroku
Get the [Necessary Variables](#Necessary-Variables) and then click the button below!  

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://deploy.Badhacker98/BadBoy.tech)

## Deploy to Okteto
Get the [Necessary Variables](#Necessary-Variables) and then click the button below!

[![Develop on Okteto](https://okteto.com/develop-okteto.svg)](https://cloud.okteto.com/deploy?repository=https://github.com/Badhacker98/BadBoy)

## Deploy Locally
- [Traditional Method](#local-deploy---traditional-method)
- [Easy Method](#local-deploy---easy-method)
- [Badhacker98/BadBoy CLI](#Badhacker98/BadBoy-cli)

### Local Deploy - Easy Method
- Linux - `wget -O locals.py https://git.io/JY9UM && python3 locals.py`
- Windows - `cd desktop ; wget https://git.io/JY9UM -o locals.py ; python locals.py`
- Termux - `wget -O install-termux https://tiny.BadBoy.tech/termux && bash install-termux`

### Local Deploy - Traditional Method
- Get your [Necessary Variables](#Necessary-Variables)
- Clone the repository:    
`git clone https://github.com/Badhacker98/BadBoy.git`
- Go to the cloned folder:    
`cd BadBoy`
- Create a virtual env:      
`virtualenv -p /usr/bin/python3 venv`
`. ./venv/bin/activate`
- Install the requirements:      
`pip 3 install -U -r re*/st*/optional-requirements.txt`
`pip 3 install -U -r requirements.txt`
- Generate your `SESSION`:
  - For Linux users:
    `bash sessiongen`
     or
    `wget -O session.py https://git.io/JY9JI && python3 session.py`
  - For Termux users:
    `wget -O session.py https://git.io/JY9JI && python session.py`
  - For Windows Users:
`cd desktop ; wget https://git.io/JY9JI -o BadBoy.py ; python BadBoy.py`
- Fill your details in a `.env` file, as given in [`.env.sample`](https://github.com/Badhacker98/BadBoy/blob/main/.env.sample).
(You can either edit and rename the file or make a new file named `.env`.)
- Run the bot:
  - Linux Users:
   `bash startup`
  - Windows Users:
    `python 3 -m pyBadhacker98/BadBoy`

---

## Necessary Variables
- `SESSION` - SessionString for your accounts login session. Get it from [here](#Session-String)

One of the following database:
- For **Redis** (tutorial [here](./resources/extras/redistut.md))
  - `REDIS_URI` - Redis endpoint URL, from [redislabs](http://redislabs.com/).
  - `REDIS_PASSWORD` - Redis endpoint Password, from [redislabs](http://redislabs.com/).
- For **MONGODB**
  - `MONGO_URI` - Get it from [mongodb](https://mongodb.com/atlas).
- For **SQLDB**
  - `DATABASE_URL`- Get it from [elephantsql](https://elephantsql.com).

## Session String
Different ways to get your `SESSION`:
* Linux : `wget -O session.py https://shorturl.at/dM7bm && python3 session.py`
* PowerShell : `cd desktop ; wget https://shorturl.at/dM7bm ; python BadBoy.py`
* Termux : `wget -O session.py https://shorturl.at/dM7bm && python session.py`
* TelegramBot : [@SessionGeneratorBot](http://t.me/Pbxx_String_Bot)

---

# License
[![License](https://www.gnu.org/graphics/agplv3-155x51.png)](LICENSE)   
BadBoy is licensed under [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) v3 or later.

---

>🤌🏻 ᴍᴀᴅᴅ ʙʏ🌸 [⎯꯭̽🇨🇦꯭꯭ ⃪В꯭α꯭∂ ꯭м꯭υ꯭η∂꯭α_꯭آآ⎯꯭ ꯭̽🌸](https://t.me/ll_BAD_MUNDA_ll)
