===============
Countable Field
===============

Countable Field is a simple Django custom for widget for displaying a
text area with the current word count displayed underneath. It can be
set up to display the count in red when the current word count is out
of required minimum or maximum word count for the form field.

Quick start
-----------

1. Add "countable_field" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'countable_field',
    ]

2. In the form, set the field's widget to be "CountableWidget", passing
the minimum and maximum word count as additional parameters, such as::

    self.fields['essay_response'].widget = \
                CountableWidget(attrs={'text_count_min': this.essay_min_length,
                                       'text_count_max': this.essay_max_length})

