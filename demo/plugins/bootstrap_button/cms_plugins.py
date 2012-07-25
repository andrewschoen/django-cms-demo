from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _
from django.conf import settings

from models import BootstrapButtonPlugin

class BootstrapButtonPlugin(CMSPluginBase):
    model = BootstrapButtonPlugin
    name = _("Button")
    text_enabled = True
    render_template = "plugins/bootstrap_button.html"

    def render(self, context, instance, placeholder):
        if instance.mailto:
            link = u"mailto:%s" % _(instance.mailto)
        elif instance.url:
            link = _(instance.url)
        elif instance.page_link:
            link = instance.page_link.get_absolute_url()
        else:
            link = ""
        context.update({
            'link': link,
            'size': instance.button_size,
            'type': instance.button_type,
            'label': instance.label,
            'new_window': instance.new_window,
        })
        return context

    def icon_src(self, instance):
        return settings.STATIC_URL + u"cms/images/plugins/link.png"


plugin_pool.register_plugin(BootstrapButtonPlugin)