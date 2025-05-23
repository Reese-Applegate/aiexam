import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def random_walk_2d(steps):
    """Generate a 2D random walk."""
    directions = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])
    moves = directions[np.random.randint(0, 4, size=steps)]
    positions = np.cumsum(moves, axis=0)  # shape: (steps, 2)
    return positions


def ergodic_test_2d(steps, trials):
    walks = np.array(
        [random_walk_2d(steps) for _ in range(trials)]
    )  # shape: (trials, steps, 2)
    time_avg = np.mean(walks, axis=1)  # shape: (trials, 2)
    ensemble_avg = np.mean(walks, axis=0)  # shape: (steps, 2)
    return walks, time_avg, ensemble_avg


def plot_3d_ensemble_vs_time_avg(walks, time_avg, ensemble_avg):
    fig = plt.figure(figsize=(12, 7))
    ax = fig.add_subplot(111, projection="3d")

    steps = walks.shape[1]
    t = np.arange(steps)

    # Plot each random walk
    for walk in walks:
        ax.plot(t, walk[:, 0], walk[:, 1], alpha=0.4)

    # Plot ensemble average
    ax.plot(
        t,
        ensemble_avg[:, 0],
        ensemble_avg[:, 1],
        color="black",
        label="Ensemble Average",
        linewidth=2,
    )

    # Plot mean of time averages as a flat line
    avg_time_x = np.mean(time_avg[:, 0])
    avg_time_y = np.mean(time_avg[:, 1])
    ax.plot(
        t,
        [avg_time_x] * steps,
        [avg_time_y] * steps,
        color="red",
        linestyle="--",
        label="Time Average (mean)",
    )

    ax.set_xlabel("Time (steps)")
    ax.set_ylabel("X Position")
    ax.set_zlabel("Y Position")
    ax.set_title("2D Random Walks: Ensemble vs Time Average (3D)")
    ax.legend()
    plt.tight_layout()
    plt.show()


# Parameters
steps = 1000
trials = 50

# Run test
walks, time_avg, ensemble_avg = ergodic_test_2d(steps, trials)

# Plot
plot_3d_ensemble_vs_time_avg(walks, time_avg, ensemble_avg)
