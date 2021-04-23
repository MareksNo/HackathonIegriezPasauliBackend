from django.contrib import admin
from core.models import Question, Option, Member

admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Member)
