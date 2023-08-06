# -*- coding: UTF-8 -*-
# Copyright 2016-2017 Luc Saffre
# License: BSD (see file COPYING for details)

from __future__ import unicode_literals

from lino.api import rt, _
from lino.utils.cycler import Cycler
from lino.utils.instantiator import create_row
from lino_xl.lib.tickets.choicelists import TicketStates

from lino.api.dd import str2kw
from lino.api import dd

TICKET_STATES = Cycler(TicketStates.objects())

from lino.modlib.users.utils import create_user

def skill(name, fr, en, **kw):
    kw.update(**dd.babelkw('name', de=name, fr=fr, en=en))
    # kw.update(name=name, name_fr=name_fr, name_en=name_en)
    return rt.models.skills.Skill(**kw)


# def S(name, **kw):
#     kw.update(name=name)
#     # return rt.models.tickets.Site(**kw)
#     return dd.plugins.tickets.site_model(**kw)


def Topic(name, **kw):
    kw.update(**str2kw('name', name))
    return rt.models.topics.Topic(**kw)


# def ticket(username, summary, en, skill=None, **kw):
#     ar = rt.login(username)
#     u = ar.get_user() # rt.models.users.User.objects.get(username=user)
#     if en and u.language != 'de':
#         summary = en
#     kw.update(summary=summary, user=u)
#     # if no manual state is specified, take a random one:
#     if not 'state' in kw:
#         kw.update(state=TICKET_STATES.pop())
#     t = create_row(rt.models.tickets.Ticket, **kw)
#     t.after_ui_create(ar)  # create author's vote
#     yield t
#     if skill is not None:
#         yield rt.models.skills.Demand(demander=t, skill=skill)


# def competence(username, first_name, skill, **kw):
#     Person = rt.models.contacts.Person
#     kw.update(
#         end_user=Person.objects.get(
#             name=first_name))
#     kw.update(skill=skill)
#     kw.update(user=rt.models.users.User.objects.get(username=username))
#     return rt.models.skills.Competence(**kw)


# def vote(user, ticket, state, **kw):
#     u = rt.models.users.User.objects.get(username=user)
#     t = rt.models.tickets.Ticket.objects.get(pk=ticket)
#     s = rt.models.votes.VoteStates.get_by_name(state)
#     return rt.models.votes.Vote(user=u, votable=t, state=s, **kw)



def objects():
    # UserTypes = rt.models.users.UserTypes
    # yield create_user("alex", UserTypes.user)
    # yield create_user("berta", UserTypes.user)
    # yield create_user("christa", UserTypes.user)
    # yield create_user("dora")
    # yield create_user("eric", UserTypes.staff)

    # prj = rt.models.tickets.Project(name=_("General"))
    # yield prj
    # for u in rt.models.users.User.objects.all():
    #     yield rt.models.tickets.Competence(project=prj, user=u)

    # yield S(_("At home"))  # "Bei mir zu Hause"
    # yield S("AZ Ephata")
    # yield S("Eupen")

    # TopicGroup = rt.models.topics.TopicGroup
    # lng = TopicGroup(**str2kw('name', _("Languages")))
    # yield lng
    # fr = Topic(_("French"), topic_group=lng)
    # yield fr
    # de = Topic(_("German"), topic_group=lng)
    # yield de
    # yield Topic(_("English"), topic_group=lng)

    # music = TopicGroup(**str2kw('name', _("Music")))
    # yield music
    # piano = Topic(_("Piano"), topic_group=music)
    # yield piano
    # guitar = Topic(_("Guitar"), topic_group=music)
    # yield guitar

    edu = skill("Unterricht", "Cours", "Teaching")
    yield edu
    yield skill(
        "Französischunterricht", "Cours de francais", "French lessons",
        parent=edu)
    yield skill("Deutschunterricht", "Cours d'allemand",
                  "German lessons", parent=edu)
    math = skill(
        "Matheunterricht", "Cours de maths", "Maths lessons",
        parent=edu)
    yield math
    
    music = skill("Musik", "Musique", "Music")
    yield music
    guitar = skill(
        "Gitarrenunterricht",
        "Cours de guitare", "Guitar lessons", parent=music)
    yield guitar
    piano = skill(
        "Klavierunterricht",
        "Cours de piano", "Piano lessons", parent=music)
    yield piano

    home = skill(
        "Haus und Garten", "Maison et jardin", "Home & Garden")
    yield home

    yield skill(
        "Kleider reparieren", "Réparer des vètements",
        "Repairing clothes", parent=home)
    garden = skill(
        "Gartenarbeiten", "Travaux de jardin", "Garden works",
        parent=home)
    yield garden
    repair = skill(
        "Reparaturarbeiten", "Travaux de réparation", "Repair works",
        parent=home)
    yield repair
    renovate = skill(
        "Renovierung", "Rénovation", "Renovation",
        parent=home)
    yield renovate

    yield skill("Fahrdienst", "Voiture", "Car driving")
    commissions = skill("Botengänge", "Commissions", "Shopping")
    yield commissions
    yield skill("Friseur", "Coiffure", "Hair cutting")
    yield skill("Babysitting", "Garde enfant", "Babysitting")
    yield skill("Gesellschafter für Senioren",
                  "Rencontres personnes agées",
                  "Mentoring elderly people")
    yield skill(
        "Hunde spazierenführen", "Chiens", "Go out with dogs")
    traduire = skill(
        "Übersetzungsarbeiten",
        "Traductions", "Translations")
    yield traduire
    yield skill("Briefe schreiben", "Écrire des lettres",
                  "Write letters")

    # Person = rt.models.contacts.Person
    # kw.update(
    #     end_user=Person.objects.get(
    #         name=first_name))
    # kw.update(skill=skill)
    # kw.update(user=rt.models.users.User.objects.get(username=username))
    # return rt.models.skills.Competence(**kw)

    # yield competence('alex', 'Alex', traduire)
    # yield competence('berta', 'Berta', traduire)
    # # yield competence('berta', traduire, topic=de)
    # yield competence('alex', 'Alex', garden)
    # yield competence('alex', 'Alex', repair)
    # yield competence('christa', 'Christa', piano)
    # yield competence('eric', 'Dora', repair)
    # yield competence('eric', 'Eric', guitar)
    # yield competence('eric', 'Dora', commissions)


    # yield ticket(  #1
    #     "berta",
    #     "Mein Wasserhahn tropft, wer kann mir helfen?",
    #     "My faucet is dripping, who can help?",
    #     state=TicketStates.closed,
    #     skill=repair)
    # yield vote('alex', 1, 'done')
    # yield vote('eric', 1, 'cancelled')
    
    # yield ticket(  #2
    #     "christa",
    #     "Mein Rasen muss gemäht werden. Donnerstags oder Samstags",
    #     "My lawn needs mowing. On Thursday or Saturday."
    #     "", skill=garden)
    # Person = rt.models.contacts.Person
    # # dora = dd.plugins.skills.end_user_model.objects.get(
    # dora = Person.objects.get(first_name="Dora")
    # yield ticket(  #3
    #     "eric",
    #     "Wer kann meinem Sohn Klavierunterricht geben?",
    #     "Who can give piano lessons to my son?",
    #     skill=piano, end_user=dora)
    
    # yield vote('christa', 3, 'candidate')
    
    # yield ticket(  #4
    #     "alex",
    #     "Wer kann meiner Tochter Gitarreunterricht geben?",
    #     "Who can give guitar lessons to my daughter?",
    #     skill=guitar)
    
    # yield ticket(  #5
    #     "alex",
    #     "Wer macht Musik auf meinem Geburtstag?",
    #     "Who would play music on my birthday party?",
    #     deadline=dd.demo_date(-20),
    #     state=TicketStates.opened,
    #     skill=music)
    # yield vote('christa', 5, 'candidate')
    # yield vote('eric', 5, 'candidate')
    
    # yield ticket(
    #     "berta",
    #     "Wer hilft meinem Sohn sich auf die Mathearbeit am "
    #     "21.05. vorzubereiten? 5. Schuljahr PDS.",
    #     "Who helps my sont to prepare for a maths test on May 21?"
    #     " (5. grade PDS)",
    #     deadline=dd.demo_date().replace(month=5, day=21),
    #     skill=math)
    # yield ticket(
    #     "eric",
    #     "Wer kann meine Abschlussarbeit korrekturlesen?",
    #     "Who can review my final work?",
    #     end_user=dora, 
    #     deadline=dd.demo_date().replace(month=3, day=12),
    #     description="Für 5. Jahr RSI zum Thema \"Das "
    #     "Liebesleben der Kängurus\"  "
    #     "Muss am 12.03. eingereicht werden.")
    # yield ticket(  #8
    #     "alex",
    #     "Wer fährt für mich nach Aachen Windeln kaufen?",
    #     "Who would buy diapers for me in Aachen?",
    #     description="Ich darf selber nicht über die Grenze.",
    #     skill=commissions)

    # yield vote('eric', 8, 'assigned')
