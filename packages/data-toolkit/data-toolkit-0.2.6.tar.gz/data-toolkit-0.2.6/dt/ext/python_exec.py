import pandas as pd 
import swifter # ==0.289
import os, sys, io
import subprocess as sp

def execute(command: str):
    all_files = os.listdir('.')

    proc = sp.check_output('find $PWD/* -type f', shell=True) # , capture_output=True, shell=True)
    df = pd.DataFrame(str(proc).split('\\n') )

    import ipdb; ipdb.set_trace()
    print(df)