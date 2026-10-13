def calculate_grade(score:int) -> str:
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    elif score >= 0:
        return "F"
    else:
        raise ValueError("Score cannot be negative")