import json
import matplotlib.pyplot as plt

def generate_heatmap():
    with open("suspicion_log.json", "r") as f:
        log = json.load(f)

    times = [entry["timestamp"] for entry in log]
    scores = [entry["score"] for entry in log]

    plt.plot(times, scores, color='red')
    plt.title("Cheating Suspicion Heatmap")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Suspicion Score")
    plt.grid(True)
    plt.show()
