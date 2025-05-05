# File Purpose: This file defines the URL routes or endpoints specific to the reviews APP.
#               These routes map incoming API requests to the related VIEWS defined in reviews/views.py
#               This is how Django knows how to behave when a user visits /api/reviews/


# 1. Imports
from django.urls import path
from .views import ReviewListCreateView, ReviewRetrieveUpdateDestroyView


# 2. URL Patterns
urlpatterns = [
    path('', ReviewListCreateView.as_view(), name='review_list_create'),
    path('<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='review_detail'),
]

#---------------- NOTES BELOW ---------------#

# '' is the ROOTPATH. This handles GET/POST requests to /api/reviews/
# - GET = list all reviews
# - POST = create a new review

# <int:pk> = integer (datatype) and PRIMARY KEY = the DETAILPATH
# - This handles GET/PUT/PATCH/DELETE for a specific review by its ID

# EXAMPLE: if user hits /api/reviews/9/
# - Django matches <int:pk> with 9
# - Passes pk=9 into the view
# - The view runs Review.objects.get(pk=9) and returns that specific review object

# This dynamic path structure allows us to manage each review directly by its database ID

# We can use other converters too — for example:
# - <str:username> for user profile routes like /users/alex/
# - <slug:slug> for cleaner URLs like /reviews/greatest-book-ever/
