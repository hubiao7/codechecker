# -------------------------------------------------------------------------
#                     The CodeChecker Infrastructure
#   This file is distributed under the University of Illinois Open Source
#   License. See LICENSE.TXT for details.
# -------------------------------------------------------------------------

import logging

from codechecker_report_converter.analyzer_result import AnalyzerResult

from .output_parser import ESLintParser
from ..plist_converter import PlistConverter


LOG = logging.getLogger('ReportConverter')


class ESLintAnalyzerResult(AnalyzerResult):
    """ Transform analyzer result of the ESLint analyzer. """

    TOOL_NAME = 'eslint'
    NAME = 'ESLint'
    URL = 'https://eslint.org/'

    def parse(self, analyzer_result):
        """ Creates plist objects from the given analyzer result.

        Returns a list of plist objects.
        """
        parser = ESLintParser()
        messages = parser.parse_messages(analyzer_result)
        if not messages:
            return

        plist_converter = PlistConverter(self.TOOL_NAME)
        plist_converter.add_messages(messages)
        return plist_converter.get_plist_results()
