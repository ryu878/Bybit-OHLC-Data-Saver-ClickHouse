# Bybit Trades Data Saver ClickHouse
Python script - Bybit Trades Data Saver using ClickHouse (ultra-fast solution for generating analytics)

Script will take the Trades data from Bybit REST API, save it to ClickHouse and then take it back from ClickHouse in JSON format.

[![Latest release](https://badgen.net/github/release/Naereen/Strapdown.js)](https://aadresearch.xyz)

## Disclaimer
<hr>
This project is for informational purposes only. You should not construe this information or any other material as legal, tax, investment, financial or other advice. Nothing contained herein constitutes a solicitation, recommendation, endorsement or offer by us or any third party provider to buy or sell any securities or other financial instruments in this or any other jurisdiction in which such solicitation or offer would be unlawful under the securities laws of such jurisdiction.

If you intend to use real money, use it at your own risk.

Under no circumstances will we be responsible or liable for any claims, damages, losses, expenses, costs or liabilities of any kind, including but not limited to direct or indirect damages for loss of profits.
<hr>

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

<code>pip install pybit</code>

## Contacts
Feel free to contact me via Discord: ryuryu#4087
or join my Discord group here: https://discord.gg/zSw58e9Uvf

<a href="https://discord.gg/zSw58e9Uvf">![image](https://user-images.githubusercontent.com/81808867/166115186-70de12b2-39fd-4eda-bb12-c1d8bec24ac6.png)</a>

To start trading on Bybit please register here: [https://bybit.com](https://www.bybit.com/en-US/invite?ref=P11NJW)<br>
On Binance here: [https://binance.com](https://www.binance.com/en/activity/referral-entry/CPA?fromActivityPage=true&ref=CPA_00T5P4X8R6)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
