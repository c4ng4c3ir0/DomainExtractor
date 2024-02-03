# Domain Extractor

## Description
The `DomainExtractor.py` script is designed to extract the main domain from a list of subdomains. It handles different scenarios based on the length of the TLDs and the presence of ccTLDs. The script intelligently differentiates between longer TLDs (more than 4 characters) and combinations of TLDs and ccTLDs that total up to 5 characters, applying specific logic to ensure accurate domain extraction.

## Features
- Extracts main domains from a provided list of subdomains.
- Supports special handling for TLDs longer than 4 characters and ccTLD combinations up to 5 characters.
- Reads subdomains from a text file, processing each line as a separate entry.

## Prerequisites
Ensure you have Python installed on your system. This script was developed with Python 3.x in mind.

## Usage
1. Prepare a text file containing your subdomains, one per line. For example, `subdomains.txt`.

2. Run the script from the command line or terminal, passing the path to your subdomains file as an argument:

```bash
python extract_domains_v2.py -file path_to_your_subdomains_file.txt
