from django.shortcuts import redirect, render
from .forms import TopicForm
from .models import Topic


# Create your views here.
def index(request):
    return render(request,'MainApp/index.html')

def topics(request):
    topics = Topic.objects.all().order_by('date_added')

    context= {'topics':topics}
    #the key of this dictionary is going to be what you used on the template, whatever you call your key is what you use in the template


    return render(request, 'MainApp/topics.html', context)

def topic(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}

    return render(request, 'MainApp/topic.html', context)

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else: 
        form=TopicForm(data=request.POST)
        if form.is_valid():
            form.save()

            return redirect('MainApp:topics')

    context= {'form':form}
    return render (request, 'MainApp/new_topic.html',context)