# btc_faucet

A minimal gui implementation of a [bitcoin faucet](https://en.wikipedia.org/wiki/Bitcoin_faucet) that is capable of running on a Raspberry Pi Zero W (rpi).

## Motivation
There are plenty of digital faucets but a google search at the time resulted in no physical bench top ones -- so I set out to create it. This was strictly a learning exercise and an opportunity to build something. 

## Parts
[Raspberry Pi Zero W](https://www.adafruit.com/product/3400?gclid=EAIaIQobChMIkva4iaj65wIVlqDsCh1gcQmpEAQYASABEgIhF_D_BwE)  
[2.8" Touch LCD](https://www.amazon.com/dp/B073R7BH1B/)  
[Pi Cam](https://www.amazon.com/gp/product/B07KF7GWJL/)

[3D Printer .STL](https://grabcad.com/library/btc_faucet-stand-1)

![demo](https://i.imgur.com/F4GiTqE.png) ![demo](https://i.imgur.com/MlPp27X.png) ![demo](https://i.imgur.com/X7VCAjG.png)

## Installation
```bash
git clone https://github.com/Tbruno25/btc_faucet
```
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies on your rpi.
```bash
pip install -r Requirements.txt
```
After cloning the repo, create ```config.py``` in the directory and bind var ```private_key``` to the private key of the bitcoin wallet you want to use for dispensing funds.

## Usage

After running ```python faucet.py``` the gui will launch. Tap the screen once to start ```scanner.py```. After scanning your wallets qr code, a small amount of btc will be sent to the address and a qr link to the transaction displays on screen.

## Demo
![btc_faucet demo](images/demo.gif)
