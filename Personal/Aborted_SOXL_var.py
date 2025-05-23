import FinanceDataReader as fdr
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

# 한글 폰트 설정
rc("font", family="Malgun Gothic")  # Windows의 경우
plt.rcParams["axes.unicode_minus"] = False  # 마이너스 기호 깨짐 방지

# 1. 최근 6개월 데이터 다운로드
recent_data = fdr.DataReader("SOXL", "2024-11-01", "2025-05-01")  # 최근 6개월 데이터

# 2. 1년 전 6개월 데이터 다운로드
one_year_ago_data = fdr.DataReader(
    "SOXL", "2023-11-01", "2024-05-01"
)  # 1년 전 6개월 데이터

# 데이터 유효성 확인
if not recent_data.empty and not one_year_ago_data.empty:
    # 3. 수익률 계산 (일일 수익률)
    recent_returns = recent_data["Close"].pct_change().dropna()
    one_year_ago_returns = one_year_ago_data["Close"].pct_change().dropna()

    # 4. Shannon 엔트로피 계산 함수
    def calculate_shannon_entropy(returns):
        # 확률 분포 계산
        hist, bins = np.histogram(returns, bins=20, density=True)
        probs = hist / hist.sum()

        # 엔트로피 계산
        entropy = -np.sum(probs[probs > 0] * np.log(probs[probs > 0]))
        return entropy

    # 5. 최근 6개월 데이터 엔트로피
    recent_entropy = calculate_shannon_entropy(recent_returns)

    # 6. 1년 전 6개월 데이터 엔트로피
    one_year_ago_entropy = calculate_shannon_entropy(one_year_ago_returns)

    # 결과 출력
    print(f"최근 6개월 SOXL의 Shannon 엔트로피: {recent_entropy:.4f} nats")
    print(f"1년 전 6개월 SOXL의 Shannon 엔트로피: {one_year_ago_entropy:.4f} nats")
else:
    print("데이터 다운로드 실패. 엔트로피를 계산할 수 없습니다.")

# Y축 범위 계산 (수익률)
min_return = min(recent_returns.min(), one_year_ago_returns.min())
max_return = max(recent_returns.max(), one_year_ago_returns.max())

# Y축 범위 계산 (엔트로피)
min_entropy = (
    min(recent_entropy, one_year_ago_entropy) * 0.9
)  # 여유를 두기 위해 10% 축소
max_entropy = (
    max(recent_entropy, one_year_ago_entropy) * 1.1
)  # 여유를 두기 위해 10% 확대

# 최근 6개월 데이터 시각화
plt.figure(figsize=(12, 6))

# 첫 번째 그래프: 최근 6개월 데이터
ax1 = plt.subplot(2, 1, 1)
ax1.plot(recent_returns.index, recent_returns, label="최근 6개월 수익률", color="blue")
ax1.set_title("최근 6개월 SOXL 수익률 및 엔트로피 변화")
ax1.set_xlabel("날짜")
ax1.set_ylabel("수익률")
ax1.set_ylim(min_return, max_return)
ax1.legend(loc="upper left")

# 두 번째 Y축: 엔트로피
ax2 = ax1.twinx()
ax2.axhline(
    recent_entropy, color="red", linestyle="--", label="엔트로피 변화"
)  # 엔트로피 값 표시
ax2.set_ylabel("엔트로피")
ax2.set_ylim(min_entropy, max_entropy)  # 엔트로피 Y축 범위 설정
ax2.legend(loc="upper right")

# 두 번째 그래프: 1년 전 6개월 데이터
ax3 = plt.subplot(2, 1, 2)
ax3.plot(
    one_year_ago_returns.index,
    one_year_ago_returns,
    label="1년 전 6개월 수익률",
    color="orange",
)
ax3.set_title("1년 전 6개월 SOXL 수익률 및 엔트로피 변화")
ax3.set_xlabel("날짜")
ax3.set_ylabel("수익률")
ax3.set_ylim(min_return, max_return)
ax3.legend(loc="upper left")

# 두 번째 Y축: 엔트로피
ax4 = ax3.twinx()
ax4.axhline(
    one_year_ago_entropy, color="green", linestyle="--", label="엔트로피 변화"
)  # 엔트로피 값 표시
ax4.set_ylabel("엔트로피")
ax4.set_ylim(min_entropy, max_entropy)  # 엔트로피 Y축 범위 설정
ax4.legend(loc="upper right")

plt.tight_layout()
plt.show()
