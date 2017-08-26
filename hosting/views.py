from django.shortcuts import render

# Create your views here.
def main_content(request) :
    contents = Activity.objects.all();
    pictures = ActivityPicture.objects.all();
    return render(request, 'main/content.html', {'contents' : contents, 'pictures' : pictures})
