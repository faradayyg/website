from django.views import generic

from core.models import Post

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = "templates/index.html"


class AboutView(generic.TemplateView):
    template_name = "templates/about.html"


class PostListView(generic.ListView):
    model = Post
    template_name = "templates/post_list.html"
    context_object_name = "posts"
    ordering = ["-created_at"]
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "templates/post_detail.html"
    context_object_name = "post"
