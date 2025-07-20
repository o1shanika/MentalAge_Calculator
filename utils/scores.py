def calculate_mental_age(responses, bio_age, gender):
    score = 0
    # A more robust way to parse the score from the answer string
    for _, answer in responses.items():
        try:
            # Assumes the format is "1. Some answer"
            points = int(answer.split(".")[0])
            score += points
        except (ValueError, IndexError):
            # Default to 1 point if parsing fails
            score += 1

    # Avoid division by zero if there are no responses
    avg_score = score / len(responses) if responses else 0

    # More nuanced scoring logic based on the average score
    if avg_score >= 3.5:
        base_adjustment = -10  # Very mature mindset
    elif avg_score >= 2.5:
        base_adjustment = -5   # Mature mindset
    elif avg_score >= 1.5:
        base_adjustment = 0    # Mindset aligns with age
    else:
        base_adjustment = 5    # Younger mindset

    mental_age = bio_age + base_adjustment

    # Example of a small adjustment based on gender (can be customized or removed)
    if gender == "Female" and bio_age > 30:
        mental_age -= 1  # Subtle adjustment

    # Clamp the result to a reasonable range
    return max(5, min(90, mental_age))
