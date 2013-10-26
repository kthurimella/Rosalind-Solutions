import sys

def main():
    f = open(sys.argv[1], 'r')

    dimensions = []

    string = str(f.readline())

    dimensions = f.readline()
    dlist = dimensions.split()

    dlist = map(int, dlist)

    a = dlist[0]
    b = dlist[1]
    c = dlist[2]
    d = dlist[3]

    print string[a:b+1] + " " + string[c:d+1]


if __name__ == "__main__":
    main()
