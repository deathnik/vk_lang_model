from django.contrib import admin

# Register your models here.
from ui.models import PersonLangModel, GroupConversationMapping, GroupConversation, Conversation, Person

admin.site.register(Person)
admin.site.register(Conversation)
admin.site.register(GroupConversation)
admin.site.register(GroupConversationMapping)
admin.site.register(PersonLangModel)