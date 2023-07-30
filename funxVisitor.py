# Generated from funx.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .funxParser import funxParser
else:
    from funxParser import funxParser

# This class defines a complete generic visitor for a parse tree produced by funxParser.

class funxVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by funxParser#root.
    def visitRoot(self, ctx:funxParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#Expres.
    def visitExpres(self, ctx:funxParser.ExpresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#Assig.
    def visitAssig(self, ctx:funxParser.AssigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#Conditional.
    def visitConditional(self, ctx:funxParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#While.
    def visitWhile(self, ctx:funxParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#BoolPar.
    def visitBoolPar(self, ctx:funxParser.BoolParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#Negation.
    def visitNegation(self, ctx:funxParser.NegationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#Comparison.
    def visitComparison(self, ctx:funxParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#bloc.
    def visitBloc(self, ctx:funxParser.BlocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#func.
    def visitFunc(self, ctx:funxParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#Par.
    def visitPar(self, ctx:funxParser.ParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#Call.
    def visitCall(self, ctx:funxParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#Variable.
    def visitVariable(self, ctx:funxParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#Negative.
    def visitNegative(self, ctx:funxParser.NegativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#Bin.
    def visitBin(self, ctx:funxParser.BinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#Valor.
    def visitValor(self, ctx:funxParser.ValorContext):
        return self.visitChildren(ctx)



del funxParser