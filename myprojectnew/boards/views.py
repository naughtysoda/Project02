from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Board
from django.views.generic import UpdateView
from django.views.generic import TemplateView
from django.urls import path

class ChartView(TemplateView):
    template_name = 'chart.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Board.objects.all().order_by('-star')
       
        return context

def home(request):
    mgs = {
                    'massage' : ' '
                }
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        comment = request.POST.get('comment')
        rate = request.POST.get('rate')
        x_create = Board(
            firstname = firstname,
            description = comment,
            star = rate
        )
        x_create.save()
        mgs = {
                    'massage' : 'Done'
                }
         
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards,'mgs': mgs})

def table(request):
    boards = Board.objects.all().order_by('id')
    return render(request, 'table.html', {'boards': boards})

def edit(request,Progress_ID):
    boards = Board.objects.get(pk=Progress_ID)
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        comment = request.POST.get('comment')
        rate = request.POST.get('rate')
        boards.firstname = firstname
        boards.description = comment
        boards.star = rate
        boards.save()
        return redirect('table')
    return render(request, 'edit.html',{'boards':boards})

def chart(request):
    # do something...
    return render(request, 'chart.html')

def about(request):
    # do something...
    return render(request, 'about.html')

def about_company(request):
    # do something else...
    # return some data along with the view...
    return render(request, 'about_company.html', {'company_name': 'Simple Complex'})

# def board_topics(request, pk):
#     board = Board.objects.get(id=pk)
#     return render(request, 'topics.html', {'board': board})

# def new_topic(request, pk):
#     board = get_object_or_404(Board, pk=pk)
#     user = User.objects.first()  # TODO: get the currently logged in user
#     if request.method == 'POST':
#         form = NewTopicForm(request.POST)
#         if form.is_valid():
#             topic = form.save(commit=False)
#             topic.board = board
#             topic.starter = user
#             topic.save()
#             post = Post.objects.create(
#                 message=form.cleaned_data.get('message'),
#                 topic=topic,
#                 created_by=user
#             )
#             return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
#     else:
#         form = NewTopicForm()
#     return render(request, 'new_topic.html', {'board': board, 'form': form})

