students = [
    ("Paula", 88),
    ("Carlos", 72),
    ("Maria", 95),
    ("Luis", 60),
    ("Ana", 81)
]

def student_record() -> str:
    record = ''
    for index, (name, score) in enumerate(students, 1):
        if score >= 70:
            record += f"{index}. {name} - {score} | PASSED\n"
        else:
            record += f"{index}. {name} - {score} | FAILED\n"
    return record

if __name__ == "__main__":
    print(student_record())
