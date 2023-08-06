class Base:
    def __init__(self, response):
        self.response = response


class Department(Base):
    def __init__(self, response):
        super().__init__(response)
        self.schedule_sync_time = response.get("schd_sync_dtm")

        department_info = self.response.get("Dept_Info")
        self.department = department_info.get("department")
        self.abbreviation = department_info.get("abbreviation")
        self.phone_number = department_info.get("phone_number")
        self.address = department_info.get("address")
        self.notes = department_info.get("Notes")
        self.term_notes = department_info.get("TermNotes")
        self.department_url = department_info.get("dept_url")
        self.offered_courses = self.get_offered_courses()

    def get_offered_courses(self):
        if type(self.response.get("OfferedCourses").get("course")) is list:
            return [Course(response) for response in self.response.get("OfferedCourses").get("course")]
        elif type(self.response.get("OfferedCourses").get("course")) is dict:
            return [Course(self.response.get("OfferedCourses").get("course"))]
        else:
            return []


class Course(Base):
    def __init__(self, response):
        super().__init__(response)
        self.cross_listed = response.get("IsCrossListed")
        self.published_course_id = response.get("PublishedCourseID")
        self.scheduled_course_id = response.get("ScheduledCourseID")
        self.course_data = self.get_course_data()

    def get_course_data(self):
        return CourseData(self.response.get("CourseData"))


class CourseData(Base):
    def __init__(self, response):
        super().__init__(response)
        self.prefix = response.get("prefix")
        self.number = response.get("number")
        self.sequence = response.get("sequence")
        self.suffix = response.get("suffix")
        self.title = response.get("title")
        self.description = response.get("description")
        self.units = response.get("units")
        self.restriction_by_major = response.get("restriction_by_major")
        self.restriction_by_class = response.get("restriction_by_class")
        self.restriction_by_school = response.get("restriction_by_school")
        self.course_notes = response.get("CourseNotes")
        self.course_term_notes = response.get("CourseTermNotes")
        self.prereq_text = response.get("prereq_text")
        self.coreq_text = response.get("coreq_text")
        self.section_data = self.get_section_data()

    def get_section_data(self):
        if type(self.response.get("SectionData")) is list:
            return [SectionData(response) for response in self.response.get("SectionData")]
        elif type(self.response.get("SectionData")) is dict:
            return [SectionData(self.response.get("SectionData"))]
        else:
            return []


class SectionData(Base):
    def __init__(self, response):
        super().__init__(response)
        self.id = response.get("id")
        self.session = response.get("session")
        self.dclass_code = response.get("dclass_code")
        self.title = response.get("title")
        self.section_title = response.get("section_title")
        self.description = response.get("description")
        self.notes = response.get("notes")
        self.type = response.get("type")
        self.units = response.get("units")
        self.spaces_available = response.get("spaces_available")
        self.number_registered = response.get("number_registered")
        self.wait_quantity = response.get("wait_qty")
        self.canceled = response.get("canceled")
        self.blackboard = response.get("blackboard")
        self.day = response.get("day")
        self.start_time = response.get("start_time")
        self.end_time = response.get("end_time")
        self.location = response.get("location")
        self.distance_learning = response.get("IsDistanceLearning")
        self.instructors = self.get_instructors()
        self.fees = self.get_fees()

    def get_instructors(self):
        if type(self.response.get("instructor")) is list:
            return [Instructor(response) for response in self.response.get("instructor")]
        elif type(self.response.get("instructor")) is dict:
            return [Instructor(self.response.get("instructor"))]
        else:
            return []

    def get_fees(self):
        if type(self.response.get("fee")) is list:
            return [Fee(response) for response in self.response.get("fee")]
        elif type(self.response.get("fee")) is dict:
            return [Fee(self.response.get("fee"))]
        else:
            return []


class Instructor(Base):
    def __init__(self, response):
        super().__init__(response)
        self.first_name = response.get("first_name")
        self.last_name = response.get("last_name")
        self.bio_url = response.get("bio_url")

    def get_name(self):
        return self.first_name + " " + self.last_name


class Fee(Base):
    def __init__(self, response):
        super().__init__(response)
        self.description = response.get("description")
        self.amount = response.get("amount")
