# from django.db import transaction
# from djstripe import webhooks

#def do_something():
    #pass  # send a mail, invalidate a cache, fire off a Celery task, etc.

@webhooks.handler("price", "product", "customer")
def my_handler(event, **kwargs):
    print("We should probably notify the user at this point")
