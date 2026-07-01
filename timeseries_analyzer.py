# Simple helper script for sequential dataset stats calculation
import numpy as np
import pandas as pd

def basic_stats(series):
    """Calculate basic statistical metrics for a numeric sequence"""
    mean_val = np.mean(series)
    std_val = np.std(series)
    max_v = np.max(series)
    min_v = np.min(series)
    return mean_val, std_val, max_v, min_v

def slice_by_range(df, start_id, end_id):
    """Filter dataframe rows within given time id range"""
    filtered = df[(df["time_id"] >= start_id) & (df["time_id"] <= end_id)]
    return filtered

if __name__ == "__main__":
    # quick test block
    test_data = pd.Series(np.random.randn(100))
    avg, std, max_num, min_num = basic_stats(test_data)
    print(f"Average value: {avg:.2f}")
    print(f"Standard deviation: {std:.2f}")
    print(f"Max / Min: {max_num:.2f} / {min_num:.2f}")