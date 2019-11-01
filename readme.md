# VCF to Abook

A python script for converting .vcf contact files into abook files to be used in the addressbook program for Mutt/Neomutt

**Note:** This project is in the Alpha stage and currently has limited capabilities.

## Requirements
* Python 3.6+

## Instructions

1. Clone or download this repository.
2. Copy your vcf file into the same directory as vcftoabook.py. **Make sure to rename it as contacs.vcf**.
3. Run `python vcftoabook.py`. If all goes well you should now have an addressbook file saved in the same directory as vcftoabook.py and your contacts.vcf

## TODO
- [ ] - Refactor into a proper command line application
- [ ] - Test with multiple vcf versions.
- [ ] - Build deployment packages for the AUR & Pip
