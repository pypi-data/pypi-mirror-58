NewPyFile
------------

Create one[or more] python files from your CLI.

Installation
************

>>> pip install newpyfile

Documentation
*************

>>> newpyfile file [file1...]
"""
Creates file.py in the current directory.
"""

>>> newpyfile file --path=path
"""
Creates file.py in the given as path directory.
"""

>>> newpyfile file --imports=a:b:c,d,e
"""
Creates a file in the current directory, importing from package a, subpackages c & d, and
importing packages d & e
"""

>>> newpyfile file --path=path --imports=a:b:c,d,e
"""
Creates a file in the given as path directory, importing from package a, subpackages c & d, and importing packages d & e
"""

Example
*******

>>> newpyfile file1 file2 --imports=datetime:datetime

Your folder now should contain file1.py & file2.py and each file
will have ``from datetime import datetime``


LICENSE
*******

``MIT License``