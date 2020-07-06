from django.contrib import admin
from .models import Topic, Course, Student, Order

admin.site.register(Topic)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Order)
