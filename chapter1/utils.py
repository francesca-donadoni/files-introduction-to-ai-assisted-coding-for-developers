def validate_grade(grade):
    if not 0 <= grade <= 100:
        raise ValueError("Grade must be 0-100")


def convert_to_letter(grade):
    if grade >= 90: 
        return "A"
    if grade >= 80: 
        return "B"
    if grade >= 70: 
        return "C"
    return "F"
