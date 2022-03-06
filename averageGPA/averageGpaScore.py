
def main():
    average = averageGPA()

def getScore():
    score = -1
    while score<0 or  score>100 :
        score = float(input("Enter score 1 to 100: "))
        if score < 0 or score > 100:       
    	    print("Invalid entry: Enter score 1 to 100: ", score)
            
    print ("score entered is: " , score)
    return score

def getGPApoint(score):
    print("checking score: ", score)
    if score < 60.0:
        gpaPoint = 0
    elif score >= 60.0 and score <= 69.0:
        gpaPoint = 1.0
    elif score >= 70.0 and score <= 79.0:
        gpaPoint = 2.0
    elif score >= 80.0 and score <= 89.0:
        gpaPoint = 3.0
    else :
        gpaPoint = 4.0
    return gpaPoint
        
def averageGPA():
    totalGPA = 0
    for grade in range(5):
        score = getScore()
        print("score: ", score)
        gpaPoint = getGPApoint(score)
        print("gpa point: ", gpaPoint)
        totalGPA = totalGPA + gpaPoint
        print("total: ", totalGPA)
    average = totalGPA / 5.0
    print("Your average is: ", average)

if __name__ == "__main__":
    main()
