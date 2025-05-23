# 순서        0 1 2 3 4
# 인덱스     -5 -4 -3 -2 -1
listData1 = [1.0, 2.0, 3.0, 4.0, 5.0]

print(listData1)
print(type(listData1))  # <class 'list'>
print(listData1[3])  # 1
print(type(listData1[3]))  # <class 'int'>
print(listData1[-1])
print(type(listData1[-1]))  # <class 'int'>
# 마지막 값으로 오류를 확인한다. (데이터 개수 등)
# 중간값만 오류가 나는 경우는 거의 없다. 나면, 천재지변이다.


# 리스트 다중 리스트
#              0  1  2  3
# 인덱스       -4 -3 -2 -1
#                     0   1   2
# 인덱스              -3  -2  -1
listData2 = [1, 2, 3, ["a", "b", "c"]]
# print(listData2[-1][1])

a = [
    1,
    2,
    3,
    4,
    5,
]  # 슬라이싱 : 데이터를 일부 추출하는 것; 특정한 영역 부분만을 잘라내는 것

print(a[1:4])  # Python은 기본적으로 이상과 미만이다.

b = [1, 2, 3, ["a", "b", "c"], 4, 5]

print(b[::-1])  # [첫번째위치:마지막위치:시작위치] 생략하면 끝과 끝
print(b[:])
print("-" * 60)
c = [1, 2, 3]
d = [4, 5, 6]
print(c + d)  # 리스트 더하기
print(c * 3)  # 리스트 곱하기
print("-" * 60)
