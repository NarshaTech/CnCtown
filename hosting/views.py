from django.shortcuts import render
from . import models

# Create your views here.
def main_content(request) :
    contents = Activity.objects.all();
    pictures = ActivityPicture.objects.all();
    return render(request, 'hosting/content.html', {'contents' : contents, 'pictures' : pictures})

def detail(request, pk) :
    activity = get_object_or_404(Activity, pk=pk)
    picture = ActivityPicture.objects.filter(activityIndex=pk)
    schedule = ActivitySchedule.objects.filter(activityIndex=pk)
    hash_tag = HashTag.objects.filter(activityIndex=pk)
    review = ActivityReview.objects.filter(activityIndex=pk)
    host = get_object_or_404(Host, user_id = activity.user_id)
    context = { "detail" : activity, "picture" : picture, "hashtags" : hash_tag, "reviews" : review, "host" : host, "schedules" : schedule}
    return render(request, 'hosting/activity_detail.html', context)
