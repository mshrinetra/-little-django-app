from django.shortcuts import render
from django.views import generic
from .models import Story


class IndexView(generic.ListView):
    model = Story
    template_name = 'story/index.html'
    context_object_name = 'stories'


class DetailView(generic.DetailView):
    model = Story
    template_name = 'story/detail.html'
    context_object_name = 'story'


class CreateView(generic.CreateView):
    model = Story
    template_name = 'story/create.html'


class EditView(generic.UpdateView):
    model = Story
    template_name = 'story/edit.html'
    context_object_name = 'story'


class DeleteView(generic.DeleteView):
    model = Story
    context_object_name = 'story'
