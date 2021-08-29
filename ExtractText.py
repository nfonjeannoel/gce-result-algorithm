import pyautogui as pt
from time import sleep
import pyperclip
import random

# pagezoom = 54
lines = []
prevLine = ""

x_col1 = 540
x_col2 = 750
y_colxy = 150

# page_number = 0

skips = 95

centers = []
centerId = -1
paperCounter = 0
isNewCenter = True
counter = 0
sameLine = 0
oldLine = ""


def changePageNumber(page_number):
    # x = 565
    # y = 100
    # global page_number
    # page_number += 1
    pt.moveTo(x_col1 + 25, y_colxy - 50)
    pt.leftClick()
    pt.typewrite(str(page_number), interval=.00001)
    pt.moveRel(-50, 0)
    pt.click()


def goToFirstColumn():
    pt.moveTo(x_col1, y_colxy)
    for i in range(skips):
        pt.tripleClick()
        smallWait()
        getLineText()
        moveDown()


def getLineText():
    thisLine = copy_clipboard()
    # global prevLine
    # prevLine = thisLine
    addToList(thisLine)
    # print(line)


def moveDown():
    pt.moveRel(0, 6.9, 0.0001)


def smallWait():
    sleep(0.0001)


def addToList(thisLine):
    global prevLine
    if prevLine == thisLine:
        # print("duplicate")
        None
    else:
        # print("not equal")
        lines.append(thisLine)
        prevLine = thisLine


def goToSecondColumn():
    pt.moveTo(x_col2, y_colxy)
    for i in range(skips):
        pt.tripleClick()
        smallWait()
        getLineText()
        moveDown()


def copy_clipboard():
    pt.hotkey('ctrl', 'c')
    sleep(.001)  # ctrl-c is usually very fast but your program may execute faster
    return pyperclip.paste()


def getResults():
    sleep(3)
    print("start")
    for i in range(2):
        changePageNumber(i + 1)
        goToFirstColumn()
        goToSecondColumn()
    with open("result.txt", "w") as f:
        for line in lines:
            f.write(line)
    f.close()
    print("done")

    # with open("result.txt", "r") as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         print(line)

def checkIfCenterNumber(line):
    global centerId
    global centers
    # global counter
    splitedLines = line.split()
    if "Centre" in splitedLines or "No:" in splitedLines:
        centerId += 1
        # global counter
        # counter -= counter
        # print("center is there")
        # it is a new center
        # print(line)
        # centers.append([line])
        if [line] not in centers:
            global counter
            counter = 0
            centers.append([line])
            with open(f"myfile{centerId}.txt", "w") as f:
                f.write(line)
            f.close()
            # print("new centre")
            # print(f"counter is {counter}")
        # centerId = 0

        return True
        # print(splitedLines)
        # print(centers)
        # print(centers[centerId])
    return False


def checkIfCenterDetails(line):
    global centers
    global centerId
    global paperCounter
    splitedLines = line.split()
    if "Regist:" in splitedLines or "Subjects:" in splitedLines:
        if line not in centers[centerId]:
            centers[centerId].append(line)
        # centerId += 1
        # print("regist in ")
        return True
        # print(centers[centerId])
        # print("printed")
        # print(centers[centerId].append(line))
    return False


def addStudentsNamesAndGrades(line):
    global centerId, centers, counter, sameLine


    # student = line
    # studentNum = line.split()[0]
    # number = student[1:len(studentNum) - 1]
    # try:
    #     if type(int(number)) == int:
    #         centers[centerId].append(line)
    #         counter += 1
    #
    #
    # except ValueError as e:
    #     pass


        #handle the case where the numbering at the begining is not there.
        # add the corresponding number


        # sameLine += 1
        # # print("use value of counter")
        # if sameLine < 3:
        #     centers[centerId].append(line)
        #     counter += 1
        # else:
        #     sameLine = 0
        #     centers[centerId][len(centers[centerId]) - 1] += (str(studentNum)+ " " + line)
        #     print(f"adding {str(studentNum)} to {line} at ")

    # print()
    # DONT DELETE
    # centers[centerId].append(line)


def checkIfUselessLine(line):
    splitedLine = line.split()
    if "Successful" in splitedLine or "Candidates" in splitedLine:
        return True
    return False


def reformatResults():
    with open("result.txt", "r") as f:
        results = f.readlines()
    f.close()
    for line in results:
        if checkIfCenterNumber(line):
            continue
        elif checkIfCenterDetails(line):
            continue
        elif checkIfUselessLine(line):
            continue
        else:
            addStudentsNamesAndGrades(line)

    # print(results)


if __name__ == '__main__':
    # getResults()
    reformatResults()
    print(centers)
    # for i in centers:
    #     for j in i:
    #         print(j)
