from django.contrib import admin

# Register your models here.
from.models import *

admin.site.register(AccountHeads)
admin.site.register(AccountType)
admin.site.register(AccountName)
admin.site.register(JournalLog)
admin.site.register(JournalLogDetails)
