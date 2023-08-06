# -*- coding: UTF-8 -*-
# Copyright 2015-2017 Luc Saffre
# License: BSD (see file COPYING for details)

"""Desktop UI for this plugin.

"""

from lino_xl.lib.online.users.desktop import *

from lino.api import _

from lino.core import actions
# from lino.modlib.office.roles import OfficeUser
from lino_xl.lib.working.roles import Worker

from lino.modlib.users.actions import SendWelcomeMail
from lino.modlib.office.roles import OfficeUser
#from .models import VerifyUser

class UserDetail(UserDetail):
    """Layout of User Detail in Lino Care."""

    main = "general contact dashboard.WidgetsByUser"

    general = dd.Panel("""
    box1:45 working:15
    skills.OffersByEndUser
    """, label=_("General"))

    if dd.is_installed('working'):
        working = dd.Panel("""
        open_session_on_new_ticket
        timezone
        """, label=_("Clocking"), required_roles=dd.login_required(Worker))
    else:
        working = dd.DummyPanel()

    # calendar = dd.Panel("""
    # event_type access_class
    # cal.SubscriptionsByUser
    # # cal.MembershipsByUser
    # """, label=dd.plugins.cal.verbose_name, required_roles=dd.login_required(OfficeUser))


    box1 = """
    username user_type:20 initials #partner #user_site
    language id created modified
    callme_mode mail_mode notify_myself
    """

    # cal_left = """
    # event_type access_class
    # cal.SubscriptionsByUser
    # """

    # cal = dd.Panel("""
    # cal_left:30 cal.TasksByUser:60
    # """, label=dd.plugins.cal.verbose_name,
    #                required_roles=dd.login_required(OfficeUser))

    contact = dd.Panel("""
    address_box info_box
    remarks:40 users.AuthoritiesGiven:20
    """, label=_("Contact"))

    info_box = """
    email:40
    # url
    phone
    gsm
    """
    address_box = """
    first_name last_name #initials
    country region city zip_code:10
    #addr1
    #street_prefix street:25 street_no #street_box
    # addr2
    """


Users.detail_layout = UserDetail()
