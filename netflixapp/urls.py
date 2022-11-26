from django.urls import path
from .views import Home,ProfileList, CreateProfile, MovieList, MovieDetail, PlayMovie

app_name = "netflixapp"

urlpatterns = [
    path("",Home.as_view(), name = "Home"),
    path("profiles/",ProfileList.as_view(), name = "profile-list"),
    path("profiles/create",CreateProfile.as_view(),name = "createprofile"),
    path("watch/<str:profile_id>",MovieList.as_view(),name = "movielist"),
    path("watch/detail/<str:movie_id>",MovieDetail.as_view(),name = "moviedetail"),
    path("watch/play/<str:movie_id>",PlayMovie.as_view(),name = "playmovie"),
]