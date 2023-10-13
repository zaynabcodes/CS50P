#argparse is a library that handles the parsing of the command line arguments

import argparse


parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n",default=1,  help="Number of times to meow", type=int)
args = parser.parse_args() #has all the commandline arguments stored in there

for _ in range(args.n):
    print("meow")