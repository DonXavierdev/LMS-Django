from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()


    def __str__(self):
        return self.title
    
class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    video = models.CharField(max_length=200)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} - {self.title}"