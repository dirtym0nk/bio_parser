read = open('bioinf.txt', 'r')
num = ""
for line in read:
    if line == "1)":
        num = "1)"
    elif line == "2)":
        num = "2)"
    elif line == "3)":
        num = "3)"
    elif line == "4)":
        num = "4)"
    elif line == "5)":
        num = "5)"
    elif line == "6)":
        num = "6)"
    if line.strip() != '' and line.strip() not in ["1)", "2)", "3)", "4)", "5)", "6)"]:
        print(num + line)

