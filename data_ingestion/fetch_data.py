"""Download or stream market data for demo purposes."""

import argparse
import csv
import os

# the fetch_data module may require yfinance

# placeholder: implement real downloads

def download_public(pair, out_dir='data'):
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, f'{pair}.csv')
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp','price','volume'])
        # write dummy rows
        for i in range(100):
            writer.writerow([i, 100+i, 1])
    print(f'Wrote sample data to {path}')


def stream_yfinance(pair):
    import yfinance as yf
    # download last 5 days of minute data
    ticker_a, ticker_b = pair.split('-')
    print(f'Downloading 5d 1m data for {ticker_a} and {ticker_b}')
    data_a = yf.download(ticker_a, period='5d', interval='1m')
    data_b = yf.download(ticker_b, period='5d', interval='1m')
    out_dir = 'data'
    os.makedirs(out_dir, exist_ok=True)
    path_a = os.path.join(out_dir, f'{ticker_a}.csv')
    path_b = os.path.join(out_dir, f'{ticker_b}.csv')
    data_a.to_csv(path_a)
    data_b.to_csv(path_b)
    print(f'Wrote {path_a} and {path_b}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--pair', required=True)
    parser.add_argument('--source', choices=['public','yfinance'], default='public')
    args = parser.parse_args()
    if args.source == 'public':
        download_public(args.pair)
    else:
        stream_yfinance(args.pair)
