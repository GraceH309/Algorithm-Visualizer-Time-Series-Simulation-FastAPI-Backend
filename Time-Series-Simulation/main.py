# Self-built sequential data simulation toolkit
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# calculate basic statistical metrics
def calc_metrics(data_series):
    avg = np.mean(data_series)
    max_val = np.max(data_series)
    min_val = np.min(data_series)
    std_dev = np.std(data_series)
    return avg, max_val, min_val, std_dev

# simple rule-based simulation runner
def run_simulation(raw_df, rule_threshold):
    output_records = []
    for idx, row in raw_df.iterrows():
        current_val = row["value"]
        # simple filter rule
        if current_val > rule_threshold:
            mark = 1
        else:
            mark = 0
        output_records.append({
            "timestamp": idx,
            "value": current_val,
            "signal_flag": mark
        })
    return pd.DataFrame(output_records)

# plot simulation result chart
def draw_sim_result(df):
    plt.figure(figsize=(10,4))
    plt.plot(df["timestamp"], df["value"], label="dataset value")
    plt.scatter(df[df["signal_flag"]==1]["timestamp"], df[df["signal_flag"]==1]["value"], c="red")
    plt.legend()
    plt.title("Sequential Dataset Simulation Output")
    plt.savefig("simulation_output.png")
    plt.show()

if __name__ == "__main__":
    # generate dummy sequential dataset
    time_axis = list(range(1, 101))
    value_seq = np.random.normal(loc=50, scale=8, size=100)
    test_df = pd.DataFrame({"timestamp": time_axis, "value": value_seq})

    # run simulation
    sim_result = run_simulation(test_df, rule_threshold=55)
    mean, maxv, minv, std = calc_metrics(sim_result["value"])

    # print metric results for quick check
    print(f"Average: {mean:.2f}, Max: {maxv:.2f}, Min: {minv:.2f}, Std: {std:.2f}")
    draw_sim_result(sim_result)