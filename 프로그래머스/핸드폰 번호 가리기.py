
# 프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
# 전화번호가 문자열 phone_number로 주어졌을 때, 
# 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

#핸드폰 뒤 4자리만 보여준다 -> 그럼 번호를 *로 바꾸고 뒷자리만 남긴다 -> 그리고 4자리만 남기니까 len에서 -4를 한다

def solution(phone_number):
    return "*" * (len(phone_number) -4) + phone_number[-4:]

print(solution("01031182957"))