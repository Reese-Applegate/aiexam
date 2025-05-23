import numpy as np
import matplotlib.pyplot as plt
from scipy.special import zeta
from mpmath import zetazero, mp


# 리만 제타 함수 계산 (기본 연산으로 구현)
def riemann_zeta(s, terms=100000):
    """
    리만 제타 함수 ζ(s)를 근사적으로 계산합니다.
    :param s: 제타 함수의 입력 값 (s > 1)
    :param terms: 합산할 항의 개수 (무한 합을 근사적으로 계산)
    :return: ζ(s)의 근사값
    """
    if s <= 1:
        raise ValueError("s 값은 1보다 커야 합니다.")

    zeta_sum = 0
    for n in range(1, terms + 1):
        zeta_sum += 1 / (n**s)
    return zeta_sum


# 예제: s = 2, s = 3, s = 4
s_values = [2, 3, 4, 5, 6, 7, 8, 9, 10]
for s in s_values:
    result = riemann_zeta(s)
    print(f"ζ({s}) = {result}")

# mpmath 설정: 높은 정밀도 사용
mp.dps = 50  # 소수점 이하 50자리까지 계산


def compute_riemann_zeta_zeros():
    """
    리만 제타 함수의 비자명해를 계산하고 시각화합니다.
    """
    # 알려진 비자명해의 첫 번째 3개 계산
    zeros = [zetazero(n) for n in range(1, 4)]  # zetazero(n)은 n번째 비자명해를 반환

    # 출력
    for idx, zero in enumerate(zeros, start=1):
        print(f"Zero {idx}: {zero}")

    # 시각화
    plt.figure(figsize=(10, 6))
    plt.scatter(
        [z.real for z in zeros],
        [z.imag for z in zeros],
        color="red",
        label="Non-trivial Zeros",
    )
    plt.axvline(0.5, color="blue", linestyle="--", label="Critical Line (Re(s) = 0.5)")
    plt.title("Non-trivial Zeros of the Riemann Zeta Function", fontsize=16)
    plt.xlabel("Re(s)", fontsize=14)
    plt.ylabel("Im(s)", fontsize=14)
    plt.grid(True)
    plt.legend(fontsize=12)
    plt.show()


# 실행
compute_riemann_zeta_zeros()
