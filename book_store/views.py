from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import Book, RequestRecord
from .forms import BookForm
from .viewmixins import LoginRequiredMixin

class RequestsView(generic.ListView):
    template_name = 'book_store/requests.html'
    context_object_name = 'request_list'
    queryset = RequestRecord.get_last_10_items()

class BookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Book
    form_class = BookForm
    template_name_suffix = '_update'

class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Book
    form_class = BookForm
    template_name_suffix = '_create'

def user_test(request):
    username = request.user.username
    if username:
        return HttpResponse("You are logged in as %s." % username)
    else:
        return HttpResponse("You are not logged in.")

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/book_store/")

def user_login(request):    #Method not incapsulated in model because of form.save incapsulation.
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
        return render(request, 'book_store/login.html', {'next' : next})

class UserRegisterView(generic.CreateView):
    template_name = 'book_store/register.html'
    model = User
    fields = ['username', 'email', 'password']
    success_url = '/book_store/'

class IndexView(generic.ListView):
    template_name = 'book_store/index.html'

    def get_queryset(self):
        return Book.objects.order_by('title').select_related('author')