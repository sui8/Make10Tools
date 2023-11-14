import itertools as it

def run(inpt):

    pattern = list(it.product(["+", "-", "×", "÷"], repeat=3))
    inputs = list(it.permutations(inpt, 4))

    for a in inputs:   
        for i in range(len(pattern)):
            tmp = a[0]
            
            for j in range(3):
                if pattern[i][j] == "+":
                    tmp += a[j + 1]

                elif pattern[i][j] == "-":
                    tmp -= a[j + 1]

                elif pattern[i][j] == "×":
                    tmp *= a[j + 1]

                else:
                    try:
                        tmp /= a[j + 1]

                    except:
                        tmp = 100000

            #print(a, pattern[i], tmp)
            
            if isinstance(tmp, int):
                if tmp == 10:
                    ans = f"{a[0]} {pattern[i][0]} {a[1]} {pattern[i][1]} {a[2]} {pattern[i][2]} {a[3]}"
                    return ans
                    

            else:
                if round(tmp) == 10 and tmp.is_integer():
                    ans = f"{a[0]} {pattern[i][0]} {a[1]} {pattern[i][1]} {a[2]} {pattern[i][2]} {a[3]}"
                    return ans

    return "Not found"

while True:
    print(run(list(map(int, input().split()))))
