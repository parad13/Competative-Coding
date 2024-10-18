value1 = "".join(input().rstrip().split('\r'))
value2 = "".join(input().rstrip().split('\r'))
value3 = "".join(input().rstrip().split('\r'))
value4 = "".join(input().rstrip().split('\r'))

strings = [value1, value2, value3, value4]
outputs = []

def operation(strings):
    for string in strings:
        stringSplit = string.split(";")
        if stringSplit[0] == "S":
            if stringSplit[1] == "M":
                outputs.append(camel_case_to_words(stringSplit[2].strip("()")))
            elif stringSplit[1] == "C":
                outputs.append(camel_case_to_words(stringSplit[2]))
            else:
                outputs.append(camel_case_to_words(stringSplit[2]))
        elif stringSplit[0] == "C":
            string_combine = list_to_camel_case_words((stringSplit[2].split(" ")))
            if stringSplit[1] == "M":
                outputs.append(string_combine + "()")
            elif stringSplit[1] == "C":
                outputs.append(string_combine[0].upper() + string_combine[1:])
            else:
                outputs.append(string_combine)
            
    return outputs

def camel_case_to_words(text):
    result = text[0].lower()
    for char in text[1:]:
        if char.isupper():
            result += ' ' + char.lower()
        else:
            result += char
    return result

def list_to_camel_case_words(listw: list):
    output = listw[0]
    for i in range(1, len(listw)):
        val = listw[i]
        output += val[0].upper() + val[1:]

    return output
    
for output in operation(strings):
    print(output)

