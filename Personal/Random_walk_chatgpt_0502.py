import numpy as np
import matplotlib.pyplot as plt


def random_walk_1d_increments(steps):
    """Simulate increments of a 1D random walk (±1)."""
    return np.random.choice([-1, 1], size=steps)


def ergodic_test_position(steps, trials):
    """
    Test the ergodic hypothesis using positions (cumulative sum of increments).
    Returns time averages (per trial) and ensemble averages (per step).
    """
    increments = np.array(
        [random_walk_1d_increments(steps) for _ in range(trials)]
    )  # (trials, steps)
    positions = np.cumsum(increments, axis=1)  # 누적 위치 계산
    time_averages = np.mean(positions, axis=1)  # 각 경로의 시간평균
    ensemble_averages = np.mean(positions, axis=0)  # 각 시간스텝별 앙상블 평균
    return time_averages, ensemble_averages


# Parameters
steps = 10000
trials = 1000

# Run experiment
time_averages, ensemble_averages = ergodic_test_position(steps, trials)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(range(steps), ensemble_averages, label="Ensemble Average (Position)")
plt.axhline(
    np.mean(time_averages), color="r", linestyle="--", label="Time Average (Position)"
)
plt.title("Ergodic Hypothesis Test via Random Walk Positions")
plt.xlabel("Steps")
plt.ylabel("Average Position")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
