
from Node import Node
from LinkList import LinkList

data = ["horse","chicken","rat","mouse",
        "cow","dog","cat"]

def main():
    print "main"
    linkList = LinkList()

    for item in data:
        linkList.addData(item)

    print "\n\ndisplay list as inserted"      
    linkList.dump()    

    print "\n\ndispaly list reversed"
    linkList.reverse()
    linkList.dump()


if __name__=='__main__':
    main()
