
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
        output = super(CountableWidget, self).render(name, value, final_attrs)
        output += """<span class="text-count" id="%(id)s_counter" data-min-count="%(min_count)s"
                  data-max-count="%(max_count)s">Word count: <span class="text-count-current">0</span></span>""" \
                  % {'id': final_attrs.get('id'),
                     'min_count': final_attrs.get('text_count_min' or 'false'),
                     'max_count': final_attrs.get('text_count_max' or 'false')}
        js = """
        <script type="text/javascript">
            var countableField = new CountableField("%(id)s")
        </script>
        """ % {'id': final_attrs.get('id')}
        output += js
        return mark_safe(output)

