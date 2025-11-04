from .links import notes, pyq, syllabus

def processCommand(c):
    c = c.lower()

    if "note" in c or "notes" in c:
        for subject in notes:
            if subject.lower() in c:
                return f"Here are the {subject.upper()} notes: {notes[subject]}"

    if "previous year question" in c or "pyq" in c:
        for subject in pyq:
            if subject.lower() in c:
                return f"Here are the {subject.upper()} PYQs: {pyq[subject]}"

    if "syllabus" in c:
        for subject in syllabus:
            if subject.lower() in c:
                return f"Here is the {subject.upper()} syllabus: {syllabus[subject]}"

    return None
