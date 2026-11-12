def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort by start value
    intervals = sorted(intervals, key=lambda x: x[0])

    merged = []
    current = intervals[0][:]  # copy so the input isn't mutated

    for start, end in intervals[1:]:
        if start <= current[1]:
            # Overlap: extend the current interval
            current[1] = max(current[1], end)
        else:
            # No overlap: save current and start a new one
            merged.append(current)
            current = [start, end]

    merged.append(current)  # don't forget the last one
    return merged


intervals = [[1, 3], [2, 6], [8, 10], [9, 12]]
print(merge_intervals(intervals))  # [[1, 6], [8, 12]]