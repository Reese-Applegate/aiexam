import numpy as np
import matplotlib.pyplot as plt


def ornstein_uhlenbeck_process(steps, mu=0, sigma=1, dt=0.1, theta=0.1):
    """Simulate 1D Ornstein-Uhlenbeck process."""
    x = np.zeros(steps)
    for t in range(1, steps):
        dx = theta * (mu - x[t - 1]) * dt + sigma * np.sqrt(dt) * np.random.normal(
            size=1
        )
        x[t] = x[t - 1] + dx
    return x


def simulate_2d_ornstein_uhlenbeck(steps, trials, mu=0, sigma=1, dt=0.1, theta=0.1):
    """Simulate 2D Ornstein-Uhlenbeck process."""
    x_walks = np.array(
        [ornstein_uhlenbeck_process(steps, mu, sigma, dt, theta) for _ in range(trials)]
    )
    y_walks = np.array(
        [ornstein_uhlenbeck_process(steps, mu, sigma, dt, theta) for _ in range(trials)]
    )
    return x_walks, y_walks


def plot_3d_ou_walks(x_walks, y_walks):
    fig = plt.figure(figsize=(12, 7))
    ax = fig.add_subplot(111, projection="3d")

    steps = x_walks.shape[1]
    t = np.arange(steps)

    # Plot each 2D Ornstein-Uhlenbeck path
    for x, y in zip(x_walks, y_walks):
        ax.plot(t, x, y, alpha=0.4)

    # Ensemble average
    ensemble_avg_x = np.mean(x_walks, axis=0)
    ensemble_avg_y = np.mean(y_walks, axis=0)
    ax.plot(
        t,
        ensemble_avg_x,
        ensemble_avg_y,
        color="black",
        label="Ensemble Average",
        linewidth=2,
    )

    # Time average (mean of time averages for each trial)
    avg_time_x = np.mean(np.mean(x_walks, axis=1))
    avg_time_y = np.mean(np.mean(y_walks, axis=1))
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
    ax.set_title("2D Ornstein-Uhlenbeck Process: Ensemble vs Time Average (3D)")
    ax.legend()
    plt.tight_layout()
    plt.show()


# Parameters
steps = 1000
trials = 500

# Run simulation
x_walks, y_walks = simulate_2d_ornstein_uhlenbeck(steps, trials)

# Plot the results
plot_3d_ou_walks(x_walks, y_walks)
