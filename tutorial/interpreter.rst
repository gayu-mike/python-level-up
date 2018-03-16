.. _The Interpreter and Its Environment

Python解释器
===========

Argument Passing
----------------

.. code-block:: console

    $ python main.py --debug

向Python解释器传参, 参数存放在sys.argv里面, 它是一个list.
比如上面的命令:

.. code-block:: python3

    import sys
    print(sys.argv)

    >>> ['main.py', '--debug']

source code encoding
--------------------

Python3默认使用utf-8, 除了标准库的``indentifier``用ascii.
如果要指定文件的编码方式，在文件的第一行用

.. code-block:: python3

    # -*- coding: utf-16 -*-

如果有 shebang, 则 shebang 放在第一行，encoding 放在第二行.

.. code-block:: python3

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
