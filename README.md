`yay_ast`
---------

Fork of the CPython parser to parse `yay` files.

Update process inspired by [`typed_ast`](https://github.com/python/typed_ast).



Initial setup
-------------

1. Copy necessary files from CPython repo.
   ```
   _yay_ast
   ├── Grammar
   │   └── Grammar
   ├── Include
   │   ├── asdl.h
   │   ├── ast.h
   │   ├── bitset.h
   │   ├── compile.h
   │   ├── errcode.h
   │   ├── graminit.h
   │   ├── grammar.h
   │   ├── node.h
   │   ├── parsetok.h
   │   ├── Python-ast.h
   │   └── token.h
   ├── Parser
   │   ├── acceler.c
   │   ├── asdl_c.py
   │   ├── asdl.py
   │   ├── bitset.c
   │   ├── grammar1.c
   │   ├── grammar.c
   │   ├── node.c
   │   ├── parser.c
   │   ├── parser.h
   │   ├── parsetok.c
   │   ├── Python.asdl
   │   ├── tokenizer.c
   │   └── tokenizer.h
   ├── Pgen
   │   ├── dynamic_annotations.c
   │   ├── firstsets.c
   │   ├── listnode.c
   │   ├── metagrammar.c
   │   ├── mysnprintf.c
   │   ├── obmalloc.c
   │   ├── parsetok_pgen.c
   │   ├── pgen.c
   │   ├── pgenmain.c
   │   ├── printgrammar.c
   │   ├── pyctype.c
   │   └── tokenizer_pgen.c
   └── Python
       ├── asdl.c
       ├── ast.c
       ├── graminit.c
       └── Python-ast.c
   ```
1. Create `setup.py` file.
1. Make sure it compiles: `python setup.py build`.
1. Commit (ef46bd949ff9cb73406369cb7cdeaaecf9f5facf)
1. Rename `_ast` to `_yay_ast` in `_yay_ast/Python/Python-ast.c`.
1. Commit (163f16e37ce4bb0ecd017d812eb6d9cbc57b1220).
1. Assemble `_yay_ast/Custom/yay_ast.c` (for `_yay_ast._parse` to be used instead
   of `__builtins__.compile` in `yay_ast.parse`.) and add to `setup.py`.
1. Commit (a5716aeb9f4d2d9316b9d2737707e6cbc20037ee).
1. Add `yay_ast_parse` from `Custom/yay_ast.c` to `_yay_ast` module.
1. Commit (3eae9f472c2c95c699ff27ba7a208da192e5721f).
1. Compile: `python setup.py build`.
1. Rename exported symbol names to avoid collisions with the original CPython parser.
   1. `tools/find_exported_symbols`
   1. `tools/update_exported_symbols`
   1. (TODO: Use `clang-rename` or something similar instead of the hacked `sed` & `grep` scripts.)
1. Compile again.
1. Commit (69f3aa79aec655024b57187a93291980c4b54a8f).
1. Modify `yay_ast.parse` to not use `__builtins__.compile`.
1. Commit (f23368fb09a5d57a37ff67e111e57f2211626a68).
1. Adapt `Parser/asdl_c.py` to emit `Yay` prefix.
1. Commit (38c2171dacd04c8910c10783e95a668ef231033a).
1. Update include header guards (`tools/update_include_guards`)
   * The complete `#ifndef Py_LIMITED_API` block in `_yay_ast/Include/compile.h`
     has to be removed.
1. Commit (0419bc444e3402deb603091cc16e04f74b838e18).
1. Now new features can be added to the grammar. Follow the
   [CPython devguide](https://docs.python.org/devguide/grammar.html).
   1. Update `Grammar/Grammar` file.
   1. Add new AST nodes to `Parser/Python.asdl`.
   1. Add new tokens to `Include/token.h`.
   1. Update `Parser/tokenizer.c` to recongnize new tokens.
   1. Update `Python/ast.c` to emit new AST nodes.
   1. Run `tools/make_grammar` and `tools/make_python-ast` to regenerate
      `graminit.{h,c}` and the `_yay_ast` module (`Python/Python-ast.c`).
   1. Commit (c048cc936b926b8997ceefe5c8a26212e6bc488e).



Update process
--------------

TODO! -- Wait for next CPython minor release to find suitable update process.



Copyright and License Information
---------------------------------

The contents of this repository are licensed under the Python Software
Foundation License.

Copyright (c) 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011,
2012, 2013, 2014, 2015, 2016 Python Software Foundation.  All rights reserved.

Copyright (c) 2000 BeOpen.com.  All rights reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.  All
rights reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum.  All rights reserved.

See the file "LICENSE" for information terms & conditions for usage, and a
DISCLAIMER OF ALL WARRANTIES.

This Python distribution contains *no* GNU General Public License (GPL) code,
so it may be used in proprietary projects.  There are interfaces to some GNU
code but these are entirely optional.

All trademarks referenced herein are property of their respective holders.
