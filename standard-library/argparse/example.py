import argparse


parser = argparse.ArgumentParser(description='Example')

parser.add_argument(
    '-i',
    action='store', 
    dest='input',
    help='Input file'
)

args = parser.parse_args()
print args.input
print args
