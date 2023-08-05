#Welcome to the LeafPy framework.
==================================

Useage
-------
- LeafPy-admin.py <project name (in English)> <project creation path (not required)>. 
- Example:"LeafPy-admin.py testweb" is to create a testweb project in the current directory.


Recent Changes
===============

Version 1.0.8 - 2019/12/19
===========================
Fix bug when session store is set to none

Version 1.0.7 - 2019/12/19
===========================
- Fix the bug that the deployment path does not take effect
- Fix the bug that the default template cannot be cached normally

Version 1.0.6 - 2019/12/18
===========================
- Fix a can't render to template bug for default Template
- Fix DiskStore Session Permission denied bug

Version 1.0.2 - 2019/12/18
===========================
- Fix lost LeafPy-admin.py Script on setup
- Add some Example to demo project

Version 1.0.1 - 2019/12/17
===========================
- Support >= Python2.7
- Add redis session support.
- Add jinja2, mako, genshi Templater Support
- Optimize Database operations, support Transaction
- Fix some bugs

Version 1.0.0 - 2016
===========================
Because of learning python, I like python, but I haven't found a suitable python web framework for myself, so I refer to some of my favorite features of commonly used frameworks on the Internet, and wrote the first rough LeafPy framework.