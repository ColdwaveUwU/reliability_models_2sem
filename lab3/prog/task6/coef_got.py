# CUM.% from table
cumulative_percent = [38.28, 77.03, 94.40, 99.11, 99.91, 99.99, 100.00, 100.00]
i_values = list(range(len(cumulative_percent)))

def get_interval_percent(cum_percent):
    intervals = [cum_percent[0]]
    for idx in range(1, len(cum_percent)):
        intervals.append(cum_percent[idx] - cum_percent[idx-1])
    return intervals

intervals = get_interval_percent(cumulative_percent)
threshold = 5
availability = sum(intervals[i] for i in range(len(intervals)) if i <= threshold)

print(f"Коэффициент готовности системы: {availability:.4f} или {availability:.2f}%")
