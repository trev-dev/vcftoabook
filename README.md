# VCF to addressbook

A python script for converting .vcf contact files into abook files to be used in the addressbook program for Mutt/Neomutt

**Note:** This project is in the Alpha stage. Help with testing on various distros/vcf versions would be appreciated

## Requirements
* Python 3.6+

## Instructions

1. Clone or download this repository.
2. cd into vcftoabook and run vcftoabook -h/--help for instructions

**Optional** You can also symlink vcftoabook into a directory that's included in your $PATH variable to use it system wide.

## Testing
Currently tested with:
* Nextcloud 16.x VCF version 4

## TODO
- [x] Refactor into a proper command line application
- [ ] Test with multiple vcf versions.
- [ ] Build deployment packages for the AUR & Pip

License: [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)
