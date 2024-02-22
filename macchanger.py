#!/usr/bin/env python3

import subprocess
import os
from argparse import ArgumentParser


def change_mac(interface, new_mac):
    """Change the MAC address of the specified interface"""
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])


def random_mac(interface):
    """Generate and assign a random MAC address to the specified interface"""
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "macchanger", "-r", interface])
    subprocess.call(["sudo", "ifconfig", interface, "up"])


def reset_mac(interface):
    """Reset the MAC address of the specified interface to its original MAC"""
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "macchanger", "-p", interface])
    subprocess.call(["sudo", "ifconfig", interface, "up"])


def show_interfaces():
    """Show available network interfaces"""
    print("[:Available Interfaces:]")
    os.system("sudo netstat -i | awk '{print $1}'")


def main():
    parser = ArgumentParser(description="macchanger [Option]", usage="%(prog)s [options]")
    parser.add_argument('-i', '--interface', metavar='', type=str, help="Interface you want to change MAC")
    parser.add_argument('-m', '--mac', metavar='', type=str, help="MAC Address to change [Manual Mode only]")
    parser.add_argument('-s', '--show', help="Show available interfaces and exit", action="store_true")
    parser.add_argument('-R', '--random', help="Automatically assign a random MAC", action="store_true")
    parser.add_argument('-r', '--reset', help="Reset to original MAC", action="store_true")

    args = parser.parse_args()

    if args.show:
        show_interfaces()
    elif args.interface:
        if args.mac:
            change_mac(args.interface, args.mac)
        elif args.random:
            random_mac(args.interface)
        elif args.reset:
            reset_mac(args.interface)
        else:
            parser.print_help()
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
