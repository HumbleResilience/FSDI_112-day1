from django.views.generic import TemplateView

#this is OOP -> class is just a blueprint, Object is the house



class HomePageView(TemplateView): #inheriting code from TemplateView
    template_name = "index.html"

#create about class
class AboutPageView(TemplateView): #inheriting code from TemplateView
    template_name = "about.html"

class TestPageView(TemplateView):
    template_name = "test.html"