scores = [85.0, 89.6, 68.7]

def calculate_average(scores: list[float]) -> float:
    if not scores:
        raise ValueError("Value must not be empty")
    return sum(scores) / len(scores)


calculate_average(scores)