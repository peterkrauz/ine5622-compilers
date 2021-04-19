from .parser.pirParser import pirParser
from .parser.pirVisitor import pirVisitor
from typing import List, Dict, Callable

class globVisitor(pirVisitor):
    def __init__(self, file_name):
        self.file_name = file_name
        self.func_table = set()

    # Visit a parse tree produced by pirParser#generalArguments.
    def visitGeneralArguments(self, ctx:pirParser.GeneralArgumentsContext):
        return [str(id) for id in ctx.generalArgument()]
