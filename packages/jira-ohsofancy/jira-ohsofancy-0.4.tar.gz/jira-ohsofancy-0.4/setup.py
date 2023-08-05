# -*- coding: utf-8 -*-
# Author: Chmouel Boudjnah <chmouel@chmouel.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from distutils.core import setup

setup(
    name='jira-ohsofancy',
    version='0.4',
    description='Jira getting a facelift via the command line',
    long_description_content_type='text/markdown',
    long_description="See homepage on "
    "https://github.com/chmouel/jira-ohsofancy "
    "for a longer description",
    author='Chmouel Boudjnah',
    author_email='chmouel@chmouel.com',
    url='https://github.com/chmouel/jira-ohsofancy',
    install_requires=['iterfzf>=0.4.0', 'jira>=2.0.0'],
    packages=["jiraohsofancy"],
    license="Apache 2.0",
    classifiers=[
        'License :: OSI Approved :: Python Software Foundation License'
    ],
    entry_points={
        'console_scripts': [
            'jira-new-issue = jiraohsofancy.cli:newissue',
        ],
    })
