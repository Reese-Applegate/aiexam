import numpy as np
import matplotlib.pyplot as plt


def random_walk_1d_increments(steps):
    """Simulate increments of a 1D random walk."""
    return np.random.choice([-1, 1], size=steps)


def ergodic_test(steps, trials):
    """Test the ergodic hypothesis using random walk increments."""
    increments = np.array(
        [random_walk_1d_increments(steps) for _ in range(trials)]
    )  # (trials, steps)
    time_averages = np.mean(increments, axis=1)  # 각 실현별 time average
    ensemble_averages = np.mean(increments, axis=0)  # 각 step별 ensemble average
    return time_averages, ensemble_averages


# Parameters
steps = 1000
trials = 100

# Perform the test
time_averages, ensemble_averages = ergodic_test(steps, trials)

# Plot results
plt.figure(figsize=(10, 5))
plt.plot(range(steps), ensemble_averages, label="Ensemble Average (increments)")
plt.axhline(
    np.mean(time_averages), color="r", linestyle="--", label="Time Average (increments)"
)
plt.title("Ergodic Hypothesis Test via Random Walk Increments")
plt.xlabel("Steps")
plt.ylabel("Average")
plt.legend()
plt.show()
