class Teacher:
    def __init__(self, teacher_id, name):
        self.name = name
        self.teacher_id = teacher_id
        self.created_course = []

    def create_course(self, course):
        self.created_course.append(course)

    def view_created_course(self):
        return self.created_course

