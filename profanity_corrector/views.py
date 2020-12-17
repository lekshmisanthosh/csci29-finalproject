from django.shortcuts import render, redirect, get_object_or_404
from profanity_corrector.forms import EnterText
from django.utils import timezone
from textblob import TextBlob
from .models import UserResponse

# Create your views here.


def post_detail(request, pk):
    post = get_object_or_404(UserResponse, pk=pk)
    post.test = TextBlob(post.user_response).sentiment.polarity
    return render(request, "detail.html", {"post": post})


def post_new(request):
    if request.method == "POST":
        form = EnterText(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_time = timezone.now()
            post.save()
            # return redirect('enter_new_text')
            return redirect("post_detail", pk=post.pk)

    else:
        form = EnterText()
    return render(request, "add_data.html", {"form": form})
