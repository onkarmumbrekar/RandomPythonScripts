string = input()
ln = len(string)
substring_count = int(ln*(ln+1)/2)
kevin = 0
for i in range(ln):
    if string[i] in "AEIOU":
        kevin += (ln-i)
stuart = substring_count-kevin
if stuart > kevin:
    print("Stuart", stuart)
elif kevin > stuart:
    print("Kevin", kevin)
else:
    print("Draw")