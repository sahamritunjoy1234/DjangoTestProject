from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to MyProject!")

def test_branch_1(request):
    return HttpResponse("This is a test branch view from the test-branch-1.")
