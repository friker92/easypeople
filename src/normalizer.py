

class Normalizer:

    def column(self,matrix, i):
        return [row[i] for row in matrix]

    def normalize(self,people):
        headers, humans = people[0], people[1::]
        result = []
        result.append(headers)
        for person in humans:
            curr = []
            for i in range(0, len(person)):
                curr.append(self.normalizeData(headers[i],person[i]))
            result.append(curr)
        
        print headers, humans,result
        return False, result

    def normalizeData(self,name,data):
        print "TO-DO: Normalizer.normalize(name,data)",name,data
        return data+1




    
def main():
    n = Normalizer()
    n.normalize([['a','b','c'],['1','2','3'],['4','5','6']])

if __name__ == '__main__':
    main()
