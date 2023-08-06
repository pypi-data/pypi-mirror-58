#!/bin/python
from Tree import Tree
from random import randrange
import random
import string
import time
from progress.bar import ShadyBar

class bytestock:
    def __init__(self):
        self.tree = Tree()
        self.dataSet1 = []
        self.dataSet2 = []
        self.data = []
        self.findData = None
        self.letters = 'al34nMT0V&#@fr'
        self.dataset1Size = 1000000
        self.searchKeySize = 10
        
    def insert(self, str, ):
        return tree.insert(str)
                
    def findBulk(self, self.dataSet2=dataSet2):
        for data in dataSet2:
            findData = tree.find(data)
            if findData is not False:
                return findData
                
    def find(self, self.data=data):
        findData = tree.find(data)
        if findData is not False:
            return findData
                
    ##Genarate random Strings
    def randString(self, letters=self.letters):
        return ''.join((random.choice(letters) for i in range(randrange(10))))


    ##Genarate random dataset 
    def datagen(self,dataset1Size=self.dataset1Size, letters=self.letters):
        with ShadyBar('Genarating dataset of ' + dataset1Size + ' using ' + letters + ' ...', max=100) as bar:
            for counter1 in range(0,dataset1Size):
                randomstring = randString(letters)
                dataSet1.append(randomstring)
                tree.insert(randomstring)
                if counter1/dataset1Size*100 in range(0,100) :
                    bar.next()
        return dataSet1

    def keygen(self, searchKeySize=self.searchKeySize, letters=self.letters):
        ##Genarate random search keys
        with ShadyBar('Genarating random ' + searchKeySize + ' search keys using ' + letters + ' ...', max=100) as bar:
            for counter2 in range(0,searchKeySize):
                dataSet2.append(randString(letters))
                if counter2/searchKeySize*100 in range(0,100) :
                    bar.next()
        return dataSet2
            
    def demo(self, letters=self.letters, dataset1Size=self.dataset1Size, searchKeySize=self.searchKeySize):
        datagen(dataset1Size, letters)
        keygen(searchKeySize, letters)
        self.letters = letters
        self.dataset1Size = dataset1Size
        self.searchKeySize = searchKeySize
        print('\nDataset includes ',len(dataSet1),' data')
        print(len(dataSet2),' search keys')
        print('======================================================================')

        ##Search option 1
        start1 = time.time()
        for data in dataSet2:
            print('Find ',data,' \t:',tree.find(data))
        end1 = time.time()
        print('=============ByteStock Execution time : %s seconds ===================\n' %round(end1-start1,2))

        ##search option 2
        start2 = time.time()
        for searchIndex in dataSet2:
            for index in dataSet1:
                if index == searchIndex:
                    print('Find ',searchIndex,' \t: True')
                    break
                index = None
            print('Find ',searchIndex,' \t: False')
        searchIndex = None

        end2 = time.time()
        print('======== Traditional Approach Execution time : %s seconds ========' %round(end2-start2,2))
        print('==================================================================\n')
        print('ByteStock Execution efficiency %s/100' %round(((end2-start2)-(end1-start1)/(end2-start2))*100,2))



