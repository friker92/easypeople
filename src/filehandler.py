import csv
import sys

def multiRow(row):
    return row;

def readCSV (filename):
    f = open(filename,'rb');
    try:
        reader = csv.reader(f);
        f.close();
        return reader;

def writeNormalCSV(filename, people):
    f = open(filename,'w');
    try:
        writer = csv.writer(f)
        for row in people:
            writer.writerow(multiRow(row));
        writer.close();
        return true;
    return false;


def main() :
    #filename = sys.argv[1];
    filename = "../files/example.csv"
    #outfilename = sys.argv[2];
    outfilename = "../files/outexample.csv"
    InData = readCSV(filename)
    writeNormalCSV(outfilename)
    
if __name__ == "__main__":
    main()
