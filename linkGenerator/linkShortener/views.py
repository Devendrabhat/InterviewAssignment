from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from .forms import LinkForm

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'
    output = 'output.html'

    def get(self, request, *args, **kwargs):
        form = LinkForm()
        return render(request,self.template_name,{'form':form})

    def post(self,request, *args, **kwargs):
        form = LinkForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['link']

        return render(request,self.output,{'text':text})


# def home(request):
#     if request.method == 'POST':
#         form = LinkForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('/output/')
#     else:
#         form = LinkForm()
#     return render(request,'home.html',context={'form': form})
#
# def output(request):
#     return render(request,'output.html',context={})