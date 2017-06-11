
from django.forms import widgets
from django.utils.safestring import mark_safe


class TextCountWidget(widgets.Textarea):
    class Media:
        js = (
            'text_count_field/js/countable.js',
        )

    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs, name=name)
        js = """
        <script type="text/javascript">
            var textarea = document.getElementById('%(id)s');
            var countDisplay = document.getElementById('%(id)s_counter');
            var minCount = %(minCount)s;
            var maxCount = %(maxCount)s;
            if (textarea != null && countDisplay != null) {
                Countable.live(textarea, function (counter) {
                    countDisplay.getElementsByClassName("text-count-current")[0].innerHTML = counter.words;
                    if (minCount && counter.words < minCount)
                        countDisplay.className = "text-count text-is-under-min";
                    else if (maxCount && counter.words > maxCount)
                        countDisplay.className = "text-count text-is-over-max";
                    else
                        countDisplay.className = "text-count";
                })
            }
        </script>
        """
        js = js % {'id': final_attrs.get('id'),
                   'minCount': final_attrs.get('text_count_min') or 'false',
                   'maxCount': final_attrs.get('text_count_max') or 'false'}
        output = super(TextCountWidget, self).render(name, value, final_attrs)
        output += self.get_word_count_template(final_attrs.get('id'))
        output += js
        return mark_safe(output)

    @staticmethod
    def get_word_count_template(related_id):
        return """<span class="text-count" id="%(id)s_counter">Word count:
                  <span class="text-count-current">0</span></span>""" % {'id': related_id}

