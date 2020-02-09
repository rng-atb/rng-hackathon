import argparse
import random

def generate_data(num_accounts, labels, num_lines, output=None):
    print("""
    num accounts: {0}
    labels:       {1}
    num_lines:    {2}
    """.format(num_accounts, labels, num_lines))

    labels = labels.split(",")
    data = []
    for a in range(num_accounts):
        for l in range(num_lines):
            r = random.randint(0, len(labels)-1)
            v = random.randint(1, 99)
            entry = "Account{0},{1},{2}".format(a, labels[r], v)
            data.append(entry)
    if output is not None:
        with open(output, 'w') as myfile:
            for line in data:
                myfile.write(line+'\n')
    else:
        for line in data:
            print(line)
    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process args to generate d3 open banking data')
    parser.add_argument('--num_accounts', '-a', type=int,
                        help='number of accounts to generate data for')
    parser.add_argument('--labels', '-l',
                        help='comma separate list of labels')
    parser.add_argument('--num_lines', '-c', type=int,
                        help='average number of lines connecting accounts to labels') 
    parser.add_argument('--outputfile', '-o',
                        help='output file to write to ')                 

    args = parser.parse_args()
    generate_data(args.num_accounts, args.labels, args.num_lines, args.outputfile)