#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# Clean screen on Windows
if os.name == "nt":
    os.system("cls")

# Clean screen on macOS and Linux
else:
    os.system("clear")

import os
import requests

# Coinbase API endpoint
coinbase_url = "https://api.coinbase.com/v2/prices/"

# Binance API endpoint
binance_url = "https://api.binance.com/api/v3/ticker/price"

# fiwind BTC API endpoint

fiwind_btc_url = "https://criptoya.com/api/fiwind/btc/usd/0.5"
fiwind_eth_url = "https://criptoya.com/api/fiwind/eth/usd/0.5"
fiwind_ada_url = "https://criptoya.com/api/fiwind/ada/ars/0.5"

# Cryptocurrencies to retrieve
cryptos = ["BTC", "ETH", "ADA"]

print("")
print("\033[94mCoinbase Buy Prices\033[0m")
print("______________________________")
print("")

# Retrieve prices from Coinbase
for crypto in cryptos:
    response = requests.get(coinbase_url + f"{crypto}-USD/spot")
    coinbase_price = response.json()["data"]["amount"]
    coinbase_price_float = float(coinbase_price)
    coinbase_price_2decimals = "{:.2f}".format(coinbase_price_float)
    print(f"Coinbase {crypto} price in USDT: ${coinbase_price_2decimals}")

print("______________________________")

print("")
print("\033[93mBinance Buy Prices\033[0m")
print("______________________________")
print("")

# Retrieve prices from Binance
for crypto in cryptos:
    response = requests.get(binance_url, params={"symbol": f"{crypto}USDT"})
    binance_price = response.json()["price"]
    binance_price_float = float(binance_price)
    binance_price_2decimals = "{:.2f}".format(binance_price_float)
    print(f"Binance {crypto} price in USDT: ${binance_price_2decimals}")

print("______________________________")

print("")
print("\033[93mfiwind Buy Prices\033[0m")
print("______________________________")
print("")

# Retrieve prices from fiwind

# BTC price
response = requests.get(fiwind_btc_url, params={"bid": f"BTC"})
fiwind_btc_price = response.json()["bid"]
fiwind_btc_price_float = float(fiwind_btc_price)
fiwind_btc_price_2decimals = "{:.2f}".format(fiwind_btc_price_float)
print(f"fiwind BTC price in USD: ${fiwind_btc_price_2decimals}")

# ETH price
response = requests.get(fiwind_eth_url, params={"bid": f"ETH"})
fiwind_eth_price = response.json()["bid"]
fiwind_eth_price_float = float(fiwind_eth_price)
fiwind_eth_price_2decimals = "{:.2f}".format(fiwind_eth_price_float)
print(f"fiwind ETH price in USD: ${fiwind_eth_price_2decimals}")

# ADA price
response = requests.get(fiwind_ada_url, params={"bid": f"ADA"})
fiwind_ada_price = response.json()["bid"]
fiwind_ada_price_float = float(fiwind_ada_price)
fiwind_ada_price_2decimals = "{:.2f}".format(fiwind_ada_price_float)
print(f"fiwind ADA price in ARS: ${fiwind_ada_price_2decimals}")

print("______________________________")

print("")
print("Thank you for using FNX Labs Crypto Prices v0.1 Alpha")
print("")
