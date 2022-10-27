#!/usr/bin/python3
result = [list(str(11**i)) for i in range(5)]
result = [[int(i) for i in j] for j in result]
print(result)
