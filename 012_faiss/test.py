# a는 1이고, b는 2인경우를 처리하라.
a = 1
b = 2
if a == 1 and b ==2:
    print("맞소.")


# Instead,

if a != 1:
    exit()
if b != 2:
    exit()
print("맞소.")

# 조건을 하나씩 제거하는 방식이 복잡할 때 더 유용하다. 