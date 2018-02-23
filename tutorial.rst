The Python Tutorial
-------------------
High-level data structure, simple object-oriented, dynamic typing.

A python interpreter, which is extensible with C/C++, with standard library, 3rd-party library.

The Python Tutorial
    basic concepts and features.

    introduces noteworthyly features.

    pre-reading for standard library.

The Python Standard Library
    standard objects/modules

The Python Language Reference
    formal definition of python

Extending and Embedding the Python Interpreter
Python/C API Reference Manual
    write extensions in C/C++

Glossary
    terms used in python

- Whetting Your Appetite
- Using the Python Interpreter
    - Invoking the Interpreter
        - Argument Passing
        - Interactive Mode
    - :ref:`The Interpreter and Its Environment`
        - Source Code Encoding
- 3. An Informal Introduction to Python
    - 3.1. Using Python as a Calculator
        - 3.1.1. Numbers
        - :ref:`Strings <Strings>`
        - 3.1.3. Lists
    - 3.2. First Steps Towards Programming
- 4. More Control Flow Tools
    - 4.1. if
    - 4.2. for
    - 4.3. range()
    - 4.4. break / continue, else Clauses
    - 4.5. pass
    - 4.6. Defining Functions
    - 4.7. More on Defining Functions
        - 4.7.1. Default Argument Values
        - 4.7.2. Keyword Arguments
        - 4.7.3. Arbitrary Argument Lists
        - 4.7.4. Unpacking Argument Lists
        - 4.7.5. Unpacking Expressions
        - 4.7.6. Documentation Strings
        - 4.7.7. Function Annotations
    - 4.8. Coding Style
- 5. Data Structure
    - 5.1. More on Lists
        - 5.1.1. as Stacks
        - 5.1.2. as Queues
        - 5.1.3. List Comprehensions
        - 5.1.4. Nested List Comprehensions
    - 5.2. The del Statement
    - 5.3. Tuples and Sequences
    - 5.4. Sets
    - 5.5. Dictionaries
    - 5.6. Looping Techniques
    - 5.7. More on Conditions
    - 5.8. Comparing Sequences and Other Types
- modules
    - more on modules
        - executing as scripts
        - search path
        - "compiled" python files
    - standard modules
    - dir()
    - packages
        - import *
        - intra-package ref
        - packages and multiple dirs
- input / output
    - fancier output format
        - old string format
    - r / w files
        - methods of file objects
        - json
- errors / exceptions
    - syntax errors
    - exceptions
    - handle exceptions
    - raising exceptions
    - user-defined exceptions
    - define clean-up actions
    - predefined clean-up
- classes
    - a word about names and objects
    - scopes and namespaces
        - examples
    - a first look at classes
        - definition
        - class objects
        - instance obj
        - method obj
        - class and instance vars
    - random remarks
    - inheritance
        - multiple inheritance
    - private vars
    - odds and ends
    - iterators
    - generators
    - generator expressions
- biref tour of std lib
    - os interface
    - file wildcards
    - cli args
    - err output redirections / terminate program
    - string pattern match
    - mathematics
    - internet access
    - dates / times
    - data compression
    - performance measurement
    - quality control
    - batteries included
- brief tour of stdlib 2
    - output formatting
    - templating
    - working with bin data
    - multi-threading
    - logging
    - weak refenrence
    - tools for lists
    - decimal floating point arithmetic
- virtual env / packages
    - intro
    - creating venv
    - pip
- what's now
- interactive input editing and history substitution
    - tab completion
    - alternatives to interactive interpreter
- floating point: issues / limitation
    representation error
- appendix
    - interactive mode
        - err handle
        - executable python script
        - interactive startup file
        - customization modules


.. _Whetting Your Appetite
Automate works, faster than *write/compile/test/recompile* circle, writing test
suite, use extension language. -- That's what Python supply.



.. _The Interpreter and Its Environment
source code encoding

python3 默认使用 utf-8，除了标准库的indentifier 用 ascii
如果要指定文件的编码方式，在文件的第一行用::
    # -*- coding: utf-16 -*-

如果有 shebang::
    #!/usr/bin/env python3

则 shebang 放在第一行，encoding 放在第二行

.. _Strings

Python 字符一般用 string 来操作，'' 和 "" 是一样的，不像 C
中的字符数组和字符。另外，遇到::
    "I say, \"hello\"."
    'I say, \'hello\'.'

这样的情况，两者其实都要 escape，但 ' 可一少按一个键，更方便。

.. _More on Defining Functions

有三种定义多个函数参数参数的方式，可以组合

.. _Default Argument Values

::
    def func(a, b=2):
        return a ** b

调用::
    func(2)
    >>> 2 ** 2
    func(2, 3)
    >>> 2 ** 3

*Warning:
默认参数只会初始化一次，如果用可变的参数作为初始值，会在每次调用的时候改变参数的值*

::
    def apnd(a, L=[]):
        return L.append(a)

::
    print(apnd(1))
    >> [1]
    print(apnd(1))
    >> [1, 1]
    print(apnd(1))
    >> [1, 1, 1]

如果想避免上述情况::
    def apnd(a, L=None):
        if L is None:
            L = []
        return L.append(a)

.. _Keayword Arguments

.. _Arbitrary Argument Lists

::
    def write_items(f, sep, *args):
        file.write(sep.join(args))

::
    write_items(f, '/', 'included', 'in', 'args')
    >> 'included/in/args'

其中，当参数使用 * 的时候，args 变量是一个 tuple，把余下的所有实参放在这个
tuple 中。

args 后面还可以定义参数，但必须是 Keyword Arguments::
    def write_items(f, *args, sep='/'):
        return sep.join(args)

::
    write_items(f, 'all', 'in', 'args')
    >> 'all/in/args'
    write_items(f, 'all', 'in', 'args', sep=',')
    >> 'all,in,args'
