def solution(a,b):
    return sum(range(min(a,b), max(a,b)+1))

#가우스의 덧셈 공식 help: gemini
def solution(a, b):
    # (양끝 수의 합) * (숫자의 개수) / 2
    return (a + b) * (abs(a - b) + 1) // 2