# MAC Changer

MAC Changer is a Python script for changing MAC addresses of network interfaces on Unix-like operating systems. It provides a simple command-line interface for modifying MAC addresses manually, generating random MAC addresses, and resetting to the original MAC address.

## Features

- Change the MAC address of a specified network interface.
- Generate and assign a random MAC address to a network interface.
- Reset a network interface to its original MAC address.
- View available network interfaces.

## Prerequisites

- Python 3.x
- Unix-like operating system (Linux, macOS)

## Installation

1. Clone the repository:

sudo https://github.com/arun-the-hacker/mac_changer.git
cd macchanger

## Run the script:

python3 macchanger.py [options]

## Usage

python3 macchanger.py [options]

    -i, --interface: Specify the network interface you want to change the MAC address for.
    -m, --mac: Specify the MAC address to change (manual mode only).
    -R, --random: Automatically assign a random MAC address.
    -r, --reset: Reset to the original MAC address.
    -s, --show: Show available network interfaces and exit.

## Examples

Change the MAC address of a specific interface manually:

python3 macchanger.py -i eth0 -m XX:XX:XX:XX:XX:XX

Generate a random MAC address for a specific interface:

python3 macchanger.py -i eth0 -R

Reset a specific interface to its original MAC address:

python3 macchanger.py -i eth0 -r

Show available network interfaces:

python3 macchanger.py -s

## Contributing

Contributions are welcome! If you have any bug reports, feature requests, or suggestions, please open an issue or submit a pull request.
