STUDENT_DB = {
    101: {"name": "Alice", "grades": [88, 92, 95]},
    102: {"name": "Bob", "grades": [75, 80, 85]},
    103: {"name": "Charlie", "grades": [90, 85, 88]}
}

def get_student(student_id):
    return STUDENT_DB.get(student_id)

def calculate_average(grades):
    return round(sum(grades) / len(grades), 2) if grades else 0
