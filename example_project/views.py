from django.shortcuts import render

from example_project.forms import CountableTestForm


def test_form_view(request):
    form = CountableTestForm()
    return render(request, "example_project/home.html", {'form': form})

