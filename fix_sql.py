# pg2mysql SQL Fixer
# (c)2015 Rob "N3X15" Nelson <nexisentertainment@gmail.com>
#
# Available under the MIT Open-Source License
#

import os
import sys
import re

REG_FUCKED_TYPE = re.compile('` `([a-z]+)`')
REG_FUCKED_CONSTRAINT = re.compile(r'ADD CONSTRAINT "([a-z_]+)" PRIMARY KEY \("([a-z_]+)"\)')

def fixFile(infn, outfn):
    with open(outfn, 'w') as outf:
        with open(infn, 'r') as inf:
            prefixedWith = []
            for line in inf:
                line = REG_FUCKED_TYPE.sub(r'` \1', line)
                line = REG_FUCKED_CONSTRAINT.sub(r'ADD CONSTRAINT `\1` PRIMARY KEY (`\2`)', line)
                lines = line.strip()
                if lines.startswith('DROP TABLE IF EXISTS'):
                    prefixedWith.append('DROP TABLE IF EXISTS')
                    if lines.startswith('CREATE TABLE'):
                        if 'DROP TABLE IF EXISTS' not in prefixedWith:
                            tablename = lines.split(' ')[2].strip('`')
                            outf.write('DROP TABLE IF EXISTS `{0}`;\n'.format(tablename))
                            print(" + DROP TABLE IF EXISTS")
                            prefixedWith = []
                            outf.write(line.rstrip() + '\n')
                            print('Wrote {0}.'.format(outfn))

if __name__ == '__main__':
    fixFile(sys.argv[1], sys.argv[2])
