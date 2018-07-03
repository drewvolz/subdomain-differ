# subdomain-differ

This script is a dumbed-down wrapper around the [CTFR](https://github.com/UnaPibaGeek/ctfr) project created by Sheila A. Berta. It checks for subdomains of a domain, stores them in a text file per domain, and diffs the output in the CLI. This wrapper handles the "diffing-the-changes" and the "writing-to-a-file" logic.

## Original CTFR intro

> Do you miss AXFR technique? This tool allows to get the subdomains from a HTTP**S** website in a few seconds. How it works? CTFR does not use neither dictionary attack nor brute-force, it just abuses of Certificate Transparency logs. For more information about CT logs, check www.certificate-transparency.org and [crt.sh](https://crt.sh/).

## Prerequisites

Make sure you have installed the following tools:

```
Python 3.0 or later.
pip3 (sudo apt-get install python3-pip).
```

## Installing

```bash
$ git clone https://github.com/drewvolz/subdomain-differ.git
$ cd subdomain-differ
$ pip3 install -r requirements.txt
```

## Running

```bash
$ python3 subdomain-differ.py wikipedia.org
```
