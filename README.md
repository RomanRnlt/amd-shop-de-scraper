# amd-shop-de-scraper

## Description:
Scraper that scraps the digitalriver (AMD-Shop partner) website and watches for error code CAT15 (GPU not available) and CAT16 (gpu available).
Every Thursday ~ 5 - 8 pm (german time ca. 17:00 - 20:00 Uhr) AMD sells on their webshop (https://www.amd.com/de/direct-buy/de) less than 400 GPUs.

This scraper will check if the diffrent GPUs (RX6900XT, RX6800XT_Midnight_Black, RX6800XT, RX6800, RX6700XT) are available and opens a new Chrome tab with the specific GPUs which is available.

## How to use:
1. Start script (MAC: $ python3 amdshop.py) every thursday at ~ 4:30 pm (ca. 16:30 Uhr)
2. Wait until chrome tab with specific GPU opens
3. Having fun while buying your dream GPU

**To stop script, just go to your IDE/terminal/cmd (where you start the script) and hit *ctrl + c*.**

## Installation
1. Just clone project to your IDE or download ZIP file
2. Open script in your IDE or goto "How to use:"

**Mac is the standard.
For Windows use comment line 32 in.
For Linux use comment line 35 in. (in *amdshop.py*)**
