#!/usr/bin/env python3
# Day 62

import json

data = {
    "server_list": [
        {
            "host": "server1",
            "eventlog_dir": "/applications/spark/hs_1"
        },
        {
            "host": "server2",
            "eventlog_dir": "/data/applications/spark/hs_2"
        }
    ]
}

def read_json_block(data):
    for server in data.get("server_list", []):
        host = server.get("host", "Unknown Host")
        eventlog_dir = server.get("eventlog_dir", "Unknown Eventlog Directory")
        print(f"Host: {host}, Eventlog Dir: {eventlog_dir}")

if __name__ == "__main__":
    read_json_block(data)
