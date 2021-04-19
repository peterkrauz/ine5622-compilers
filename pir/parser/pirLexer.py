# Generated from pir/parser/pir.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2*")
        buf.write("\u0102\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\34\6\34\u00ba\n\34\r\34\16\34\u00bb\3\35\6\35\u00bf")
        buf.write("\n\35\r\35\16\35\u00c0\3\35\3\35\6\35\u00c5\n\35\r\35")
        buf.write("\16\35\u00c6\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\5\37\u00d3\n\37\3 \3 \3 \3 \5 \u00d9\n \3!\3")
        buf.write("!\3\"\3\"\3#\3#\3$\3$\3%\3%\3%\3%\3&\3&\7&\u00e9\n&\f")
        buf.write("&\16&\u00ec\13&\3\'\6\'\u00ef\n\'\r\'\16\'\u00f0\3(\3")
        buf.write("(\7(\u00f5\n(\f(\16(\u00f8\13(\3(\3(\3)\6)\u00fd\n)\r")
        buf.write(")\16)\u00fe\3)\3)\2\2*\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*\3\2\b\3\2\62;\4\2C\\c|\3\2C\\")
        buf.write("\5\2\62;C\\c|\4\2\f\f\17\17\5\2\13\f\16\17\"\"\2\u010c")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\3S\3\2\2")
        buf.write("\2\5U\3\2\2\2\7W\3\2\2\2\tY\3\2\2\2\13[\3\2\2\2\r]\3\2")
        buf.write("\2\2\17e\3\2\2\2\21m\3\2\2\2\23s\3\2\2\2\25x\3\2\2\2\27")
        buf.write("}\3\2\2\2\31\177\3\2\2\2\33\u0081\3\2\2\2\35\u0087\3\2")
        buf.write("\2\2\37\u008d\3\2\2\2!\u0091\3\2\2\2#\u0094\3\2\2\2%\u009b")
        buf.write("\3\2\2\2\'\u00a0\3\2\2\2)\u00a5\3\2\2\2+\u00a8\3\2\2\2")
        buf.write("-\u00aa\3\2\2\2/\u00ac\3\2\2\2\61\u00af\3\2\2\2\63\u00b2")
        buf.write("\3\2\2\2\65\u00b5\3\2\2\2\67\u00b9\3\2\2\29\u00be\3\2")
        buf.write("\2\2;\u00c8\3\2\2\2=\u00d2\3\2\2\2?\u00d8\3\2\2\2A\u00da")
        buf.write("\3\2\2\2C\u00dc\3\2\2\2E\u00de\3\2\2\2G\u00e0\3\2\2\2")
        buf.write("I\u00e2\3\2\2\2K\u00e6\3\2\2\2M\u00ee\3\2\2\2O\u00f2\3")
        buf.write("\2\2\2Q\u00fc\3\2\2\2ST\7.\2\2T\4\3\2\2\2UV\7<\2\2V\6")
        buf.write("\3\2\2\2WX\7?\2\2X\b\3\2\2\2YZ\7*\2\2Z\n\3\2\2\2[\\\7")
        buf.write("+\2\2\\\f\3\2\2\2]^\7D\2\2^_\7q\2\2_`\7q\2\2`a\7n\2\2")
        buf.write("ab\7g\2\2bc\7c\2\2cd\7p\2\2d\16\3\2\2\2ef\7K\2\2fg\7p")
        buf.write("\2\2gh\7v\2\2hi\7g\2\2ij\7i\2\2jk\7g\2\2kl\7t\2\2l\20")
        buf.write("\3\2\2\2mn\7H\2\2no\7n\2\2op\7q\2\2pq\7c\2\2qr\7v\2\2")
        buf.write("r\22\3\2\2\2st\7E\2\2tu\7j\2\2uv\7c\2\2vw\7t\2\2w\24\3")
        buf.write("\2\2\2xy\7c\2\2yz\7j\2\2z{\7q\2\2{|\7{\2\2|\26\3\2\2\2")
        buf.write("}~\7}\2\2~\30\3\2\2\2\177\u0080\7\177\2\2\u0080\32\3\2")
        buf.write("\2\2\u0081\u0082\7e\2\2\u0082\u0083\7n\2\2\u0083\u0084")
        buf.write("\7c\2\2\u0084\u0085\7u\2\2\u0085\u0086\7u\2\2\u0086\34")
        buf.write("\3\2\2\2\u0087\u0088\7y\2\2\u0088\u0089\7j\2\2\u0089\u008a")
        buf.write("\7k\2\2\u008a\u008b\7n\2\2\u008b\u008c\7g\2\2\u008c\36")
        buf.write("\3\2\2\2\u008d\u008e\7h\2\2\u008e\u008f\7q\2\2\u008f\u0090")
        buf.write("\7t\2\2\u0090 \3\2\2\2\u0091\u0092\7k\2\2\u0092\u0093")
        buf.write("\7p\2\2\u0093\"\3\2\2\2\u0094\u0095\7u\2\2\u0095\u0096")
        buf.write("\7y\2\2\u0096\u0097\7k\2\2\u0097\u0098\7v\2\2\u0098\u0099")
        buf.write("\7e\2\2\u0099\u009a\7j\2\2\u009a$\3\2\2\2\u009b\u009c")
        buf.write("\7e\2\2\u009c\u009d\7c\2\2\u009d\u009e\7u\2\2\u009e\u009f")
        buf.write("\7g\2\2\u009f&\3\2\2\2\u00a0\u00a1\7g\2\2\u00a1\u00a2")
        buf.write("\7n\2\2\u00a2\u00a3\7u\2\2\u00a3\u00a4\7g\2\2\u00a4(\3")
        buf.write("\2\2\2\u00a5\u00a6\7k\2\2\u00a6\u00a7\7h\2\2\u00a7*\3")
        buf.write("\2\2\2\u00a8\u00a9\7@\2\2\u00a9,\3\2\2\2\u00aa\u00ab\7")
        buf.write(">\2\2\u00ab.\3\2\2\2\u00ac\u00ad\7@\2\2\u00ad\u00ae\7")
        buf.write("?\2\2\u00ae\60\3\2\2\2\u00af\u00b0\7>\2\2\u00b0\u00b1")
        buf.write("\7?\2\2\u00b1\62\3\2\2\2\u00b2\u00b3\7?\2\2\u00b3\u00b4")
        buf.write("\7?\2\2\u00b4\64\3\2\2\2\u00b5\u00b6\7#\2\2\u00b6\u00b7")
        buf.write("\7?\2\2\u00b7\66\3\2\2\2\u00b8\u00ba\t\2\2\2\u00b9\u00b8")
        buf.write("\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bb")
        buf.write("\u00bc\3\2\2\2\u00bc8\3\2\2\2\u00bd\u00bf\t\2\2\2\u00be")
        buf.write("\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00be\3\2\2\2")
        buf.write("\u00c0\u00c1\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c4\7")
        buf.write("\60\2\2\u00c3\u00c5\t\2\2\2\u00c4\u00c3\3\2\2\2\u00c5")
        buf.write("\u00c6\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2")
        buf.write("\u00c7:\3\2\2\2\u00c8\u00c9\7)\2\2\u00c9\u00ca\t\3\2\2")
        buf.write("\u00ca\u00cb\7)\2\2\u00cb<\3\2\2\2\u00cc\u00cd\7C\2\2")
        buf.write("\u00cd\u00ce\7{\2\2\u00ce\u00d3\7g\2\2\u00cf\u00d0\7P")
        buf.write("\2\2\u00d0\u00d1\7c\2\2\u00d1\u00d3\7{\2\2\u00d2\u00cc")
        buf.write("\3\2\2\2\u00d2\u00cf\3\2\2\2\u00d3>\3\2\2\2\u00d4\u00d9")
        buf.write("\5\67\34\2\u00d5\u00d9\59\35\2\u00d6\u00d9\5;\36\2\u00d7")
        buf.write("\u00d9\5=\37\2\u00d8\u00d4\3\2\2\2\u00d8\u00d5\3\2\2\2")
        buf.write("\u00d8\u00d6\3\2\2\2\u00d8\u00d7\3\2\2\2\u00d9@\3\2\2")
        buf.write("\2\u00da\u00db\7-\2\2\u00dbB\3\2\2\2\u00dc\u00dd\7/\2")
        buf.write("\2\u00ddD\3\2\2\2\u00de\u00df\7,\2\2\u00dfF\3\2\2\2\u00e0")
        buf.write("\u00e1\7\61\2\2\u00e1H\3\2\2\2\u00e2\u00e3\7\f\2\2\u00e3")
        buf.write("\u00e4\3\2\2\2\u00e4\u00e5\b%\2\2\u00e5J\3\2\2\2\u00e6")
        buf.write("\u00ea\t\4\2\2\u00e7\u00e9\t\3\2\2\u00e8\u00e7\3\2\2\2")
        buf.write("\u00e9\u00ec\3\2\2\2\u00ea\u00e8\3\2\2\2\u00ea\u00eb\3")
        buf.write("\2\2\2\u00ebL\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ed\u00ef")
        buf.write("\t\5\2\2\u00ee\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0")
        buf.write("\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1N\3\2\2\2\u00f2")
        buf.write("\u00f6\7%\2\2\u00f3\u00f5\n\6\2\2\u00f4\u00f3\3\2\2\2")
        buf.write("\u00f5\u00f8\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f6\u00f7\3")
        buf.write("\2\2\2\u00f7\u00f9\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f9\u00fa")
        buf.write("\b(\2\2\u00faP\3\2\2\2\u00fb\u00fd\t\7\2\2\u00fc\u00fb")
        buf.write("\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe")
        buf.write("\u00ff\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0101\b)\2\2")
        buf.write("\u0101R\3\2\2\2\f\2\u00bb\u00c0\u00c6\u00d2\u00d8\u00ea")
        buf.write("\u00f0\u00f6\u00fe\3\b\2\2")
        return buf.getvalue()


class pirLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    IntegerLiteral = 27
    FloatLiteral = 28
    CharLiteral = 29
    BooleanLiteral = 30
    GeneralLiteral = 31
    AdditionOperator = 32
    SubtractionOperator = 33
    MultiplicationOperator = 34
    DivisionOperator = 35
    NewLine = 36
    ClassIdentifier = 37
    Identifier = 38
    Comment = 39
    WS = 40

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "':'", "'='", "'('", "')'", "'Boolean'", "'Integer'", 
            "'Float'", "'Char'", "'ahoy'", "'{'", "'}'", "'class'", "'while'", 
            "'for'", "'in'", "'switch'", "'case'", "'else'", "'if'", "'>'", 
            "'<'", "'>='", "'<='", "'=='", "'!='", "'+'", "'-'", "'*'", 
            "'/'", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "IntegerLiteral", "FloatLiteral", "CharLiteral", "BooleanLiteral", 
            "GeneralLiteral", "AdditionOperator", "SubtractionOperator", 
            "MultiplicationOperator", "DivisionOperator", "NewLine", "ClassIdentifier", 
            "Identifier", "Comment", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "IntegerLiteral", "FloatLiteral", "CharLiteral", "BooleanLiteral", 
                  "GeneralLiteral", "AdditionOperator", "SubtractionOperator", 
                  "MultiplicationOperator", "DivisionOperator", "NewLine", 
                  "ClassIdentifier", "Identifier", "Comment", "WS" ]

    grammarFileName = "pir.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


