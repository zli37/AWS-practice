#!/home/zli/local/anaconda2/bin/python

# This file convert the json file to 
# strict json file
# Reference jmcauley.ucsd.edu/data/amazon/

import json 
import gzip 
def parse(path): 
    g = gzip.open(path, 'r') 
    for i in g: 
        yield json.dumps(eval(i)) 
f = open("output.strict", 'w') 
for i in parse("reviews_Books_5.json.gz"): 
    f.write(i + '\n')
