from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, null=True)

    def __str__(self):
        return "{ Name: " + self.name + \
               "; Category: " + self.category + " }"


class Course(models.Model):
    topic = models.ForeignKey(Topic, related_name='courses', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    for_everyone = models.BooleanField(default=True)
    description = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return "{ Name: " + self.name + \
               "; Price: " + str(self.price) + \
               "; For Everyone: " + str(self.for_everyone) + \
               "; Topic: " + self.topic.name + \
               "; Description: " + (self.description or "NA") + "} "


class Student(User):
    CITY_CHOICES = [('WS', 'Windsor'), ('CG', 'Calgary'), ('MR', 'Montreal'), ('VC', 'Vancouver')]
    school = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=2, choices=CITY_CHOICES, default='WS')
    interested_in = models.ManyToManyField(Topic)

    def __str__(self):
        return "{ Name: " + self.first_name + " " + self.last_name + \
               "; School: " + self.school + \
               "; City: " + self.city + \
               "; Interested in: " + str(self.interested_in.values_list("name")) + "} "


class Order(models.Model):
    course = models.ManyToManyField(Course)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    levels = models.PositiveIntegerField(default=0)
    ORDER_CHOICES = [(0, 'Cancelled'), (1, 'Order Confirmed')]
    order_status = models.IntegerField(choices=ORDER_CHOICES, default=1)
    order_date = models.DateField(auto_now_add=True, editable=False)

    def total_cost(self):
        return sum(course.price for course in self.course.all())

    def __str__(self):
        return "{ Student: " + str(self.student.first_name + " " + self.student.last_name) + \
               "; Courses: " + str(self.course.values_list("name")) + \
               "; Levels: " + str(self.levels) + \
               "; Order Status: " + str(self.order_status) + \
               "; Order Date: " + str(self.order_date) + "} "


# def set_level(sender, **kwargs):
#     if kwargs['action'] == 'post_add':
#         order = kwargs['instance']
#         order.levels = len(kwargs['pk_set'])  # Length of Primary key set of Many-Many Relation
#         order.save()

# m2m_changed.connect(set_level, sender=Order.course.through)
