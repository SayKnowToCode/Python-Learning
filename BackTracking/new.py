n = 4
output = []

for i in range(n):
    output.append(['.'] * n)

print(output)
output[1][2] = 'Q'

def outputToString():
    ans = []
    for i in range(n):
        ans.append(''.join(output[i]))
    return ans

ans = outputToString()
print(ans)
print(output)