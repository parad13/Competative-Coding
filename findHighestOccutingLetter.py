# In given string find the letter which has highest occurance and print the letter with its no. of occurances

def findHighestOccuringLetter(l:list) -> tuple:
    dic = {}

    for i in l:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    print(dic)
    max1 = 0
    letter = ''
    for k,v in dic.items():
        if v > max1:
            max1 = v
            letter = k
    return letter, max1

if __name__ == "__main__":
    # string = "loremipsum"
    string = input("Enter a string: ").replace(" ", "")
    result = findHighestOccuringLetter(string)
    print(result)