import os
import pytest
import pytest_html
from py.xml import html
from datetime import datetime
from typing import Dict, Tuple

# Set report name
def pytest_html_report_title(report):
    report.title =  "Automation Report " + datetime.now().strftime("%Y-%m-%d") + "T" + datetime.now().strftime("%H:%M:%S.%f")

# Set report path
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # to remove environment section
    config._metadata = None

    if not os.path.exists('reports'):
        os.makedirs('reports')

    config.option.htmlpath = 'reports/' + "Automation Report " + datetime.now().strftime("%Y%m%d%H%M%S ") + ".html"
'''
# Custom 'Results' table in report.html
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th("Time", class_="sortable time", col="time"))
    cells.pop()

def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(datetime.utcnow(), class_="col-time"))
    cells.pop() 
'''
# set incremental mark
def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item

def pytest_runtest_setup(item):
    previousfailed = getattr(item.parent, "_previousfailed", None)
    if previousfailed is not None:
        pytest.xfail("previous test failed (%s)" % previousfailed.name)