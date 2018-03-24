from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from .models import LinkModel
from .forms import LinkForm
from .linkGenerator import Generator
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'
    output = 'output.html'
    gen = Generator()
    linksAndShortlinks = {}

    def get(self, request, *args, **kwargs):
        form = LinkForm()
        links = LinkModel.objects.all().order_by('-date')

        allLinks = links[0]
        # Extracting out all the stored links with short links
        iterator = 0
        while iterator < len(links):
            self.linksAndShortlinks[allLinks.link] = allLinks.shortLink
            if iterator != (len(links))-1:
                allLinks = allLinks.get_next_by_date()
            iterator+=1
        print(self.linksAndShortlinks)
        return render(request,self.template_name,{'form':form,'links':links})

    def post(self,request, *args, **kwargs):
        form = LinkForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['link']
        links = LinkModel.objects.all().order_by('-date')

        if not text in self.linksAndShortlinks:
            dbobj = LinkModel()
            dbobj.link = text
            self.no = self.gen.generateShortLink()
            dbobj.shortLink = str(self.no)
            dbobj.save()
            context = {'text':text,'no':self.no}
        else:
            context = {'text':text,'no':self.linksAndShortlinks[text]}

        return render(request,self.output,context=context)


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