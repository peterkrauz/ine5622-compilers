# Generated from pir/parser/pir.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .pirParser import pirParser
else:
    from pirParser import pirParser

# This class defines a complete generic visitor for a parse tree produced by pirParser.

class pirVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by pirParser#start.
    def visitStart(self, ctx:pirParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#generalArgument.
    def visitGeneralArgument(self, ctx:pirParser.GeneralArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#generalArguments.
    def visitGeneralArguments(self, ctx:pirParser.GeneralArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#typedArguments.
    def visitTypedArguments(self, ctx:pirParser.TypedArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#classAssignment.
    def visitClassAssignment(self, ctx:pirParser.ClassAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#booleanAssignment.
    def visitBooleanAssignment(self, ctx:pirParser.BooleanAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#integerAssignment.
    def visitIntegerAssignment(self, ctx:pirParser.IntegerAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#floatAssignment.
    def visitFloatAssignment(self, ctx:pirParser.FloatAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#charAssignment.
    def visitCharAssignment(self, ctx:pirParser.CharAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#booleanType.
    def visitBooleanType(self, ctx:pirParser.BooleanTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#integerType.
    def visitIntegerType(self, ctx:pirParser.IntegerTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#floatType.
    def visitFloatType(self, ctx:pirParser.FloatTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#charType.
    def visitCharType(self, ctx:pirParser.CharTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#numberType.
    def visitNumberType(self, ctx:pirParser.NumberTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#genericType.
    def visitGenericType(self, ctx:pirParser.GenericTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#functionKeyword.
    def visitFunctionKeyword(self, ctx:pirParser.FunctionKeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#functionName.
    def visitFunctionName(self, ctx:pirParser.FunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:pirParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#functionInvocation.
    def visitFunctionInvocation(self, ctx:pirParser.FunctionInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#classDeclaration.
    def visitClassDeclaration(self, ctx:pirParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#classConstructor.
    def visitClassConstructor(self, ctx:pirParser.ClassConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#simpleClassDeclaration.
    def visitSimpleClassDeclaration(self, ctx:pirParser.SimpleClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#completeClassDeclaration.
    def visitCompleteClassDeclaration(self, ctx:pirParser.CompleteClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#typeDeclaration.
    def visitTypeDeclaration(self, ctx:pirParser.TypeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#generalDeclaration.
    def visitGeneralDeclaration(self, ctx:pirParser.GeneralDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#generalInvocation.
    def visitGeneralInvocation(self, ctx:pirParser.GeneralInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#generalExpression.
    def visitGeneralExpression(self, ctx:pirParser.GeneralExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#loopExpression.
    def visitLoopExpression(self, ctx:pirParser.LoopExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#whileExpression.
    def visitWhileExpression(self, ctx:pirParser.WhileExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#forExpression.
    def visitForExpression(self, ctx:pirParser.ForExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#controlExpression.
    def visitControlExpression(self, ctx:pirParser.ControlExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#switchCaseExpression.
    def visitSwitchCaseExpression(self, ctx:pirParser.SwitchCaseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#switchCaseBody.
    def visitSwitchCaseBody(self, ctx:pirParser.SwitchCaseBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#switchCaseCaseBranch.
    def visitSwitchCaseCaseBranch(self, ctx:pirParser.SwitchCaseCaseBranchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#switchCaseElseBranch.
    def visitSwitchCaseElseBranch(self, ctx:pirParser.SwitchCaseElseBranchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#ifExpression.
    def visitIfExpression(self, ctx:pirParser.IfExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#elseExpression.
    def visitElseExpression(self, ctx:pirParser.ElseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#comparisonExpression.
    def visitComparisonExpression(self, ctx:pirParser.ComparisonExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#comparisonOperand.
    def visitComparisonOperand(self, ctx:pirParser.ComparisonOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#comparisonOperator.
    def visitComparisonOperator(self, ctx:pirParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#algebraicExpression.
    def visitAlgebraicExpression(self, ctx:pirParser.AlgebraicExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#integerAlgebraicExpression.
    def visitIntegerAlgebraicExpression(self, ctx:pirParser.IntegerAlgebraicExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#integerMultiplicationExpression.
    def visitIntegerMultiplicationExpression(self, ctx:pirParser.IntegerMultiplicationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#integerSummationExpression.
    def visitIntegerSummationExpression(self, ctx:pirParser.IntegerSummationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#floatAlgebraicExpression.
    def visitFloatAlgebraicExpression(self, ctx:pirParser.FloatAlgebraicExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#floatMultiplicationExpression.
    def visitFloatMultiplicationExpression(self, ctx:pirParser.FloatMultiplicationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#floatSummationExpression.
    def visitFloatSummationExpression(self, ctx:pirParser.FloatSummationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#generalAssignment.
    def visitGeneralAssignment(self, ctx:pirParser.GeneralAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pirParser#baseParameter.
    def visitBaseParameter(self, ctx:pirParser.BaseParameterContext):
        return self.visitChildren(ctx)



del pirParser