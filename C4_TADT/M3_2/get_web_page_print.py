#!/usr/bin/env python3


import urllib3

def get_web_page_print(url):
	http = urllib3.PoolManager()

	print("Retrieving URL:", url)
	response = http.request("GET", url)

	print("HTTP response code:", response.status, response.reason)
	print(response.data.decode("utf-8"))

if __name__ == "__main__":
	get_web_page_print("www.google.com")
