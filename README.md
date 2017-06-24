# django-countable-field
A simple django form field widget for a text field with a current word count.

## Installation and usage
1. Add "countable_field" to your INSTALLED_APPS setting like this:
```
    INSTALLED_APPS = [
        ...
        'countable_field',
    ]
```
2. In the form, set the field's widget to be "CountableWidget", passing
the minimum and maximum word count as additional parameters, such as:
```
    self.fields['essay_response'].widget = \
                CountableWidget(attrs={'text_count_min': this.essay_min_length,
                                       'text_count_max': this.essay_max_length})
```
The additional parameters are optional.

## Credit
This project makes use of the Countable.js library courtesy of Sacha Schmid. https://sacha.me/Countable/
