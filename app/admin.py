from django.contrib import admin

from .models import User, Data, Attendence, Github

admin.site.register(User)
admin.site.register(Data)
admin.site.register(Attendence)
admin.site.register(Github)

