from django.shortcuts import render

# Create your views here.
def interest(request):
    context={'interest':'active'}
    return render(request,'interest/interest.html',context)
