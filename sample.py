# -*- coding: utf-8 -*-
import json
import os

# all django-related code below this line
import cPickle

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vk_lang_model.settings")
from ui.models import Person, PersonLangModel, Conversation


p = Person()
p.firstName = "alexander"
p.lastName = "gin"
p.vk_id = "13"
other_information = {"nick": "PubGin"}
p.otherInformation = json.dumps(other_information, ensure_ascii=False).encode('utf8')
p.save()


p2 = Person()
p2.firstName = "alexander"
p2.lastName = "gin2"
p2.vk_id = "133"
other_information = {"nick": "PubGin2"}
p2.otherInformation = json.dumps(other_information, ensure_ascii=False).encode('utf8')
p2.save()


class LangModel():
    def __init__(self):
        self.a = "a"
        self.b = set()
        self.c = dict()


lm = LangModel()

plm = PersonLangModel()
plm.person = p
plm.data = cPickle.dumps(lm).encode("zip").encode("base64")
plm.save()


conv = Conversation()
conv.first = p
conv.second = p2
#maybe some class for conv data representation
conv.data = "dsfdfsddf".encode('zip').encode("base64")
conv.save()