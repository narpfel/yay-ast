#!/usr/bin/env python3

from setuptools import setup, Extension


_yay_ast = Extension(
    "_yay_ast",
    include_dirs=["_yay_ast/Include"],
    sources=[
        "_yay_ast/Custom/yay_ast.c",
        "_yay_ast/Parser/acceler.c",
        "_yay_ast/Parser/bitset.c",
        "_yay_ast/Parser/grammar.c",
        "_yay_ast/Parser/grammar1.c",
        "_yay_ast/Parser/node.c",
        "_yay_ast/Parser/parser.c",
        "_yay_ast/Parser/parsetok.c",
        "_yay_ast/Parser/tokenizer.c",
        "_yay_ast/Python/asdl.c",
        "_yay_ast/Python/ast.c",
        "_yay_ast/Python/graminit.c",
        "_yay_ast/Python/Python-ast.c",
    ],
    depends=[
        "_yay_ast/Include/asdl.h",
        "_yay_ast/Include/ast.h",
        "_yay_ast/Include/bitset.h",
        "_yay_ast/Include/compile.h",
        "_yay_ast/Include/errcode.h",
        "_yay_ast/Include/graminit.h",
        "_yay_ast/Include/grammar.h",
        "_yay_ast/Include/node.h",
        "_yay_ast/Include/parsetok.h",
        "_yay_ast/Include/Python-ast.h",
        "_yay_ast/Include/token.h",
        "_yay_ast/Parser/parser.h",
        "_yay_ast/Parser/tokenizer.h",
    ]
)


setup(
    name="yay_ast",
    version="3.6.1",
    py_modules=["yay_ast"],
    ext_modules=[_yay_ast],
    license="PSFL",
    keywords="yay",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
)
