""".git/"""
from django.shortcuts import render, get_object_or_404
from home.models import Cover
from .models import Lesson, Subscription


def lessons_details(request):
    """ A view to show the lessons page """
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='lessons')
    piano_lessons = Lesson.objects.filter(type=1)
    piano_lesson_image = get_object_or_404(piano_lessons,
                                           image_description='A young girl playing the piano')
    singing_lessons = Lesson.objects.filter(type=2)
    singing_lesson_image = get_object_or_404(singing_lessons,
                                             image_description='A young boy'
                                                               ' singing into a microphone')
    song_lessons = Lesson.objects.filter(type=3)
    song_lesson_image = get_object_or_404(song_lessons,
                                          image_description='A woman playing the piano and singing')
    subscriptions = Subscription.objects.all()
    subscription_thirty = get_object_or_404(subscriptions, name='Weekly Payment - 30 minute lesson')
    subscription_forty_five = get_object_or_404(subscriptions, name='Weekly Payment - 45 minute lesson')
    context = { 'covers': covers,
                'cover': cover,
                'piano_lessons': piano_lessons,
                'piano_lesson_image': piano_lesson_image,
                'singing_lessons': singing_lessons,
                'singing_lesson_image': singing_lesson_image,
                'song_lessons': song_lessons,
                'song_lesson_image': song_lesson_image,
                'subscription_thirty': subscription_thirty,
                'subscription_forty_five': subscription_forty_five}

    return render(request, 'lessons/lessons.html', context)


def subscriptions_details(request):
    """ A view to show the lessons page """
    covers = Cover.objects.all()
    cover = get_object_or_404(covers, page='subscriptions')
    context = { 'covers': covers,
                'cover': cover}

    return render(request, 'lessons/subscriptions.html', context)