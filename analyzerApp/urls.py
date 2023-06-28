from django.urls import path
from analyzerApp.views import (
    LandingPageView,
    AnalyzerView,
    AboutMePageView,
    MyskillsPageView,
    MytoolsPageView,
    ConnectwithmePageView,
    ErrorPageView,
)


urlpatterns = [
    path('', LandingPageView, name='landing_page'),
    path('analyzer', AnalyzerView, name='analyzer'),
    path('about_me/', AboutMePageView, name='aboutme_page'),
    path('my_skills/', MyskillsPageView, name='myskills_page'),
    path('my_tools/', MytoolsPageView, name='mytools_page'),
    path('connect_with_me/', ConnectwithmePageView, name='connectwithme_page'),
    path('error', ErrorPageView, name='error_page'),
]
