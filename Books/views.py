from django.shortcuts import render
from django.http import Http404
from django.views import generic
from django.shortcuts import reverse, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required, permission_required
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin


class BookListView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    model = Book
    template_name = 'Books/ListView.html'
    context_object_name = 'books'

    def test_func(self):
        return Book.objects.filter(user=self.request.user)


class BookDetailView(generic.DetailView, generic.FormView):
    self.request.user.
    model = Book
    form_class = CommentForm
    template_name = 'Books/DetailView.html'

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        context['comment_form'] = CommentForm
        return context

    def post(self, request, *args, **kwargs):
        book = self.get_object()
        form = CommentForm(self.request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            comment.user = self.request.user
            comment.save()
            return redirect(book.get_absolute_url())
        return redirect(book.get_absolute_url())


# @login_required
# def BookDetailView(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     book_comments = book.comments.all()
#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             comment = comment_form.save(commit=False)
#             comment.user = request.user
#             comment.book = book
#             comment.save()
#             comment_form = CommentForm()
#
#     else:
#         comment_form = CommentForm()
#     return render(request, template_name='Books/DetailView.html', context={'book': book, 'comments':book_comments,
#                                                                            'comment_form': comment_form})


class BookCreateView(generic.CreateView):
    model = Book
    template_name = 'Books/Create_And_Update.html'
    fields = '__all__'
    success_url = reverse_lazy('book_list')


class BookUpdateView(UserPassesTestMixin, generic.UpdateView):
    model = Book
    template_name = 'Books/Create_And_Update.html'
    fields = '__all__'

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user
