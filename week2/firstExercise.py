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

 

#I nedenstående main sætning kan du køre en funktion der kører alle funktioner
#parser.add_argument("--arg", help="")*/

if __name__ == '__main__':
    printFile(sys.argv[1])
    #writeToFile(sys.argv[1], sys.argv[2])
    #writeManyToFile(sys.argv[1])
    #listFile(sys.argv[1])

