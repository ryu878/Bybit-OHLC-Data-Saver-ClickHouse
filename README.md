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


***

## 📄 License
MIT License - Feel free to modify and distribute.


## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check issues page.

## ⚠️ Disclaimer

> This project is for informational and educational purposes only. You should not use this information or any other material as legal, tax, investment, financial, or other advice. Nothing contained here is a recommendation, endorsement, or offer by me to buy or sell any securities or other financial instruments.
>
> **If you intend to use real money, use it at your own risk.**
>
> Under no circumstances will I be responsible or liable for any claims, damages, losses, expenses, costs, or liabilities of any kind, including but not limited to direct or indirect damages for loss of profits.


***

## 📌 Quantitative Researcher | Algorithmic Trader | Trading Systems Architect

Quantitative researcher and trading systems engineer with end-to-end ownership of systematic strategies — from research and statistical validation to low-latency execution and production deployment.

Core focus areas:
- Systematic strategy design and validation
- Market microstructure analysis (order book dynamics, liquidations, volume, delta, liquidity, spread behavior, funding)
- Backtesting framework development (tick-level and historical data)
- Execution engine architecture and order lifecycle management
- Real-time market data processing
- Risk-aware system design
- Production-grade trading infrastructure (24/7 environments)

Experience across crypto (CEX, DEX), FX, and exchange-traded markets.

## Technical Stack

- Languages: Python, C++, MQL5
- Execution & Connectivity: REST, WebSocket, FIX
- Infrastructure: Linux, Docker, Redis, PostgreSQL, ClickHouse
- Analytics: NumPy, Pandas, custom backtesting frameworks

## Contact

Email: ryu8777@gmail.com

***
