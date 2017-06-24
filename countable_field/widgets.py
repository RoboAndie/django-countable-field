
from django.forms import widgets
from django.utils.safestring import mark_safe


class CountableWidget(widgets.Textarea):
    class Media:
        js = ('countable_field/js/scripts.js',)
        css = {
            'all':
                ('countable_field/css/styles.css',)
        }

    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs)
        # to avoid xss, if the min or max attributes are not integers, set them to 'false'
        if not isinstance(final_attrs.get('data-min-count'), int):
            final_attrs['data-min-count'] = 'false'
        if not isinstance(final_attrs.get('data-max-count'), int):
            final_attrs['data-max-count'] = 'false'
        output = super(CountableWidget, self).render(name, value, final_attrs)
        output += self.get_word_count_template(final_attrs)
        return mark_safe(output)

    @staticmethod
    def get_word_count_template(attrs):
        return (
                 '<span class="text-count" id="%(id)s_counter">Word count: '
                 '<span class="text-count-current">0</span></span>\r\n'
                 '<script type="text/javascript">var countableField = new CountableField("%(id)s")</script>\n'
               ) % {'id': attrs.get('id')}


