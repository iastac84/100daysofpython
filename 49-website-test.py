#!/usr/bin/env python3
# Day 49

'''
Here is a simple Python script that uses the requests library to check if a website is reachable or not by making an HTTP GET request. If the request is successful (status code 200), it considers the website to be reachable. Otherwise, it's considered unreachable.

Before running the script, make sure you have the requests library installed. You can install it using the following command:
pip install requests

'''
import requests

def check_website_reachable(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError:
        return False

url_to_check = "https://www.ianstacey.net"  # Replace with the URL you want to check

if check_website_reachable(url_to_check):
    print(f"The website {url_to_check} is reachable.")
else:
    print(f"The website {url_to_check} is NOT reachable.")

