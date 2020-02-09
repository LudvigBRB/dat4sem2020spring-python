import sys
import csv
import getopt

#1
#A.
def printFile(file):
    with open(file) as fObj:
        reader = csv.reader(fObj)

        for row in reader:
            print(str(row))

#B.
def writeToFile(file, list):
    with open(file, 'a') as fObj:
        for element in list:
            fObj.write(str(element))
        print(fObj)

#B. a.
def writeManyToFile(file, *strings):
    with open(file, 'a') as fObj:
        for string in strings:
            fObj.write(string)
        print(fObj)

#C.
def listFile(file):
    with open(file) as fObj:
        reader = csv.reader(fObj)
        return [row for row in reader]

#2.
def doFile(arguments):
    try:
        opts, args = getopt.getopt(arguments, "f", ["file"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    for options, file in opts:
        print(option)
        with open(file) as fObj:
            if option in ("-f", "--file"):
                with open(file) as fObj:
                    for element in list:
                        fObj.write(str(element))
            else:            
                reader = csv.reader(fObj)
                for row in reader:
                    print(str(row))


if __name__ == '__main__':
    #printFile(sys.argv[1])
    #writeToFile(sys.argv[1], sys.argv[2])
    #writeManyToFile(sys.argv[1])
    #listFile(sys.argv[1])