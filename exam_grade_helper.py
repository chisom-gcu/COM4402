def classify_mark(mark):
    if mark < 40:
        return "Fail"
    elif mark < 70:
        return "Pass"
    else:
        return "Distinction"

