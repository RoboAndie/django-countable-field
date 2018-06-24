# django-countable-field
A simple django form field widget for a text field with a current word count. It can alternatively be configured
to display the character, paragraph, or sentence count.
<img src="https://raw.githubusercontent.com/roboandie/django-countable-field/master/example.gif"/>

## Installation and usage
1. Install with pip
```
pip install django-countable-field
```
2. Add "countable_field" to your INSTALLED_APPS setting like this:
```
    INSTALLED_APPS = [
        ...
        'countable_field',
    ]
```
3. In the form, set the field's widget to be "CountableWidget", passing
the count type, minimum and maximum word count as additional parameters, such as:
```
    self.fields['essay_response'].widget = \
                CountableWidget(attrs={'data-count': 'words',
                                       'data-min-count': this.essay_min_length,
                                       'data-max-count': this.essay_max_length})
```
The additional parameters are optional. `data-min-count` and `data-max-count` must be integers. 
`data-count` indicates what kind of text to count, and can be one of the following: `'words'` (default),
`'characters'`, `'paragraphs'`, or `'sentences'`.

To run the example project, run the server using the settings file in the example_project module.
```
python manage.py runserver --settings=example_project.settings
```

## Credit
This project makes use of the Countable.js library courtesy of Sacha Schmid. https://sacha.me/Countable/
