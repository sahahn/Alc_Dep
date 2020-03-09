#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 13:30:35 2019

@author: sage
"""

import os, time, sys
from Ev_Search.Check_Viable import get_best

KEY_NAME = 'key_set'
SCRIPT_TEMPLATE = 'template.script'
KEY_DR = 'Ev_Search'

START_NUM = 1
JOBS = 50

GENERATIONS = 10
PRELOADED = False

CHECK_EVERY = 120
LIMIT = 7200

CHECK_SCORE = False

SCORE_LIMIT = .9
CHECK_SCORE_EVERY = 3600 #Hour

COUNTER = {}
TIMER = {}

def check_directory():
    
    files = os.listdir()

    if 'KILL_TASKS' in files:
        os.remove('KILL_TASKS')
        sys.exit()

    files = [file for file in files if KEY_NAME in file]
    
    valid = [str(i) for i in range(START_NUM, START_NUM+JOBS)]
    valid_files = []
    
    for file in files:
        name = file.split('.')[0].replace(KEY_NAME, '')
        
        if name in valid:
            valid_files.append(file)        

    return valid_files

def change_temp_script(name, load):
    
    with open(SCRIPT_TEMPLATE, 'r') as f:
        lines = f.readlines()
        
    for i in range(len(lines)):
        if 'REPLACE' in lines[i]:
            lines[i] = lines[i].replace('REPLACE', name)
        if 'LOAD' in lines[i]:
            lines[i] = lines[i].replace('LOAD', load)
            
    with open('temp.script', 'w') as f:
        for line in lines:
            f.write(line)
            
def run_job():
    os.system('qsub temp.script')

def init_jobs():
    
    for i in range(START_NUM, START_NUM+JOBS):
        change_temp_script(str(i), '0')
        run_job()
        
        COUNTER[str(i)] = 1
        TIMER[str(i)] = time.time()
        
def check_counter():
    '''Returns true if jobs need to be run more'''
    
    #Check if any jobs are not done
    for i in range(START_NUM, START_NUM+JOBS):
        if COUNTER[str(i)] < GENERATIONS:
            return True
        
    return False

def proc_new_files(files):
    
    for file in files:
        name = file.split('.')[0].replace(KEY_NAME, '')
        
        if COUNTER[name] < GENERATIONS:
            change_temp_script(name, '1')
            run_job()
        
            COUNTER[name] += 1
            TIMER[name] = time.time()
            
            os.remove(file)
        
def save_progress():
    with open('progress', 'w') as f:
        for c in COUNTER:
            f.write(str(c) + ' ' + str(COUNTER[c]) + ' ' + str(TIMER[c]) + '\n')
            
            
def restart_job(name):
    
    #If starting from scratch and counter still == 1
    if PRELOADED == False and COUNTER[name] == 1:
        print('restart job ', name, 'with new')

        change_temp_script(name, '0')
        run_job()
        
        COUNTER[name] = 1
        TIMER[name] = time.time()
    
    #Otherwise, just try again
    else:
        print('restart job w/ load', name)
        change_temp_script(name, '1')
        run_job()
    
        COUNTER[name] += 1
        TIMER[name] = time.time()
            
def check_progress():
    
    current_time = time.time()
    
    for i in range(START_NUM, START_NUM+JOBS):
        i = str(i)
        
        if COUNTER[i] < GENERATIONS:
            print('check progress job ', i, current_time - TIMER[i])
            
            #If job hasnt been updated in enough time, restart it-
            if current_time - TIMER[i] > LIMIT:
                restart_job(i)

def check_score_limit():
    '''Every so often check and see if any of the
       jobs still running are over the limit. If so-
       set them to be stopped.'''

    valid = [file for file in os.listdir(KEY_DR) if '.pkl' in file and KEY_NAME in file]

    for i in range(START_NUM, START_NUM+JOBS):
        i = str(i)

        file_name = KEY_NAME + i + '.pkl'
        if COUNTER[i] < GENERATIONS and file_name in valid:
            
            score = get_best(KEY_DR + file_name)
            
            if score > SCORE_LIMIT:
                COUNTER[i] = GENERATIONS * 5

def check_score_time(last):

    current_time = time.time()

    if (current_time - last) > CHECK_SCORE_EVERY:
                
        check_score_limit()
        return current_time

    return last

if not PRELOADED:
    init_jobs()

#If preloaded-
else:
    for i in range(START_NUM, START_NUM+JOBS):
        
        COUNTER[str(i)] = 0
        TIMER[str(i)] = time.time()

if CHECK_SCORE:
    check_score_limit()
    last = time.time()

save_progress()
  
#MAIN LOOP
while check_counter():
    
    files = check_directory()
    if len(files) > 0:
        
        proc_new_files(files)
        save_progress()

    print('check progress')        
    check_progress()
    
    if CHECK_SCORE:
        last = check_score_time(last)
        
    time.sleep(CHECK_EVERY)
    sys.stdout.flush()        
        
        
    
        
        
        
    

    
    




