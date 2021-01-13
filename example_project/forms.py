from django import forms

from crispy_forms.helper import FormHelper

from countable_field.widgets import CountableTextarea, CountableTextInput


class CountableTestForm(forms.Form):
    char_count_field = forms.CharField(label="Character count")
    word_count_field = forms.CharField(label="Word count")
    paragraph_count_field = forms.CharField(label="Paragraph count")
    sentence_count_field = forms.CharField(label="Sentence count")
    char_count_text_input_field = forms.CharField(label="Character count (text input)")

    def __init__(self, *args, **kwargs):
        super(CountableTestForm, self).__init__(*args, **kwargs)
        self.fields['char_count_field'].widget = CountableTextarea(attrs={'data-max-count': 160,
                                                                        'data-count': 'characters',
                                                                        'data-count-direction': 'down'})
        self.fields['char_count_field'].help_text = "Type up to 160 characters"
        self.fields['word_count_field'].widget = CountableTextarea(attrs={'data-min-count': 100,
                                                                        'data-max-count': 200})
        self.fields['word_count_field'].help_text = "Must be between 100 and 200 words"
        self.fields['paragraph_count_field'].widget = CountableTextarea(attrs={'data-min-count': 2,
                                                                             'data-count': 'paragraphs'})
        self.fields['paragraph_count_field'].help_text = "Must be at least 2 paragraphs"
        self.fields['sentence_count_field'].widget = CountableTextarea(attrs={'data-count': 'sentences'})

        self.fields['char_count_text_input_field'].widget = CountableTextInput(attrs={'data-max-count': 160,
                                                                          'data-count': 'characters',
                                                                          'data-count-direction': 'down'})
        self.fields['char_count_text_input_field'].help_text = "Type up to 160 characters"

        self.helper = FormHelper()
        self.helper.wrapper_class = 'row'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.help_text_inline = False
