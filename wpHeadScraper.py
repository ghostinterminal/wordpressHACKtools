import requests
import argparse
from bs4 import BeautifulSoup
from termcolor import colored

parser = argparse.ArgumentParser(description="A simple script to scrap the head of a wordpress website.")
parser.add_argument('-u', '--url', help="Url here", type=str)
parser.add_argument('-t', '--tag', help="Tag to scrap", type=str)
args = parser.parse_args()

headers = {'User-agent':'Mozzila/5.0'}

def main():
	req = requests.get(args.url, headers=headers)
	soup = BeautifulSoup(req.text, 'lxml')

	tags = soup.head.find_all(args.tag)
	if len(tags) != 0:
		print ''
		print colored("Thank GOD !!!, This is not empty..", color="green")
		print ''
	print colored('============================== {0}S ======================================================================================='.format(args.tag.upper()), color='cyan')
	for tag in tags:
		print tag
	print colored('============================== {0}S ======================================================================================='.format(args.tag.upper()), color='cyan')




main()

