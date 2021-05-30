import requests
import datetime
import keyboard
import argparse


parser = argparse.ArgumentParser(description="Script to test internet connection")

def setup_parser():
    parser.add_argument('--url', help="URL to try to request as part of the test", type=str)
    parser.add_argument('--timeout', help="Timeout in seconds", type=int)

def test_connection(url="http://www.google.co.uk", timeout=10):
    try:
        rq = requests.get(url, timeout=timeout)
        # print("internet connected")
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        # print("internet disconnected")
        return False


def main():
    args = parser.parse_args()

    url="http://www.google.co.uk"
    if not args.url == None:
        url = args.url
    
    timeout = 10
    if not args.timeout == None:
        timeout = args.timeout
    
    print("Testing internet connection... press escape key to exit")
    quit = False
    start = datetime.datetime.now()
    
    file = open(f"./connection_test_{url.replace('http://','')}_{start.strftime('%Y.%m.%d_%H.%M.%S_%Z')}.csv", "w")
    file.write(f"date,time,connected\n")

    while not quit:
        now = datetime.datetime.now()
        str = f"{now.strftime('%Y-%m-%d %H.%M.%S.%f')} {test_connection(url, timeout)}"
        print(str)
        file.write(f"{str}\n".replace(' ',','))
        if keyboard.is_pressed('esc'):
            quit = True
    file.close()
        

if __name__ == '__main__':
    setup_parser()
    main()
