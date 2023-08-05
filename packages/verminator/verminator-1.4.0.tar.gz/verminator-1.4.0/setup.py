# Copyright (c) 2018-2019 `Transwarp, Inc. <http://www.transwarp.io>`_.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the Transwarp, Inc nor the names of its contributors
#       may be used to endorse or promote products derived from this software
#       without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
# TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
import os

from setuptools import setup, find_packages

__version__ = '1.4.0'


def walk_path_files(directory, target_folder=None):
    res = {}
    for subdir, dir, files in os.walk(directory):
        if target_folder is not None:
            target = os.path.join(target_folder, subdir)
        else:
            target = subdir
        if target not in res:
            res[target] = []
        for fname in files:
            res[target].append(os.path.join(subdir, fname))
    return res


data_files = []

requirements = open(os.path.join(os.path.dirname(__file__), 'requirements.txt')).readlines()
install_requires = [i.strip('\r\n ') for i in requirements]

setup(
    name='verminator',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    data_files=data_files,
    url='http://github.com/WarpCloud/verminator',
    license='Transwarp',
    author='Xiaming Chen',
    author_email='xiaming.chen@transwarp.io',
    description='TDC image Version management tERMINATOR.',
    install_requires=install_requires,
    scripts=[
        'bin/verminator'
    ],
    keywords=['utility', 'versioning'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
