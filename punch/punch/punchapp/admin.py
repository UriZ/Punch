from models import Punchcollection
from models import Punch,User
from django.contrib import admin


admin.site.register(Punchcollection)
admin.site.register(Punch)
admin.site.register(User)

search_fields=['title']