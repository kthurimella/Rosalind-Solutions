import sys


def main():
    
    f = open(sys.argv[1], 'r')

    integers = f.readline()
    integers = integers.split()

    a = int(integers[0])
    b = int(integers[1])

    difference = b - a
    itrdiff = 0

    if b % 2 == 0 and a % 2 == 0:
        itrdiff = difference/2
        newsum = a + 1
        totalsum = newsum
        for i in xrange(itrdiff - 1):
            newsum += 2
            totalsum = totalsum + newsum

            

    elif a % 2 == 0 and b % 2 != 0:
        itrdiff = difference/2
        newsum = a + 1
        totalsum = a + 1
        for i in xrange(itrdiff):
            newsum += 2
            totalsum = totalsum + newsum


    else:
        itrdiff = difference/2
        newsum = a
        totalsum = a
        for i in xrange(itrdiff):
            newsum += 2
            totalsum = totalsum + newsum


    print totalsum



if __name__ == "__main__":
    main()
