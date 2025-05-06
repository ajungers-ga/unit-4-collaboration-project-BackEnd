# File Purpose: This file defines the congfig for the REVIEWS APP. 
#               Djano uses it to recognize and init the APP correctly when the project runs.

from django.apps import AppConfig # imporing DJANGOS built AppConfig system, handling the app settings


class ReviewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' # bigautofield is helpful for larger DB's
    name = 'reviews'


# ReviewsConfig is the app config CLASS. DJANGO looks for this when the app starts up
# line 8 = setting the defaulttype for PRIMARY KEYS on the new models to BigAutoField
# name = 'reviews' registers the app name which must match the FOLDER NAME. in this case: 'reviews'
