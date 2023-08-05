#!/usr/bin/env python
# coding=utf8
# v0.1

from colorama import Fore,Back,init
import sys
import os
__version__ = "0.1"

HOME = os.environ['HOME']
CONFIG_PATH = os.path.join(HOME, ".ssh", "config")
user_info = {}

def gather_ssh_info():
    """
    gather ssh information
    """
    try:
        with open(CONFIG_PATH) as fd:
            for line in fd:
                line = line.strip()
                if line.startswith('Host ') and '*' not in line:
                    hostname = line.split()[1]
                if line.startswith('HostName') and '*' not in line:
                    host = line.split()[1]
                    if hostname and host:
                        user_info[hostname] = host
                    hostname = host = ''
    except Exception as e:
        print('Error, %s' %e)
        sys.exit()

def colorful_print():
    init(autoreset=True)
    print(Fore.RED + '{0:^60}'.format('Command Line SSH Quick Link to Server'))
    print
    print(Fore.GREEN + "  {0:>2}   {1:<15}{2:^15}".format('ID', 'Hostname', 'Host'))
    count = 1
    for hostname, host in user_info.items():
        if count % 2 == 0:
            print(Fore.GREEN + "  {0:>2}   {1:<15}{2:<20}".format(count, hostname, host))
        else:
            print(Fore.MAGENTA + "  {0:>2}   {1:<15}{2:<20}".format(count, hostname, host))
        count += 1
    print


def single_color_print():
    init(autoreset=True)
    print(Fore.RED + "{0:^60}".format("Command Line SSH Quick Link to Server"))
    print
    print(Fore.GREEN + "  {0:>2}   {1:<15}{2:^15}".format('ID', 'Hostname', 'Host'))
    count = 1
    for hostname, host in user_info.items():
        print(Fore.GREEN + "  {0:>2}   {1:<15}{2:<20}".format(count, hostname, host))
        count += 1
    print


if __name__ == "__main__":
    gather_ssh_info()
    colorful_print()
    #single_color_print()()
