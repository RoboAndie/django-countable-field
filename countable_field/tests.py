from unittest import TestCase
from django.utils.safestring import mark_safe

from countable_field import widgets


HTML_TEMPLATE = (
    '<textarea cols="40" data-max-count="%(max_count)s" data-min-count="%(min_count)s" name="countable" rows="10">\r\n'
    '</textarea>'
    '<span class="text-count" id="None_counter">Word count:'
    '<span class="text-count-current">0</span></span>\r\n'
    '<script type="text/javascript">var countableField = new CountableField("None")</script>\n'
)


class WidgetTestCase(TestCase):

    def setUp(self):
        pass

    def test_no_limits(self):
        widget = widgets.CountableWidget()
        self.assertEqual(
            widget.render('countable', None),
            mark_safe(HTML_TEMPLATE % {'min_count': 'false', 'max_count': 'false'})
        )

    def test_lower_limit(self):
        widget = widgets.CountableWidget()
        self.assertEqual(
            widget.render('countable', None, attrs={'data-min-count': 50}),
            HTML_TEMPLATE % {'id': '', 'min_count': 50, 'max_count': 'false'}
        )

    def test_upper_limit(self):
        widget = widgets.CountableWidget()
        self.assertEqual(
            widget.render('countable', None, attrs={'data-max-count': 70}),
            HTML_TEMPLATE % {'id': '', 'min_count': 'false', 'max_count': 70}
        )

    def test_both_limits(self):
        widget = widgets.CountableWidget()
        self.assertEqual(
            widget.render('countable', None, attrs={'data-min-count': 30, 'data-max-count': 80}),
            HTML_TEMPLATE % {'id': '', 'min_count': 30, 'max_count': 80}
        )

    def test_invalid_limits(self):
        widget = widgets.CountableWidget()
        self.assertEqual(
            widget.render('countable', None, attrs={'data-min-count': 'blue', 'data-max-count': 50.9}),
            HTML_TEMPLATE % {'id': '', 'min_count': 'false', 'max_count': 'false'}
        )
