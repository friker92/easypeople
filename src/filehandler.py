import csv
import sys

class FileHandler:

    def readCSV (self,filename):
        f = open(filename,'rb')
        try:
            reader = csv.reader(f)
            result = list(reader)
            f.close()
            return True, result
        except:
            return False, []

    def writeNormalCSV(self, filename, people):
        f = open(filename,'w');
        print people,filename
        try:
            writer = csv.writer(f)
            for row in people:
                writer.writerow(row)
            writer.close()
            return True
        except:
            return False

#-------------------------------
#      TEST
#-------------------------------
def main() :
    #filename = sys.argv[1];
    filename = "../files/example.csv"
    #outfilename = sys.argv[2];
    outfilename = "../files/outexample.csv"
    handler = FileHandler()
    NoError, InData = handler.readCSV(filename)
    print NoError,InData
    if NoError :
        handler.writeNormalCSV(outfilename,InData)
    else:
        print "Something was wrong!"
    
if __name__ == "__main__":
    main()
