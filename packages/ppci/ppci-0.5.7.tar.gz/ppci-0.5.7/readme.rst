
Introduction
============

The PPCI (Pure Python Compiler Infrastructure) project is a compiler
written entirely in the `Python <https://www.python.org/>`_ programming
language. It contains front-ends for various programming languages as
well as machine code generation functionality. With this library you can
generate (working!) machine code using Python (and thus very easy to
explore, extend, etc.)!

The project contains the following:

- A compiler, an assembler, a linker and a build system
- Language front-ends: Brainfuck, C, c3, WebAssembly
- CPU backends: 6500, arm, avr, m68k, microblaze, msp430, openrisc, risc-v, stm8,
  x86_64, xtensa
- Other backends: WebAssembly, Python

.. warning::

    **This project is in alpha state and not ready for production use!**

You can try out PPCI at godbolt.org, a site which offers Web access to
various compilers: https://godbolt.org/g/eooaPP

API
---

API example to compile c3 code:

.. code-block:: python

    >>> import io
    >>> from ppci.api import c3c, link
    >>> source_file = io.StringIO("""
    ... module main;
    ... function void print(string txt) {
    ... }
    ... function void main() {
    ...  print("Hello world");
    ... }""")
    >>> obj = c3c([source_file], [], 'arm')
    >>> obj = link([obj])

Example how to assemble some assembly code:

.. code-block:: python

    >>> import io
    >>> from ppci.api import asm
    >>> source_file = io.StringIO("""section code
    ... pop rbx
    ... push r10
    ... mov rdi, 42""")
    >>> obj = asm(source_file, 'x86_64')
    >>> obj.get_section('code').data
    bytearray(b'[ARH\xbf*\x00\x00\x00\x00\x00\x00\x00')

Example of the low level api usage:

.. code-block:: python

    >>> from ppci.arch.x86_64 import instructions, registers
    >>> i = instructions.Pop(registers.rbx)
    >>> i.encode()
    b'['

Documentation
-------------

Documentation can be found here:

- https://ppci.readthedocs.io/


|gitter|_
|appveyor|_
|codecov|_
|docstate|_
|travis|_
|codacygrade|_
|codacycoverage|_
|downloads|_
|conda|_

.. |codecov| image:: https://codecov.io/bb/windel/ppci/branch/default/graph/badge.svg
.. _codecov: https://codecov.io/bb/windel/ppci/branch/default


.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/h0h5huliflrac65o?svg=true
.. _appveyor: https://ci.appveyor.com/project/WindelBouwman/ppci-786


.. |docstate| image:: https://readthedocs.org/projects/ppci/badge/?version=latest
.. _docstate: https://ppci.readthedocs.io/en/latest


.. |travis| image:: https://travis-ci.org/windelbouwman/ppci-mirror.svg?branch=master
.. _travis: https://travis-ci.org/windelbouwman/ppci-mirror


.. |codacygrade| image:: https://api.codacy.com/project/badge/Grade/a178be14a54243be81c27172031dc82c
.. _codacygrade: https://www.codacy.com/app/windel-bouwman/ppci-mirror

.. |codacycoverage| image:: https://api.codacy.com/project/badge/Coverage/a178be14a54243be81c27172031dc82c
.. _codacycoverage: https://www.codacy.com/app/windel-bouwman/ppci-mirror


.. |downloads| image:: https://anaconda.org/conda-forge/ppci/badges/downloads.svg
.. _downloads: https://anaconda.org/conda-forge/ppci

.. |conda| image:: https://anaconda.org/conda-forge/ppci/badges/version.svg
.. _conda: https://anaconda.org/conda-forge/ppci


.. |gitter| image:: https://badges.gitter.im/ppci-chat/Lobby.svg
.. _gitter: https://gitter.im/ppci-chat/Lobby
