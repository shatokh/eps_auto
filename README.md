Epsilion Trainer
=================
[![tests](https://github.com/esemi/epsilion_wars_mmorpg_automation/actions/workflows/tests.yml/badge.svg?branch=master)](https://github.com/esemi/epsilion_wars_mmorpg_automation/actions/workflows/tests.yml)
[![linters](https://github.com/esemi/epsilion_wars_mmorpg_automation/actions/workflows/linters.yml/badge.svg?branch=master)](https://github.com/esemi/epsilion_wars_mmorpg_automation/actions/workflows/linters.yml)

TODO GIF

The Epsilion Trainer is an automated tool that allows users to quickly and easily level up their character in [the Epsilion War MMORPG](https://t.me/epsilionwarbot?start=ref-537453818).
It automatically controls your character and instantly earns experience points, money and items.
With Epsilion Trainer you can quickly become the strongest player on the server.

Table of Contents
=================

* [What about the rules?](#what-about-the-rules)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
  * [Grinding](#grinding)
  * [Daily reward catcher](#daily-reward-catcher)
  * [Fishing](#fishing)
  * [Inventory](#inventory)
  * [What about the captcha?](#what-about-the-captcha)
* [Roadmap](#roadmap)
* [Developers](#developers)
  * [Run on server](#run-on-server)
  * [TData converter](#tdata-converter)
  * [Need more characters](#need-more-characters)


## What about the rules?
TL;DR Screw [the rules](https://teletype.in/@epsilionwar/HkPsNEfZL)


## Requirements
1. [Python 3.11 or later](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installation/) 
2. Telegram [API ID and token](https://docs.telethon.dev/en/stable/basic/signing-in.html#signing-in)
3. [Registration](https://t.me/epsilionwarbot?start=ref-537453818) on the game.


## Installation
Use the following commands to download and install the latest version of Epsilion Trainer
```shell
git clone https://github.com/esemi/epsilion_wars_mmorpg_automation.git
cd epsilion_wars_mmorpg_automation
pip install -U poetry pip setuptools
poetry install --only main
```

Place the telegram credentials (from the previous step) in the `.env` file using
```shell
cat > .env << EOF
telegram_api_id=U_API_ID
telegram_api_hash=U_API_HASH
EOF
```
The first time you use it, you'll need to log in to your Telegram account, but after that you'll be automatically logged in.

## Usage
### Grinding
Grinding will save you from having to fight annoying monsters in the hunting grounds. 
The Epsilion Trainer checks your health before searching for an enemy, choosing a random direction to attack and block, using combat tricks and collecting the reward. 
Sometimes you just need to take your character to repair equipment and open chests.

Just get your character to the right location, equip PVE and run the Epsilion Trainer with `grind`. 

If you prefer to hunt for a limited time, you can use `grind -t 30`: it will only hunt for 30 minutes, after which it will automatically shut down.


##### Settings
You can change the settings in the .env file as follows

`minimum_hp_level_for_grinding`: Minimum HP level to begin grinding. Default level is 75%.

`notifications_enabled`: Send alerts about important events. On by default.

`favorites_enabled`: Send messages to telegram myself-favorites chat too. On by default.

`auto_healing_enabled`: Using HP potions. On by default.

`stop_if_equip_broken`: Stop when something breaks. On by default.

`stop_if_captcha_fire`: Stop when captcha detected. Default is off.

`select_random_combo`: Choose a random combo shot from the available ones. On by default.

`skip_combo`: Skip the combo shots sometimes. On by default.

`captcha_solver_enabled`: Try to solve simple captcha automatically. On by default.

`use_backup_game_bot`: If the main game bot is down, you can try switching to the backup bot. Default is off.


### Daily reward catcher
If you find it inconvenient to keep track of your daily reward, you can use The Epsilon Trainer to handle it for you. 
The program automatically checks every hour to see if a reward has been made available, and it will attempt to collect it on your behalf. 

All you need to do is run The Epsilon Trainer and enter the `reward-catcher` command.


### Fishing
The Epsilion Trainer has a feature that allows your character to go fishing on their own. 
Give your character more rods, take him to the water and give him a `fishing` command.

The Epsilion Trainer will periodically check your character's energy level and start a fishing session when there's enough energy to do.
If any of your fishing rods break while fishing, the program will automatically replace them from your character's inventory.

Please keep in mind that it's important to only equip your character with fishing rods they can use effectively.


### Inventory
The Epsilion Trainer knows how to inventory your character's resources.
Run `inventory` and after a short time you will see a message in your favourite Telegram chat showing all the recipes for sale. 

By default it takes a list of recipes, but you can get a list of other resources by using the `inventory -t` flag.


### What about the captcha?
The Epsilion Trainer successfully solves simple text captcha. 
But it won't be able to solve numbers in a picture. 

Fortunately, there are some services that can help us. 
[One is already included](http://getcaptchasolution.com/r4gkdobk03). 
Just register there, top up your account with some $ and add your account key to settings.

You can have more information about registration and account funding on [their web site](http://getcaptchasolution.com/r4gkdobk03).   

You can also run the Epsilion Trainer in captcha-only help mode. Use the command `captcha-solver`.

In this mode, the tool will only help you solve the captcha automatically and nothing else.


##### Settings

`captcha_solver_enabled`: Try to solve simple captcha automatically. Enabled by default.

`notifications_enabled`: Send alerts about important events. On by default.

`anti_captcha_com_apikey`: your account key (ex: 172ea50b3d12345678de199546c66b20)


## Roadmap
- readme for customers (teletype page) and change link in settings/readme
- readme for customers (GIFs)
- farming (grind+autorepair+rewardcatcher) experimental tool
- publish as package + docs update


## Developers
### Run on server
To run The Epsilion Trainer on the server, you will need python and any supervisor (for automatic restart after failures, highly recommended).
For example:
```shell
adduser epsa
usermod -a -G supervisor epsa
cp ./etc/supervisor-example.conf /etc/supervisor/conf.d/epsa.conf
vi /etc/supervisor/conf.d/epsa.conf
service supervisor restart
```

### TData converter
If you plan to buy Telegram accounts, you will need a utility to convert credentials from tdata to .session (for Telethon library).
```shell
python etc/tdata_converter.py -f ~/.local/share/TelegramDesktop/tdata
```

### Need more characters
The game allows you to have three characters per telegram account. 
If you need more, you will need new telegram accounts. 

You can buy them or create them yourself.
The algorithm for self-registration is as follows
- get a temporary phone number, for [example here](https://sms-activate.org/?ref=6431353)
- create an account with this number from telegram mobile app (or TelegramX if you are out of slots)
- set 2fa password, email, nickname
- get your character into game using [a referral link](https://t.me/epsilionwarbot?start=ref-537453818)
- get authorisation for the Epsilion Trainer \([see step #2](#requirements)\)
- start grinding.

For a new account, I strongly recommend enabling the `slow_mode` flag in the settings. 
Otherwise the Telegram may block the account for too many requests.
