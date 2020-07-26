from django.shortcuts import get_object_or_404, render, redirect

from .forms import OrderForm, InterestForm
from .models import Topic, Course


def index(request):
    top_list = Topic.objects.all().order_by('id')[:10]
    return render(request, "myapp/index.html", {'top_list': top_list})


def about(request):
    # return HttpResponse("This is an E-learning Website! Search our Topics to find all available Courses.")
    return render(request, "myapp/about.html")


def detail(request, top_no):
    # response = HttpResponse()
    # topic  = Topic.objects.get(id=top_no)          #Standard answer
    topic = get_object_or_404(Topic, id=top_no)  # Q4 Gives 404 if Topic not found
    course_list = Course.objects.filter(topic__id=top_no)
    # response.write(topic)
    # response.write('<p>' + 'List of courses: ' + '</p>')
    # for course in Course.objects.filter(topic__id=top_no):
    #     if course.for_everyone:
    #         for_str = "This Course is For Everyone!"
    #     else:
    #         for_str = "This Course is not For Everyone!"
    #     response.write('<p>' + str(course.id) + ': ' + str(course) + for_str + '</p>')
    # return response
    return render(request, "myapp/detail.html", {'topic': topic, 'course_list': course_list})


def courses(request):
    courlist = Course.objects.all().order_by('id')
    return render(request, 'myapp/courses.html', {'courlist': courlist})


def place_order(request):
    msg = ''
    discount = 0
    courlist = Course.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if order.levels <= order.course.stages:
                order.save()
                msg = 'Your course has been ordered successfully.'
                if order.course.price > 150:
                    discount = order.course.discount()
            else:
                msg = 'You exceeded the number of levels for this course.'
            return render(request, 'myapp/order_response.html', {'msg': msg, 'discount': discount})
    else:
        form = OrderForm()
    return render(request, 'myapp/placeorder.html', {'form': form, 'msg': msg, 'courlist': courlist})


def coursedetail(request, cour_id):
    course = get_object_or_404(Course, pk=cour_id)
    if request.method == 'POST':
        form = InterestForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data['interested'] == 1:
                course.interested += 1
            course.save()
            return redirect('myapp:index')
    elif request.method == 'GET':
        form = InterestForm()
        return render(request, 'myapp/coursedetail.html/', {'form': form, 'course': course})