# Custom-Reconnaissance-Tool
A modular Python-based reconnaissance tool for passive and active information gathering. Performs WHOIS lookup, DNS &amp; subdomain enum, port scanning, banner grabbing, tech detection, and generates detailed reports for red team ops.

##  Features

- WHOIS Lookup
- DNS Enumeration (A, MX, TXT, NS)
- Subdomain Enumeration (via crt.sh, AlienVault OTX, etc.)
- Port Scanning (via socket/Nmap)
- Banner Grabbing
- Technology Detection (via WhatWeb or Wappalyzer)
- Generates `.txt` and `.html` summary reports
- Modular CLI flags for each function
- Logging and Verbosity levels

## Installation

git clone https://github.com/yourusername/recon-tool.git
cd recon-tool
pip install -r requirements.txt

## Usage
python recon_tool.py --domain example.com --whois --dns --subdomains --portscan --banners --techdetect --verbose

## Flag	Description
--domain	Target domain (required)
--whois	Perform WHOIS lookup
--dns	DNS record enumeration
--subdomains	Subdomain enumeration via APIs
--portscan	Scan ports (default top 1000)
--banners	Grab banners from open ports
--techdetect	Detect technologies used
--report	Generate .txt or .html report
--verbose	Enable detailed logs
