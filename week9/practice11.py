#dictionary comprehensions you can create a dictionary on the fly

students = ["Hermonie", "Harry", "Ron"]

gryffindors = {student : "Gryffindor" for student in students}

print(gryffindors)