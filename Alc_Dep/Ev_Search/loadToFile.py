# -*- coding: utf-8 -*-

import os, argparse


def load_valid(file):
    
    thresh = .5
    
    above_thresh_lines = []
    
    with open(file, 'r') as f:
        lines = f.readlines()
        
        for line in lines:
            l = line.split(' ')
            if len(l) > 1 and l[0] != 'None':
                
                try:
                    if float(l[0]) > thresh:
                        above_thresh_lines.append(line)
                        
                except:
                    pass
                
    return above_thresh_lines
    

parser = argparse.ArgumentParser(description='Give load/save commands')

parser.add_argument('key', type=str, help='File name')
parser.add_argument('seperate', type=int, help='If 1, lr sep, else together')
args = parser.parse_args()

files = os.listdir()
files = [ file for file in files if '.o' in file and args.key in file ]

valid = []
for file in files:
    valid += load_valid(file)
    
    os.remove(file)

if args.seperate == 0:
    to_open = 'ALL'    
elif args.seperate == 1:
    to_open = 'LR_SEPERATE'
elif args.seperate == 2:
    to_open = 'LR_BOTH'
else:
    to_open = 'GARBAGE'

print('Sending to ', to_open, ' with key = ', args.key)

with open(to_open, 'a') as f:
    for line in valid:
        f.write(line)
    

