.. _The Interpreter and Its Environment

Python解释器
===========

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
