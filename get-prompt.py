'''
This script generates a random number and pulls a prompt from the 
"list-of-prompts.txt" file.  The top of that file lists the 
website that the prompts were pulled from.

Can be turned into an alias to be run from the terminal
'''

import numpy as np
import pandas as pd

# reading in list of prompts
path = '/home/aibhleog/Documents/scratch-code/phd-writing-prompts/' # change to be your own path
df = pd.read_csv(path+'list-of-prompts.txt',skiprows=4,sep='\n',names=['prompt'])

num = round(np.random.uniform(0,len(df))) # generating random number

print(f'''
---------------
WRITING PROMPT:
---------------
{df.loc[num,"prompt"]}
''')

