from django import VERSION
from django.forms import widgets
from django.utils.safestring import mark_safe


class CountableWidget(widgets.Textarea):
    class Media:
        js = ('countable_field/js/scripts.js',)
        css = {
            'all':
                ('countable_field/css/styles.css',)
        }

    def render(self, name, value, attrs=None, **kwargs):
        # the build_attrs signature changed in django version 1.11
        if VERSION[:2] >= (1, 11):
            final_attrs = self.build_attrs(self.attrs, attrs)
        else:
            final_attrs = self.build_attrs(attrs)
        # to avoid xss, if the min or max attributes are not integers, remove them
        if final_attrs.get('data-min-count') and not isinstance(final_attrs.get('data-min-count'), int):
            final_attrs.pop('data-min-count')
        if final_attrs.get('data-max-count') and not isinstance(final_attrs.get('data-max-count'), int):
            final_attrs.pop('data-max-count')
        if not final_attrs.get('data-count') in ['words', 'characters', 'paragraphs', 'sentences']:
            final_attrs['data-count'] = 'words'

        if VERSION[:2] >= (1, 11):
            output = super(CountableWidget, self).render(name, value, final_attrs, **kwargs)
        else:
            output = super(CountableWidget, self).render(name, value, final_attrs)
        output += self.get_word_count_template(final_attrs)
        return mark_safe(output)

    @staticmethod
    def get_word_count_template(attrs):
        count_type = attrs.get('data-count', 'words')
        count_direction = attrs.get('data-count-direction', 'up')
        max_count = attrs.get('data-max-count', '0')

        if count_direction == 'down':
            count_label = "Words remaining: "
            if count_type == "characters":
                count_label = "Characters remaining: "
            elif count_type == "paragraphs":
                count_label = "Paragraphs remaining: "
            elif count_type == "sentences":
                count_label = "Sentences remaining: "
        else:
            count_label = "Word count: "
            if count_type == "characters":
                count_label = "Character count: "
            elif count_type == "paragraphs":
                count_label = "Paragraph count: "
            elif count_type == "sentences":
                count_label = "Sentence count: "
        return (
                 '<span class="text-count" id="%(id)s_counter">%(label)s'
                 '<span class="text-count-current">%(number)s</span></span>\r\n'
               ) % {'label': count_label,
                    'id': attrs.get('id'),
                    'number': max_count if count_direction == 'down' else '0'}


