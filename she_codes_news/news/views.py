from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from .models import NewsStory
from .forms import StoryForm
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by("-pub_date")[:4]
        context['all_stories'] = NewsStory.objects.all().order_by("-pub_date")
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'
    
class AddStoryView(generic.CreateView):
    form_class = StoryForm
    # context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class StoryEditView(LoginRequiredMixin, generic.UpdateView):
    model = NewsStory
    fields = ['title', 'pub_date', 'content', 'image']

    def get_success_url(self) -> str:
        return reverse_lazy('news:story', kwargs={'pk':self.kwargs['pk']})

    def get_queryset(self):
        qs = super().get_queryset()
        # if not self.request.user.is_authenticated:
        #     raise qs.model.DoesNotExist
        # qs = qs.filter(author=self.request.user)
        return qs.filter(author=self.request.user)

class StoryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = NewsStory
    success_url = reverse_lazy('news:index')

    def get_queryset(self):
        # filter to only allow to author to delete own story
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)


    ''' when given a pk for a newsstory, add the suer to like, or if exists, remove the user'''
@login_required
def like(request, pk):
    news_story = get_object_or_404(NewsStory, pk=pk)
    if news_story.favourited_by.filter(username=request.user.username).exists():
        news_story.favourited_by.remove(request.user)
    else:
        news_story.favourited_by.add(request.user)
    return redirect(reverse_lazy('news:story', kwargs={'pk':pk}))
