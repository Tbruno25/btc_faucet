# btc_faucet

A minimal gui implementation of a [bitcoin faucet](https://en.wikipedia.org/wiki/Bitcoin_faucet) that is capable of running on a Raspberry Pi Zero W (rpi).

## Motivation
There are plenty of digital faucets but a google search at the time resulted in no physical bench top ones -- so I set out to build it. This was strictly a learning exercise and an opportunity to build something. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies on your rpi.

```bash
git clone https://github.com/Tbruno25/btc_faucet
pip install -r Requirements.txt
```
After cloning the repo, create ```config.py``` in the directory and bind var ```private_key``` to the private key of the bitcoin wallet you want to use for dispensing funds.

## Usage

After running ```python faucet.py``` the gui will launch. Tap the screen once to start ```scanner.py```. After scanning your qr wallet address, a small amount of btc will be sent to your address and a qr of the transaction displays on screen.

## Demo
![btc_faucet demo](images/demo.gif)
