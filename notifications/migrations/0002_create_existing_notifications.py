# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-06 11:49
from __future__ import unicode_literals

from django.db import migrations


NOTIFICATION_TYPES = (
    'reservation_requested',
    'reservation_requested_official',
    'reservation_cancelled',
    'reservation_confirmed',
    'reservation_denied',
    'reservation_created_with_access_code',
)

BODY_HEADER_EN = 'Hello,\n'
BODY_FOOTER_EN = 'Best regards,\nVaraamo\n'

BODY_HEADER_FI = 'Hei,\n'
BODY_FOOTER_FI = 'Ystävällisin terveisin,\nVaraamo\n'


RESERVATION_REQUESTED_SUBJECT_EN = "You've made a preliminary reservation"
RESERVATION_REQUESTED_BODY_EN = """
and thanks for using Varaamo!

You've made a preliminary reservation:

Resource: {{ resource }}
Unit: {{ unit }}
Starts: {{ begin }}
Ends: {{ end }}

Your reservation will be processed in two days and you will get an
email when your reservation is either confirmed or denied. In case we
need more information regarding the reservation, we will be in contact
with you.

This is an automated message, please don't reply to this.

"""

RESERVATION_REQUESTED_SUBJECT_FI = 'Olet tehnyt alustavan varauksen'
RESERVATION_REQUESTED_BODY_FI = """
ja kiitokset Varaamon käytöstä!

Olet tehnyt alustavan varauksen:

Tila: {{ resource }}
Toimipiste: {{ unit }}
Alkaa: {{ begin }}
Loppuu: {{ end }}

Varaus käsitellään kahden päivän kuluessa. Varauksen hyväksymisestä
saatte erillisen varausvahvistuksen sähköpostitse. Mikäli tarvitsemme
lisätietoja varaukseen liittyen, olemme teihin yhteydessä erikseen.

Tämä on automaattinen viesti, joten älä vastaa tähän.

"""

RESERVATION_REQUESTED_OFFICIAL_SUBJECT_EN = 'Reservation requested'
RESERVATION_REQUESTED_OFFICIAL_BODY_EN = """
A new preliminary reservation has been made:

Resource: {{ resource }}
Unit: {{ unit }}
Starts: {{ begin }}
Ends: {{ end }}

Process the reservation within two days.
"""

RESERVATION_REQUESTED_OFFICIAL_SUBJECT_FI = 'Alustava varaus tehty'
RESERVATION_REQUESTED_OFFICIAL_BODY_FI = """
Uusi alustava varaus on tehty:

Tila: {{ resource }}
Toimipiste: {{ unit }}
Alkaa: {{ begin }}
Loppuu: {{ end }}

Käsittele varaus kahden päivän sisällä.

"""

RESERVATION_CANCELLED_SUBJECT_EN = 'Reservation cancelled'
RESERVATION_CANCELLED_BODY_EN = """
Your reservation has been cancelled.

Resource: {{ resource }}
Unit: {{ unit }}
Starts: {{ begin }}
Ends: {{ end }}

Further information regarding the cancellation of your reservation can
be acquired from the personnel who are responsible for the space.

"""

RESERVATION_CANCELLED_SUBJECT_FI = 'Varaus peruttu'
RESERVATION_CANCELLED_BODY_FI = """
Varauksesi on peruttu.

Tila: {{ resource }}
Toimipiste: {{ unit }}
Alkaa: {{ begin }}
Loppuu: {{ end }}

Varauksen perumiseen liittyvät syyt voitte tiedustella tilasta vastaavalta
henkilökunnalta.

"""

RESERVATION_CONFIRMED_SUBJECT_EN = 'Reservation confirmed'
RESERVATION_CONFIRMED_BODY_EN = """
Your reservation has been confirmed.

Resource: {{ resource }}
Unit: {{ unit }}
Starts: {{ begin }}
Ends: {{ end }}

It is possible to cancel the reservation five days before the start of
your reservation. All cancellations are done through personnel. Further
information for cancelling your reservation can be found from Varaamo's
"Omat varaukset" section which you can find when you are logged in to the
service.

{% if extra_content is defined %}
{{ extra_content }}
{% endif %}
"""

RESERVATION_CONFIRMED_SUBJECT_FI = 'Varaus vahvistettu'
RESERVATION_CONFIRMED_BODY_FI = """
Varauksesi on hyväksytty.

Tila: {{ resource }}
Toimipiste: {{ unit }}
Alkaa: {{ begin }}
Loppuu: {{ end }}

Varauksen voitte perua viisi päivää ennen varauksen alkua. Varauksen
peruminen tehdään tilasta vastaavan henkilökunnan kautta. Tarkemmat
tiedot perumiseen löydätte Varaamon omista varauksista kirjautumalla
palveluun.

{% if extra_content is defined %}
{{ extra_content }}
{% endif %}
"""

RESERVATION_DENIED_SUBJECT_EN = 'Reservation denied'
RESERVATION_DENIED_BODY_EN = """
Your reservation request has been denied.

Resource: {{ resource }}
Unit: {{ unit }}
Starts: {{ begin }}
Ends: {{ end }}

Further information regarding the rejection of your reservation can
be acquired from the personnel who are responsible for the space.

"""

RESERVATION_DENIED_SUBJECT_FI = 'Varaus hylätty'
RESERVATION_DENIED_BODY_FI = """
Varauksesi on hylätty.

Tila: {{ resource }}
Toimipiste: {{ unit }}
Alkaa: {{ begin }}
Loppuu: {{ end }}

Varauksen hylkäämiseen liittyvät tarkemmat perusteet voitte
tiedustella tilasta vastaavalta henkilökunnalta.

"""

RESERVATION_CREATED_WITH_ACCESS_CODE_SUBJECT_EN = 'Reservation created'
RESERVATION_CREATED_WITH_ACCESS_CODE_BODY_EN = """
and thanks for using Varaamo!

You've made a new reservation:

Resource: {{ resource }}
Unit: {{ unit }}
Starts: {{ begin }}
Ends: {{ end }}

{% if access_code %}
Your access code for the resource: {{ access_code }}

{% endif %}
"""

RESERVATION_CREATED_WITH_ACCESS_CODE_SUBJECT_FI = 'Varaus tehty'
RESERVATION_CREATED_WITH_ACCESS_CODE_BODY_FI = """
ja kiitokset Varaamon käytöstä!

Olet tehnyt uuden varauksen:

Tila: {{ resource }}
Toimipiste: {{ unit }}
Alkaa: {{ begin }}
Loppuu: {{ end }}

{% if access_code %}
Pääsykoodisi tilaan: {{ access_code }}

{% endif %}
"""


def _append_header_and_footer(text, language):
    header = BODY_HEADER_EN if language == 'en' else BODY_HEADER_FI
    footer = BODY_FOOTER_EN if language == 'en' else BODY_FOOTER_FI
    return '{}{}{}'.format(header, text, footer)


def _get_text(notification_type, language, field):
    var_name = '{}_{}_{}'.format(notification_type, field, language).upper()
    text = globals().get(var_name)
    assert text, '{} undefined'.format(var_name)
    return text


def create_existing_notifications(NotificationTemplate, NotificationTemplateTranslation):
    for notification_type in NOTIFICATION_TYPES:
        notification, created = NotificationTemplate.objects.get_or_create(type=notification_type)
        if created:
            for language in ('fi', 'en'):
                subject = _get_text(notification_type, language, 'subject')
                body = _get_text(notification_type, language, 'body')
                body = _append_header_and_footer(body, language)

                NotificationTemplateTranslation.objects.create(
                    master_id=notification.id,
                    language_code=language,
                    subject=subject,
                    body=body,
                )


def forwards(apps, schema_editor):
    NotificationTemplate = apps.get_model('notifications', 'NotificationTemplate')
    NotificationTemplateTranslation = apps.get_model('notifications', 'NotificationTemplateTranslation')
    create_existing_notifications(NotificationTemplate, NotificationTemplateTranslation)


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards, migrations.RunPython.noop)
    ]
