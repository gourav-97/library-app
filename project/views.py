import sys
import json
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse, render, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from .models import Books, LibraryUser


def login_page(request):
    try:
        return render(request, 'project/login.html', {})

    except BaseException, e:
        print str(e) + str(sys.exc_traceback.tb_lineno)
        return HttpResponse("page not found")


@csrf_exempt
def user_login_request(request):
    try:
        if request.method == 'POST':

            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is None:
                return HttpResponse("invalid user")

            library_user = get_library_user(user)

            if library_user is None:
                return HttpResponse("you are not a registered user")

            login(request, user)
            return HttpResponseRedirect(reverse('form_page'))

    except BaseException, e:
        print str(e) + str(sys.exc_traceback.tb_lineno)
        return HttpResponse("page not found")


def get_library_user(user):
    try:
        library_user = LibraryUser.objects.get(library_user_belongs_to_user=user)
        return library_user

    except BaseException, e:
        print str(e) + str(sys.exc_traceback.tb_lineno)
        return None


def form_page(request):
    try:
        books_list = Books.objects.all().order_by('book_title')
        user = LibraryUser.objects.get(library_user_belongs_to_user=request.user)

        if user.is_user_librarian == True:
            librarian = True

        else:
            librarian = False

        context = {
            'books_list': books_list,
            'is_librarian': librarian,
        }
        return render(request, 'project/form_page.html', context)

    except BaseException, e:
        print str(e) + str(sys.exc_traceback.tb_lineno)
        return HttpResponse("page not found")



def add_book_request(request):
    try:

        if request.method == 'POST':
            info = dict()
            print request.POST


            info['book_author'] = request.POST['book_author']
            info['book_price'] = request.POST['book_price']
            info['book_title'] = request.POST['book_title']
            info['book_author_contact'] = request.POST['book_author_contact']

            created_book = add_book(info)

            if created_book:
                return render(request, 'project/form_page.html', {})

            return HttpResponse("error")


    except BaseException, e:
        print str(e) + str(sys.exc_traceback.tb_lineno)
        return HttpResponse("unable to render request")






def add_book(info):
    try:
        book = Books()
        book.book_title = info['book_title']
        book.book_author = info['book_author']
        book.book_price = info['book_price']
        book.book_author_contact = info['book_author_contact']
        book.save()
        return book

    except BaseException, e:
        print str(e) + str(sys.exc_traceback.tb_lineno)
        return None


