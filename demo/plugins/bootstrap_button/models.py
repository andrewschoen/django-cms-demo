from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin, Page
from cms.models.fields import PageField

BUTTON_TYPES = (
    ("btn", "Default"),
    ("btn btn-primary", "Primary"),
    ("btn btn-info", "Info"),
    ("btn btn-success", "Success"),
    ("btn btn-warning", "Warning"),
    ("btn btn-danger", "Danger"),
    ("btn btn-inverse", "Inverse"),
)

BUTTON_SIZES = (
    (" ", "Default"),
    ("btn-large", "Large"),
    ("btn-small", "Small"),
    ("btn-mini", "Mini"),
)

class BootstrapButtonPlugin(CMSPlugin):
    label = models.CharField(_('label'), max_length=255)
    url = models.CharField(_("link"), blank=True, null=True, max_length=255)
    page_link = PageField(verbose_name=_("page"), blank=True, null=True,
             help_text=_("A link to a page has priority over a text link."))
    mailto = models.EmailField(_("mailto"), blank=True, null=True,
             help_text=_("An email adress has priority over a text link."))
    button_type = models.CharField(_("button type"), max_length=255,
                choices=BUTTON_TYPES, default="btn")
    button_size = models.CharField(_("button size"), max_length=255,
                choices=BUTTON_SIZES, default=" ")
    new_window = models.BooleanField(_("new window?"), default=False,
                help_text=_("Do you want this button to open a new window?"))

    def __unicode__(self):
        return u'%s' % self.label

