from __future__ import print_function
import sys, re, os.path, pickle, subprocess
from numpy import *
from collections import defaultdict

outfname = "data.pkl"
infnamepattern = "out_.*.txt"

if len(sys.argv) < 2:
    print("Usage: {} DIR".format(sys.argv[0]))
    sys.exit(2)
    
dirname = sys.argv[1]
allfiles = os.listdir(dirname)
fnames = sorted(filter(lambda fname: re.match(infnamepattern, fname), allfiles))

data = defaultdict(list)
for fname in fnames:
    try:
        print("Looking at {}...".format(fname))
        f = open(os.path.join(dirname, fname), "r")

        # Advance to the runs
        line = f.next()
        while not line.startswith("  Running method..."):
            if not line: break
            line = f.next()

        # Read the parameters
        while not line.startswith("    p3m params:"):
            line = f.next()
        line = line.strip()
        print("  ", line)
        thematch = re.match("^p3m params: r_cut=([^,]+),", line)
        r_cut = float(thematch.group(1))
        print("  r_cut =", r_cut)

        while True:
            # Read timings
            while not line.startswith("  P3M TIMINGS:"):
                line = f.next()

            # Now read single timings
            while True:
                line = f.next()
                thematch = re.match("^\s+([^=]+)=(\S+)\s+", line)
                if thematch is None: break
                key, value = thematch.groups()
                value = float(value)
                data[key].append([r_cut, value])
    except StopIteration:
        pass

for key in data.keys():
    data[key] = array(data[key])

outpath = os.path.join(dirname, outfname)
print("Writing data to", outpath, "...")
with open(outpath, 'w') as f:
    pickle.dump(data, f)
print("Finished.")

