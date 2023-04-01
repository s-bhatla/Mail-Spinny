import pandas as pd

df = pd.read_csv('data.csv')
with open('body.txt', 'r') as file:
    # Read the contents of the file into a string variable
    body = file.read()

def punctsreplace(bodyArr, arr, it, i):
    flag = 0
    puncts = [".", ",", "/", "-", ":", ";", "?", "!", ""]

    for j in puncts:
        for k in arr:
            if (bodyArr[i] == k+j):
                bodyArr[i] = str(df[k][it])+j
                flag = 1
                break
        if (flag == 1):
            break
    return bodyArr


def replaceWords(body, arr, it):
    LocalBody = body.split(" ")

    for i in range(len(LocalBody)):
        if("\n" in LocalBody[i]):
            newlinesep = LocalBody[i].split("\n")
            for j in range(len(newlinesep)):
                newlinesep = punctsreplace(newlinesep, arr, it, j)
            concatlinesep = ""
            for k in newlinesep:
                concatlinesep += k
                concatlinesep += "\n"
            concatlinesep = concatlinesep[:-1]
            LocalBody[i] = concatlinesep
                
        else:
            LocalBody = punctsreplace(LocalBody, arr, it, i)

    localstring = ""
    for i in LocalBody:
        localstring += i
        localstring += " "
    return localstring
