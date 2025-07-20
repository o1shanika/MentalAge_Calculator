import json

def load_questions(age, gender):
    """
    Loads questions from the JSON file based on the user's age.
    It will load questions marked for 'all' and for the specific age group
    and gender.
    """
    try:
        with open("data/questions.json", "r", encoding="utf-8") as f:
            all_questions = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return [] # Return empty list on error

    if age < 18:
        age_category = "teen"
    elif 18 <= age < 40:
        age_category = "adult"
    else:
        age_category = "senior"

    # Filter questions based on both age group and gender.
    # A question is included if its age_group matches (or is 'all') AND
    # its gender matches (or is 'all', or is not specified).
    return [
        q for q in all_questions
        if q.get("age_group", "all") in ["all", age_category]
        and q.get("gender", "all").lower() in ["all", gender.lower()]
    ]
