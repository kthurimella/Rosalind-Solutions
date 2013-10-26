import sys

def main():
    
    f = open(sys.argv[1], 'r')

    number_of_lines = 0

    for x in f:
        number_of_lines += 1

    f.close()

    y = open(sys.argv[1], 'r')
    
    lines = y.readlines()
    lines = map(lambda s: s.strip(), lines)

    for i in range(1, number_of_lines, 2):
        print lines[i]



if __name__ == "__main__":
    main()
