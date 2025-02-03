# Bybit Trades Data Saver ClickHouse
Python script - Bybit Trades Data Saver using ClickHouse (ultra-fast solution for generating analytics)

Script will take the Trades data from Bybit REST API, save it to ClickHouse and then take it back from ClickHouse in JSON format.

[![Latest release](https://badgen.net/github/release/Naereen/Strapdown.js)](https://aadresearch.xyz)


## Install

First install ClickHoouse:

<code>sudo apt-get install apt-transport-https ca-certificates dirmngr</code>

<code>sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv E0C56BD4</code>

<code>echo "deb https://repo.clickhouse.tech/deb/stable/ main/" | sudo tee \
   /etc/apt/sources.list.d/clickhouse.list</code>
   
<code>sudo apt-get update</code>

<code>sudo apt-get install -y clickhouse-server clickhouse-client</code>

And run it:

<code>sudo service clickhouse-server start</code>

<code>clickhouse-client</code>

Next create python virtual environment and activate it:

<code>python3 -m venv .pb-ch && source .pb-ch/bin/activate</code>

And then install necessary libraries:

<code>pip install clickhouse-driver</code>

<code>pip install pandas</code>

<code>pip install pybit==2.4.1</code>


## Disclaimer
This project is for informational and educational purposes only. You should not use this information or any other material as legal, tax, investment, financial or other advice. Nothing contained here is a recommendation, endorsement or offer by me to buy or sell any securities or other financial instruments. If you intend to use real money, use it at your own risk. Under no circumstances will I be responsible or liable for any claims, damages, losses, expenses, costs or liabilities of any kind, including but not limited to direct or indirect damages for loss of profits.

## Contacts
I develop trading bots of any complexity, dashboards and indicators for crypto exchanges, forex and stocks.
To contact me:

Discord: https://discord.gg/zSw58e9Uvf

Join Bybit and receive up to $6,045 in Bonuses: https://www.bybit.com/invite?ref=X2PZB


## VPS for bots and scripts
I prefer using DigitalOcean. 

To get $200 in credit over 60 days use my ref link: https://m.do.co/c/3d7f6e57bc04

