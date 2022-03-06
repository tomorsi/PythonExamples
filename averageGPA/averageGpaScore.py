
# Total number of grades
NUM_OF_GRADES = 5
debug_tabs = 0;


def getScore():
    global debug_tabs
    print(debug_tabs*'\t', "entered: ", getScore.__name__, sep=" ")
    print(debug_tabs*'\t', "exited: ", getScore.__name__, sep=" ")

def getGPAPoint():
    global debug_tabs
    print(debug_tabs*'\t',"entered: ", getGPAPoint.__name__, sep=" ")
    print(debug_tabs*'\t',"exited: ", getGPAPoint.__name__, sep=" ")

def averageGPA():
    global debug_tabs
    print(debug_tabs*'\t',"entered: ", averageGPA.__name__)
    debug_tabs = debug_tabs + 1
    for grade in range(NUM_OF_GRADES):
        getScore()
        getGPAPoint()

    debug_tabs = debug_tabs - 1
    print(debug_tabs*'\t',"exited: ", averageGPA.__name__)

def main():
    global debug_tabs
    print(debug_tabs*'\t',"entered: ", main.__name__)
    debug_tabs = debug_tabs + 1
    averageGPA();
    debug_tabs = debug_tabs - 1
    print(debug_tabs*'\t',"exited: ", main.__name__)
    
if __name__ == "__main__":
    main()


    
