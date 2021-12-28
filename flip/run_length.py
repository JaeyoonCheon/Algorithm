def run_length_encoding(seq):
    start = count = 1
    data = seq[0]
    output = ""

    for i in range(1, len(seq)):
        if seq[i] != seq[i-1] or i == len(seq)-1:
            output = output + str(count) + seq[start]
            count = 1
            start = i
        else:
            count = count + 1

    return output

def run_length_decoding(seq):
    output = ""

    if seq != None:
        for i in range(0, len(seq), 2):
            count = seq[i]
            data = seq[i+1]
            output = output + data * int(count)

    return output

inputStr = input("input string : ")

flag = ""

for i in inputStr:
    if i.isalpha():
        continue
    else:
        flag = "compressed"

if flag == "compressed":
    print("decoding!")
    print(run_length_decoding(inputStr))
else:
    print("encoding!")
    print(run_length_encoding(inputStr))