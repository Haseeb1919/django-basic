from django.shortcuts import render
from django.http import HttpResponse
from .models import Item, TodoList
from .forms import createnewlist


#function to render the home page
from django.http import HttpResponse, Http404

def home(request):
    return render(request, "main/home.html")

#function to render the about page
def about(response):
    return render(response, "main/about.html", {"name": "About page"})

#function to render the contact page
def contact(response):
    return render(response, "main/contact.html")

#function to render the create page
def create(response):
    form = createnewlist()
    return render(response, "main/create.html", {"form": form})


#function to render the todo list page
def index(response, id):
    try:
        ls = TodoList.objects.get(id = id)  # Get the TodoList that has the title passed as a parameter
        item = ls.item_set.first()  # Get the first item or None if no items exist

        if not ls:
            raise Http404("TodoList does not exist")  # Handle case when TodoList is not found
    except TodoList.DoesNotExist:
        raise Http404("TodoList does not exist")  # Handle case when TodoList is not found

    title = ls.title if ls else "No TodoList with this ID"
    text = item.text if item else "No items in this TodoList"

    return render(response, "main/list.html", {"ls": ls, "title": title, "text": text})
