from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Topic, Course


def index(request):
    top_list = Topic.objects.all().order_by('id')[:10]
    response = HttpResponse()
    heading1 = '<p>' + 'List of topics: ' + '</p>'
    response.write(heading1)
    for topic in top_list:
        para = '<p>' + str(topic.id) + ': ' + str(topic) + '</p>'
        response.write(para)

    response.write('<p>' + 'List of courses: ' + '</p>')
    for course in Course.objects.all().order_by('-price')[:5]:
        if course.for_everyone:
            for_str = "This Course is For Everyone!"
        else:
            for_str = "This Course is not For Everyone!"
        response.write('<p>' + str(course.id) + ': ' + str(course) + for_str + '</p>')
    return response


def about(request):
    return HttpResponse("This is an E-learning Website! Search our Topics to find all available Courses.")


def detail(request, top_no):
    response = HttpResponse()
    #topic  = Topic.objects.get(id=top_no)          #Standard answer
    topic = get_object_or_404(Topic, id=top_no)     #Q4 Gives 404 if Topic not found
    response.write(topic)

    response.write('<p>' + 'List of courses: ' + '</p>')
    for course in Course.objects.filter(topic__id=top_no):
        if course.for_everyone:
            for_str = "This Course is For Everyone!"
        else:
            for_str = "This Course is not For Everyone!"
        response.write('<p>' + str(course.id) + ': ' + str(course) + for_str + '</p>')
    return response
