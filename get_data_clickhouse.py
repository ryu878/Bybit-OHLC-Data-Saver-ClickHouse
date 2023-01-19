# Ryuryu's Bybit OHLC Data Saver 
# Clickhouse Edition (Production Mode #6973)
# -------------------------------------------
# (C) 2023 Ryan Hayabusa 
# Github: https://github.com/ryu878 
# Discord: ryuryu#4087
# Mail: ev4AR2xihu3xXcdbYy5djGpfe01@gmail.com
# Web: https://aadresearch.xyz
# Discord: ryuryu#4087
# -------------------------------------------


# sudo apt-get install apt-transport-https ca-certificates dirmngr
# sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv E0C56BD4

# echo "deb https://repo.clickhouse.tech/deb/stable/ main/" | sudo tee \
#    /etc/apt/sources.list.d/clickhouse.list
# sudo apt-get update

# sudo apt-get install -y clickhouse-server clickhouse-client
# sudo service clickhouse-server start
# clickhouse-client
# python3 -m venv .pb-ch && source /.pb-ch/bin/activate
# pip install clickhouse-driver
# pip install pandas
# pip install pybit

import json
from config import *
import pandas as pd
from pybit import inverse_perpetual
from clickhouse_driver import Client


session_unauth_inverse = inverse_perpetual.HTTP(endpoint=endpoint)

client = Client(host=host,password=password)
show_databases = client.execute('SHOW DATABASES')
print(show_databases)
client.execute(f'DROP DATABASE IF EXISTS {database}')



# Get Data from Bybit REST API
data = session_unauth_inverse.query_kline(symbol=symbol,interval=interval,limit=limit,from_time=1654104498)
result = data['result']
print(result)

df = pd.DataFrame(result)
df = df.drop(columns = ['turnover','volume'])
df = df.assign(oth = df['open_time'])
df['oth'] = pd.to_datetime(df['oth'], unit='s', origin='unix')
print(df)


# Create DataBase
client.execute(f'DROP DATABASE IF EXISTS {database}')
client.execute(f'CREATE DATABASE {database}')
show_databases = client.execute('SHOW DATABASES')
print(show_databases)

client = Client(host=host, user=user, password=password, port=port, database=database, settings={'columnar': True})

client.execute(f'''CREATE TABLE {table} (
    symbol String,
    interval String,
    open_time Int32,
    open String,
    high String,
    low String,
    close String) 
    ENGINE = Memory'''
    )

show_tables = client.execute(f'SHOW TABLES FROM {database}')
print(show_tables)

columns = client.execute(f"SELECT * FROM {table}", with_column_types="True")

print(columns)

client.execute(f"INSERT INTO {table} VALUES", df.to_dict('records'), types_check=True)

clickhouse_data = client.execute(f"SELECT * FROM {table}")
clickhouse_data = json.dumps(clickhouse_data)

print(clickhouse_data)
