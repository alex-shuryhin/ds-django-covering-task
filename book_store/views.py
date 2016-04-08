from django.shortcuts import render
from models import Book
from django.views import generic
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from book_store.forms import BookForm
from django.contrib.auth.decorators import login_required
from book_store.models import RequestRecord
from datetime import date
from logging import StreamHandler
from book_store.signals import book_manipulation

class LoggingBooksManipulations(StreamHandler):
    def emit(self, record):
        msg = record.msg
        if (msg.find('book_store_book') != -1 and
                msg.find('INSERT') != -1 or msg.find('UPDATE') != -1 or msg.find('DELETE') != -1):
            book_manipulation.send(sender=self.__class__, msg=msg)

def copyright_context_processor(request):
    dict = {'start_year' : 2015,
            'end_year' : date.today().year }
    return dict

class RequestsView(generic.ListView):
    template_name = 'book_store/requests.html'
    context_object_name = 'request_list'

    def get_queryset(self):
        return RequestRecord.objects.order_by('-id')[:10]

class RequestKeeperMiddleware:
    def process_view(self, request, view, args, kwargs):
        record = RequestRecord(path = request.path)
        record.save()

@login_required
def book_edit(request, book_id):
    if request.POST:
        book = Book.objects.get(id=book_id)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/book_store/")
    else:
        book = Book.objects.get(id=book_id)
        form = BookForm(instance=book)
    dict = { 'form' : form, 'operation' : "Edit" }
    return render(request, 'book_store/book_edit.html', dict)

@login_required
def book_add(request):
    if request.POST:
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/book_store/")
    else:
        form = BookForm()
    dict = { 'form' : form, 'operation' : "Create" }
    return render(request, 'book_store/book_edit.html', dict)

def user_test(request):
    username = request.user.username
    if username:
        return HttpResponse("You are logged in as %s." % username)
    else:
        return HttpResponse("You are not logged in.")

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/book_store/")

def user_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            print request.POST['next']
            return HttpResponseRedirect(request.POST['next'])
        else:
            return HttpResponse('Invalid username or password')
    else:
        if request.GET:
            next = request.GET['next']
        else:
            next = '/book_store/'
        return render(request, 'book_store/user_login.html', {'next' : next})

def register(request):
    if request.POST:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username, email, password)
        user.save()
        return HttpResponse("Registration successfull.")
    else:
        return render(request, 'book_store/user_register.html')

class IndexView(generic.ListView):
    template_name = 'book_store/index.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        return Book.objects.order_by('title')