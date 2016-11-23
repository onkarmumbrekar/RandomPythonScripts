a,b,c,d,e = input().strip().split(' ')
numbers = [int(a),int(b),int(c),int(d),int(e)]
numbers = sorted(numbers)
minimum=0
maximum=0
for i in range(5):
    if i != 4:
        minimum = minimum + int(numbers[i])
    if i !=0 :
        maximum = maximum + int(numbers[i])
print(minimum , maximum)