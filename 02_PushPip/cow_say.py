import argparse

parser = argparse.ArgumentParser(
    prog = "cow_say",
    description = "draw an animal saying something",
    epilog = "something"
)

parser.add_argument('phrase')
parser.add_argument('-c', '--character')
parser.add_argument('-t', '--text')

args = parser.parse_args()

print(args.phrase, args.character, args.text)