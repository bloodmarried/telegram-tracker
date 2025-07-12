from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Reviews
from django.views.generic import DetailView
from django.http import Http404
# Create your views here.

def review(request: HttpRequest):
    print(request.user)
    return render(request, "reaction/index.html")


class ProfileDetailView(DetailView):
    model = Reviews
    template_name = "reaction/index.html"
    context_object_name = "profile"
    
    def get(self, request: HttpRequest, *args, **kwargs):
        if request.method == "GET":
            search = request.GET.get("search-input")
            if search:
                if search.isdigit():
                    user = Reviews.objects.filter(user_id = search).first()
                    if user:
                        return redirect("user", search)
                    else:
                        return redirect("user", search)
                return redirect("user", search)
            return super().get(request, *args, **kwargs)
    
    def get_object(self, queryset = None):
        attr = self.kwargs.get("pk", None)
        
        if queryset is None:
            queryset = self.get_queryset()
        try:
            user = Reviews.objects.get(user_id = attr)
            user.viewers += 1
            user.save()
            return queryset.get(user_id = attr)
        
        except Reviews.DoesNotExist:
            raise Http404("No object found with this custom ID.")