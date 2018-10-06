class Box:
 
    def add(self, *items):
        raise NotImplementedError()
        
    def empty(self):
        raise NotImplementedError()
        
    def count(self):
        raise NotImplementedError()

class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value 
        
    def setName(self, name):
        self.name = name
        
    def getName(self):
        return self.name

    def setValue(self, value):
        self.value = value
        
    def getValue(self):
        return self.value
    
class ListBox(Box):
    def __init__(self):
        self.list = []
    
    def __getitem__(self,index):
        return self.list[index]
    '''
    def returnItem(self, index):
        return self.list[index]
    '''    
    def add(self, items):
        #self.list.append(item)
        for item in items:
            self.list.append(item)
        
    def empty(self):
        listTmp = self.list
        '''
        for elem in self.list:
            listTmp.append(elem)
        '''
        self.list = []
        return listTmp
        
    def count(self):
        return len(self.list)
        
class DictBox(Box):
    def __init__(self):
        self.list = {}
        
    def add(self, items):
        for item in items:
            self.list.update({str(item):item})
        
    def empty(self):    #returns a list
        listTmp = self.list.values()
        #self.list.clear()     # modifies the pointer and listTmp   
        self.list = {}
        return listTmp
        
    def count(self):
        return len(self.list)
        
    def __getitem__(self, key):
        return self.list[key]
        
        
def repackBoxes(boxes):
    allItems = []    
    
    for i in range(len(boxes)):                        
        boxContent = boxes[i].empty()        
        allItems.extend(boxContent)     #copies each element
    
    nrItems = int(len(allItems)/len(boxes))
    print("\n", nrItems, allItems[0])
    
    prevIndex = 0
    for b in boxes:
        finalIndex = nrItems+prevIndex
        
        if len(allItems)-finalIndex <2:
            finalIndex = finalIndex + (len(allItems)-finalIndex)
        
        b.add(allItems[prevIndex:finalIndex])
        prevIndex += nrItems
    
    for b in boxes:
        print(b.count())
        
        
    
    
    
        
##########################
        
listBox = ListBox()
listBox9 = ListBox()
dictBox = DictBox()

# 1. fill the three lists
items = []
for i in range(20):
    items.append(Item(str(i), i))
listBox.add(items)

items = []
for i in range(9):
    #listBox9.add(Item(str(21+i), 21+i))
    items.append(Item(str(21+i), 21+i))
listBox9.add(items)

items = []
for i in range(5):
    items.append(Item(str(30+i), 30+i))
dictBox.add(items)
    
# 2. check that all are filled    
print(listBox.count())
print(listBox9.count())
print(dictBox.count())

# 3. show Items in ListBox
for i in range(listBox.count()):
    print(listBox[i].getName())

print("\n")

# 4. show Items in DictBox
'''
dictBoxList = dictBox.empty()
print(len(dictBoxList))
for item in dictBoxList:
    print(item.getName())
'''
'''
for k,v in dictBoxList.items():
    print(type(k))
    print(type(v))
    print(v.getName(), v.getValue())
'''
# 5. try repackBoxes method
boxes = [listBox, listBox9, dictBox]
repackBoxes(boxes)
        
        