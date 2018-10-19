#!/usr/bin/env python
# -*- coding: utf-8 -*-

import websocket
import ssl
import argparse

parser = argparse.ArgumentParser(description="This is a simple script of websocket client")
parser.add_argument("-t", metavar="TARGET HOST", help="target host", required=True)
parser.add_argument("-p", metavar="TARGET PORT", type=int, help="target port", required=True)
parser.add_argument("-useproxy", metavar="proxy", help="proxyIP:proxyPORT (ex:127.0.0.1:8080)")

args = parser.parse_args()

targetIP = args.t
targetPort = str(args.p)
webconsoleURL = "wss://" + targetIP + ":" + targetPort + "/webconsole/wc"

# create scoket
if args.useproxy == None:
	ws = websocket.create_connection(
	webconsoleURL,
	sslopt={"cert_reqs" : ssl.CERT_NONE})

else:
	proxyIP = args.useproxy[:(args.useproxy).find(":")]
	proxyPort = args.useproxy[(args.useproxy).find(":")+1:]

	ws = websocket.create_connection(
		webconsoleURL,
		http_proxy_host = proxyIP,
		http_proxy_port = proxyPort,
		sslopt={"cert_reqs" : ssl.CERT_NONE})

ws.send("{\"message\":\"Hello World!\"}")
result = ws.recv()
print(result)
ws.close()
