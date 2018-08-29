from django.db import models

# Create your models here.


class CoursesNames(models.Model):
    DB = "data structure"
    SF = "software enginering"
    DS = "discrete structure "
    WD = "web dev"
    courseChoices = (
        (DB, "data structure"),
        (SF, "software enginering "),
        (DS, "discrete structure"),
        (WD, "web dev"),
    )
    courses = models.CharField(max_length=50, choices=courseChoices)

    def __str__(self):
        return self.courses


class Document(models.Model):
    course_name = models.ForeignKey(
        CoursesNames, on_delete=models.CASCADE, related_name='document_courses')

    def content_file_name(self, course_name):
        file_path = "documents/{courses}/{filename}".format(
            courses=self.course_name, filename=course_name)
        return file_path
    title = models.CharField(max_length=100)
    description = models.TextField(
        help_text="A little description can be very helpful for others!")
    document = models.FileField(upload_to=content_file_name)
    uploaded_at = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return "{}".format(self.course_name)
