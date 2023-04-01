import pandas as pd

df = pd.read_csv('data.csv')
with open('body.txt', 'r') as file:
    # Read the contents of the file into a string variable
    body = file.read()


# print(df)
# print("+++++++++++++++++++++++")
# print(len(df.index))
# print("+++++++++++++++++++++++")
# print(df["company_name"][0])

# LocalBody = body.split(" ")
# localstring = ""
# print("================")


def punctsreplace(bodyArr, arr, it, i):
    flag = 0
    puncts = [".", ",", "/", "-", ":", ";", "?", "!", ""]

    for j in puncts:
        for k in arr:
            # print(bodyArr[i] + " and " + k+j)
            if (bodyArr[i] == k+j):
                # print(str(df[k][it]) + "yoyo\n")
                # print("here")
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
            print("do sth i guess")
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


# cols = ["company_name", "company_mail", "contact_name", "contact_number"]

# print(replaceWords(body, cols, 0))


# for i in range(len(LocalBody)):
#     if("\n" in LocalBody[i]):
#         newlinesep = LocalBody[i].split("\n")
#         for j in range(len(newlinesep)):
#             if(newlinesep[j] == "company_name"):
#                 newlinesep[j] = df["company_name"][0]
#                 print("what")
#             if(newlinesep[j] == "company_name,"):
#                 newlinesep[j] = df["company_name"][0]+","
#                 print("what")
#             if(newlinesep[j] == "company_name."):
#                 newlinesep[j] = df["company_name"][0] + "."
#                 print("what")
#         concatlinesep = ""
#         for k in newlinesep:
#             concatlinesep += k
#             concatlinesep += "\n"
#         concatlinesep = concatlinesep[:-1]
#         LocalBody[i] = concatlinesep

# for i in LocalBody:
#     localstring += i
#     localstring += " "
# print(localstring)
