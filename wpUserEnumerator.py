import requests
from termcolor import colored
import argparse


# Setting fags..

parser = argparse.ArgumentParser(description="A simple script to enumerate the wordpress users.")
parser.add_argument('-u', '--url', help='The wordpress webiste URL', type=str)
parser.add_argument('-s', '--start', default=0 ,help='The nth user to start', type=int)
parser.add_argument('-e', '--end', default=500, help='The nth user to stop', type=int)

args = parser.parse_args()

def Help():
    Help = '''\n
    \tHELP: python wpUserEnumerator.py <url>
    '''
    return Help

def main():
    url = args.url
    suffix = '/wp-json/wp/v2/users/'
    print colored('======================================================================================', color='blue')
    print colored('|Url|\t\t\t\t\t\t\t\t|Status Code|', color='yellow')
    print colored('======================================================================================', color='blue')
    for n in range(args.start, args.end+1):
        full_addr = url+suffix+str(n)
        req = requests.get(full_addr, headers={'User-agent':'Mozzila/5.0'})
        #user = dict(req.text)['User']
        if req.status_code == 200:
            print colored('{0}\t\t\t{1}'.format(full_addr, req.status_code), color='green')
        
        if req.status_code == 401:
            print colored('{0}\t\t\t{1}'.format(full_addr, req.status_code), color='cyan')
        
        print colored('{0}\t\t\t{1}'.format(full_addr, req.status_code), color='red')
    print colored('======================================================================================', color='blue')

main()

    


