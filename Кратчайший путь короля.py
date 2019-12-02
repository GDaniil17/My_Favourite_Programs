d = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}
ne = {"a":"b", "b":"c", "c":"d", "d":"e", "e":"f", "f":"g", "g":"h"}
pr = {"h":"g", "g":"f", "f":"e", "e":"d", "d":"c", "c":"b", "b":"a"}
s = list(input())
st = list(input())
num1 = int(s[1])
num2 = int(st[1])
print(max(abs(d[s[0]]-d[st[0]]),abs(num1-num2)))

while True:
    if s[0] < st[0]:
        if num1 < num2:
            print("RU")
            num1 += 1
            s[0] = ne[s[0]]
        elif num1 > num2:
            print("RD")
            num1 -= 1
            s[0] = ne[s[0]]
        else:
            print("R")
            s[0] = ne[s[0]]
    elif s[0] >  st[0]:
        if num1 < num2:
            print("LU")
            num1 += 1
            s[0] = pr[s[0]]
        elif num1 > num2:
            print("LD")
            num1 -= 1
            s[0] = pr[s[0]]
        else:
            print("L")
            s[0] = pr[s[0]]
    else:
        if num1 < num2:
            print("U")
            num1 += 1
        elif num1 > num2:
            print("D")
            num1 -= 1
        else:
            break
