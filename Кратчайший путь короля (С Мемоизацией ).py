d = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}
ne = {"a":"b", "b":"c", "c":"d", "d":"e", "e":"f", "f":"g", "g":"h"}
pr = {"h":"g", "g":"f", "f":"e", "e":"d", "d":"c", "c":"b", "b":"a"}
s = list(input())
st = list(input())
num1 = int(s[1])
num2 = int(st[1])
ans = 0
res = ""

while True:
    if s[0] < st[0]:
        if num1 < num2:
            res += "RU\n"
            num1 += 1
            s[0] = ne[s[0]]
            ans += 1
        elif num1 > num2:
            res += "RD\n"
            num1 -= 1
            s[0] = ne[s[0]]
            ans += 1
        else:
            res += "R\n"
            s[0] = ne[s[0]]
            ans += 1
    elif s[0] >  st[0]:
        if num1 < num2:
            res += "LU\n"
            num1 += 1
            s[0] = pr[s[0]]
            ans += 1
        elif num1 > num2:
            res += "LD\n"
            num1 -= 1
            s[0] = pr[s[0]]
            ans += 1
        else:
            res += "L\n"
            s[0] = pr[s[0]]
            ans += 1
    else:
        if num1 < num2:
            res += "U\n"
            num1 += 1
            ans += 1
        elif num1 > num2:
            res += "D\n"
            num1 -= 1
            ans += 1
        else:
            break
print(ans)
print(res)
