#!/usr/bin/env python3
"""
------------------------------------------------------------------------------
	CTFR - 04.03.18.02.10.00 - Sheila A. Berta (UnaPibaGeek)
------------------------------------------------------------------------------
"""

import re
import json
import requests

def parse_args():
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('-d', '--domain', type=str, required=True, help="Target domain.")
	parser.add_argument('-o', '--output', type=str, help="Output file.")
	return parser.parse_args()

def clear_url(target):
	return re.sub('.*www\.','',target,1).split('/')[0].strip()

def save_subdomains(subdomain,output_file):
	with open(output_file,"a") as f:
		f.write(subdomain + '\n')
		f.close()

def main():
	args = parse_args()

	subdomains = []
	target = clear_url(args.domain)
	output = args.output

	req = requests.get("https://crt.sh/?q=%.{d}&output=json".format(d=target))

	if req.status_code != 200:
		print("[X] Information not available!") 
		exit(1)

	json_data = json.loads('[{}]'.format(req.text.replace('}{', '},{')))

	for (key,value) in enumerate(json_data):
		subdomains.append(value['name_value'])

	subdomains = sorted(set(subdomains))

	for subdomain in subdomains:
		print("{s}".format(s=subdomain))
		if output is not None:
			save_subdomains(subdomain,output)

main()
