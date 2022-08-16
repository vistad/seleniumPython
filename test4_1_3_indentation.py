@pytest.mark.regression
# out of class - no indentation
def test_student_can_see_lesson_name_in_lesson_in_course_after_joining(self, driver):
    # all lines in the test are indented
    page = CoursePromoPage(url=self.course.url, driver=driver)
    page.open()


class TestLessonNameInCourseForTeacher():
    @pytest.mark.regression
    # a test in a class requires indentation
    def test_teacher_can_see_lesson_name_in_lesson_in_course(self, driver):
        # indentation for nesting
        page = LessonPlayerPage(url=self.lesson_url, driver=driver)
        page.open()
        try:
            # indentation for each level of nesting
            dangerous_function()
        except:
            close_something()

