"""A simple XBlock for displaying content in coloured boxes"""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, String
from xblock.fragment import Fragment
from xblockutils.studio_editable import StudioEditableXBlockMixin

class PrismXBlock(StudioEditableXBlockMixin, XBlock):
    display_name = String(display_name="Display name", default='Code', scope=Scope.settings)	
    language = String(display_name="Code language", values=('bash', 'shell', 'shell-session', 'docker', 'docker-file', 'json','regex','yaml','yml','properties','sql','nginx','apacheconf','html','xml'),
        default="bash", scope=Scope.settings,
        help="Choose a language code")
    content = String(display_name="Contents", multiline_editor='html', resettable_editor=False,
        default="", scope=Scope.content,
        help="Enter content code to be displayed")

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        """
        The primary view of the PrismXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/prism.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/prism.css"))
        frag.add_javascript(self.resource_string("static/js/src/prism.js"))
        frag.initialize_js('Prism')
        return frag
    # Make fields editable in studio
    editable_fields = ('display_name', 'language', 'content')
