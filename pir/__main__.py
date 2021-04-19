from antlr4 import FileStream, CommonTokenStream
from os import path
import argparse

try:
    from .parser.pirLexer import pirLexer
    from .parser.pirParser import pirParser
except ImportError:
    # Generate ANTLR parser from g4 file
    from .generate_parser import generate_parser
    generate_parser(path.join(path.dirname(__file__), 'parser/pir.g4'))

    from .parser.pirLexer import pirLexer
    from .parser.pirParser import pirParser

from .globVisitor import globVisitor
from .parser.pirVisitor import pirVisitor


def main():

    # Argument parser
    parser_args = argparse.ArgumentParser(prog='pir', description='C-- interpreter')
    parser_args.add_argument('input', type=str, help='source code')

    args = parser_args.parse_args()
    #################################

    input_stream = FileStream(args.input)

    lexer = pirLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = pirParser(stream)

    tree = parser.start() # Get AST
    visitor = globVisitor(args.input)
    glob = visitor.visitStart(tree)

if __name__ == '__main__':
    main()
