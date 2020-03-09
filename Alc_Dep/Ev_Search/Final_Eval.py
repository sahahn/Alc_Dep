# -*- coding: utf-8 -*-

import os
from Ev_Search.Check_Viable import check_pop

thresh = .75

def change_temp_script(keys):

    with open('final_run.script', 'r') as f:
        lines = f.readlines()

    for i in range(len(lines)):
        if 'REPLACE' in lines[i]:
            lines[i] = 'python Single_Evaluate.py --keys '
            
            for key in keys:
                lines[i] += str(key) + ' '

    with open('temp2.script', 'w') as f:
        for line in lines:
            f.write(line)
            
def run_job():
    os.system('qsub temp2.script')            

dr = 'Ev_Search/'
files = os.listdir(dr)

valid = [file for file in files if '.pkl' in file]
viable_keys = []

for pop in valid:
    viable_keys += check_pop(dr + pop, thresh)

print(len(viable_keys))
    
#for key_set in viable_keys:
    #change_temp_script(key_set)
    #run_job()
