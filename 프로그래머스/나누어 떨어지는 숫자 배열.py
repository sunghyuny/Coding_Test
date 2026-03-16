# array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
# divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

def solution(arr,divisor):
    ans = []
    for i in arr: # - arr을 순회한다
        if i % divisor == 0: #- arr[i] divsior랑 나눠서 나머지가 0이면 ans에 추가한다
            ans.append(i)
    return sorted(ans) if ans else [-1] # - ans를 정렬한다. 만약 ans가 비어있으면 [-1]을 반환한다.

print(solution([5,9,7,10],5))



def solution2(arr,divisior):
    ans = [i for i in arr if i % divisior ==0]
    return sorted(ans) if ans else [-1]

print(solution2([5,9,7,10],5))