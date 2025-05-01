#!/usr/bin/env python3


import urllib3

def get_web_page(url):
	http = urllib3.PoolManager()
	response = http.request("GET", url)
	print(response.data.decode("utf-8"))

if __name__ == "__main__":
	get_web_page("www.google.com")
