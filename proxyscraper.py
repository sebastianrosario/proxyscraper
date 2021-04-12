from urllib.request import urlopen
import sys
import re

ip_regex = "\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}:\\d+"
u_url = sys.argv[2]
u_socket_type = sys.argv[1]


def find_ip(url):
    open_page = urlopen(url)
    html_bytes = open_page.read()
    html = html_bytes.decode("utf-8")
    raw_ip = re.findall(ip_regex, html)

    if raw_ip:
        print("Found {} IPs".format(len(raw_ip)))
    else: 
        print("No IPs found.")

    return raw_ip


def arr_to_final(arr, socket_type):
    final_arr = []
    for ip in arr: 
        new_ip = ip.split(':')
        final_arr.append("{}\t{}\t{}".format(socket_type, new_ip[0], new_ip[1])) 

    return final_arr


def write_to_proxy(arr):
    with open('/etc/proxychains.conf', 'a') as file:
        for formatted_string in arr:
            file.write("{}\n".format(formatted_string))
            


if __name__ == "__main__":
    if len(sys.argv) == 3: 
        proxy_arr = []
        
        proxy_arr += find_ip(u_url)
        formatted_arr = arr_to_final(proxy_arr, u_socket_type)
        write_to_proxy(formatted_arr)
    else:
        print("Syntax: python3 proxyscraper.py [http/socks4/socks5] [website]")


    print("Added {} {} proxies to proxychains.conf".format(len(formatted_arr), u_socket_type))

