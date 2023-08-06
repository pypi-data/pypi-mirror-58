# Technic

A trading technical analysis library for python.

## Dependencies

1. pandas
2. numpy

## Install

`pip install technic`

## Supported Technical Functions

| Indicator             | Status      |
| --------------------- | ----------- |
| SMA                   | DONE        |
| EMA                   | DONE        |
| RSI                   | DONE        |
| ATR                   | DONE        |
| STD                   | DONE        |
| MACD                  | DONE        |
| BOLLINGER BANDS       | DONE        |
| KELTNER CHANNELS      | DONE        |
| SQUEEEZE              | COMING SOON |
| STOCHASTIC OSCILLATOR | COMING SOON |

## Examples

```python

import pandas as pd
import technic as ta



csv_file = 'PATH_TO_YOUR OHLCV CSV DATA'

# Dataframe containing OHLCV data
df = pd.read_csv(csv_file)


# SMA
sma = ta.tsma(df['close'], 50)

# EMA
ema = ta.tsma(df['close'], 10)

# RSI
rsi = ta.trsi(df['close'], 14)

# ATR
atr = ta.tatr(df['close'], df['high'], df['low'], w=21)

# MACD
df_macd = ta.tmacd(df['close'], w_slow=26, w_fast=12, w_signal=9)

# Bollinger Bands
df_bbands = ta.tbollingerbands(df['close'], w=21, std_multiplier=2)

# Keltner Channels
df_kelt = ta.tkeltnerchannels(df['close'], df['high'], df['low'], w=21, atr_multiplier=2)

```
