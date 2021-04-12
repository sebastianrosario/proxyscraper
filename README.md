# proxyscraper
Uses regex to match IP address and port combinations in a given web page, appends the proxies to /etc/proxychains.conf
For use in Linux environment where proxychains is already installed.

Proxy regex matches things formatted```[IP]:[PORT]```


# syntax
```python3 proxyscraper.py [http/socks4/socks5] [WEBSITE]```
