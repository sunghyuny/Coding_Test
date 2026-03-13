import math

def solution(n):
    x = int(math.sqrt(n))
    return math.pow(x+1,2) if x * x == n else -1


print(solution(3))



def gemini(n):
    x = n ** 0.5
    return (x+1) ** 2 if x % 1 == 0 else -1