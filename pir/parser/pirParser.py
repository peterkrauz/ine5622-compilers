# Generated from pir/parser/pir.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3*")
        buf.write("\u01bf\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\7\2f\n\2\f\2\16")
        buf.write("\2i\13\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\7\4r\n\4\f\4\16\4")
        buf.write("u\13\4\3\5\3\5\3\5\7\5z\n\5\f\5\16\5}\13\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\5\6\u0086\n\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u0097\n\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00a0\n\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17")
        buf.write("\5\17\u00b2\n\17\3\20\3\20\3\20\3\20\5\20\u00b8\n\20\3")
        buf.write("\21\3\21\3\22\3\22\3\23\3\23\3\23\3\23\5\23\u00c2\n\23")
        buf.write("\3\23\3\23\3\23\7\23\u00c7\n\23\f\23\16\23\u00ca\13\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\5\24\u00d1\n\24\3\24\3\24\3")
        buf.write("\25\3\25\5\25\u00d7\n\25\3\26\3\26\3\26\3\26\7\26\u00dd")
        buf.write("\n\26\f\26\16\26\u00e0\13\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\5\27\u00e7\n\27\3\30\3\30\3\30\7\30\u00ec\n\30\f\30\16")
        buf.write("\30\u00ef\13\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u00ff\n\32\3\33\3")
        buf.write("\33\3\33\3\33\5\33\u0105\n\33\3\34\3\34\3\34\5\34\u010a")
        buf.write("\n\34\3\35\3\35\5\35\u010e\n\35\3\36\3\36\3\36\3\36\7")
        buf.write("\36\u0114\n\36\f\36\16\36\u0117\13\36\3\36\3\36\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\7\37\u0121\n\37\f\37\16\37\u0124")
        buf.write("\13\37\3\37\3\37\3 \3 \5 \u012a\n \3 \5 \u012d\n \3!\3")
        buf.write("!\3!\3!\3!\3!\3\"\7\"\u0136\n\"\f\"\16\"\u0139\13\"\3")
        buf.write("\"\3\"\3#\3#\3#\5#\u0140\n#\3#\3#\7#\u0144\n#\f#\16#\u0147")
        buf.write("\13#\3#\3#\3$\3$\3$\7$\u014e\n$\f$\16$\u0151\13$\3$\3")
        buf.write("$\3%\3%\3%\3%\7%\u0159\n%\f%\16%\u015c\13%\3%\3%\3&\3")
        buf.write("&\3&\7&\u0163\n&\f&\16&\u0166\13&\3&\3&\3\'\3\'\3\'\3")
        buf.write("\'\3\'\5\'\u016f\n\'\3(\3(\3(\3(\5(\u0175\n(\3)\3)\3*")
        buf.write("\3*\5*\u017b\n*\3+\3+\5+\u017f\n+\3,\3,\3,\3,\3,\5,\u0186")
        buf.write("\n,\3,\3,\3,\3,\3,\3,\3,\5,\u018f\n,\3-\3-\3-\3-\3-\5")
        buf.write("-\u0196\n-\3-\3-\3-\3-\3-\3-\3-\5-\u019f\n-\3.\3.\5.\u01a3")
        buf.write("\n.\3/\3/\3/\3/\3/\5/\u01aa\n/\3\60\3\60\5\60\u01ae\n")
        buf.write("\60\3\60\3\60\3\60\3\60\5\60\u01b4\n\60\3\61\3\61\3\61")
        buf.write("\3\61\3\61\5\61\u01bb\n\61\3\62\3\62\3\62\2\2\63\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BDFHJLNPRTVXZ\\^`b\2\n\4\2\35 ((\4\2  ((\4\2\37\37")
        buf.write("((\4\2!!((\3\2\27\34\3\2$%\3\2\"#\4\2\35\36((\2\u01cd")
        buf.write("\2g\3\2\2\2\4l\3\2\2\2\6n\3\2\2\2\bv\3\2\2\2\n~\3\2\2")
        buf.write("\2\f\u0089\3\2\2\2\16\u008f\3\2\2\2\20\u0098\3\2\2\2\22")
        buf.write("\u00a1\3\2\2\2\24\u00a7\3\2\2\2\26\u00a9\3\2\2\2\30\u00ab")
        buf.write("\3\2\2\2\32\u00ad\3\2\2\2\34\u00b1\3\2\2\2\36\u00b7\3")
        buf.write("\2\2\2 \u00b9\3\2\2\2\"\u00bb\3\2\2\2$\u00bd\3\2\2\2&")
        buf.write("\u00cd\3\2\2\2(\u00d6\3\2\2\2*\u00d8\3\2\2\2,\u00e3\3")
        buf.write("\2\2\2.\u00e8\3\2\2\2\60\u00f2\3\2\2\2\62\u00fe\3\2\2")
        buf.write("\2\64\u0104\3\2\2\2\66\u0109\3\2\2\28\u010d\3\2\2\2:\u010f")
        buf.write("\3\2\2\2<\u011a\3\2\2\2>\u012c\3\2\2\2@\u012e\3\2\2\2")
        buf.write("B\u0137\3\2\2\2D\u013c\3\2\2\2F\u014a\3\2\2\2H\u0154\3")
        buf.write("\2\2\2J\u015f\3\2\2\2L\u016e\3\2\2\2N\u0174\3\2\2\2P\u0176")
        buf.write("\3\2\2\2R\u017a\3\2\2\2T\u017e\3\2\2\2V\u0185\3\2\2\2")
        buf.write("X\u0195\3\2\2\2Z\u01a2\3\2\2\2\\\u01a4\3\2\2\2^\u01ad")
        buf.write("\3\2\2\2`\u01ba\3\2\2\2b\u01bc\3\2\2\2df\5\62\32\2ed\3")
        buf.write("\2\2\2fi\3\2\2\2ge\3\2\2\2gh\3\2\2\2hj\3\2\2\2ig\3\2\2")
        buf.write("\2jk\7\2\2\3k\3\3\2\2\2lm\t\2\2\2m\5\3\2\2\2ns\5\4\3\2")
        buf.write("op\7\3\2\2pr\5\4\3\2qo\3\2\2\2ru\3\2\2\2sq\3\2\2\2st\3")
        buf.write("\2\2\2t\7\3\2\2\2us\3\2\2\2v{\5\60\31\2wx\7\3\2\2xz\5")
        buf.write("\60\31\2yw\3\2\2\2z}\3\2\2\2{y\3\2\2\2{|\3\2\2\2|\t\3")
        buf.write("\2\2\2}{\3\2\2\2~\177\7(\2\2\177\u0080\7\4\2\2\u0080\u0081")
        buf.write("\7\'\2\2\u0081\u0082\7\5\2\2\u0082\u0083\7\'\2\2\u0083")
        buf.write("\u0085\7\6\2\2\u0084\u0086\5\6\4\2\u0085\u0084\3\2\2\2")
        buf.write("\u0085\u0086\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0088\7")
        buf.write("\7\2\2\u0088\13\3\2\2\2\u0089\u008a\7(\2\2\u008a\u008b")
        buf.write("\7\4\2\2\u008b\u008c\5\24\13\2\u008c\u008d\7\5\2\2\u008d")
        buf.write("\u008e\t\3\2\2\u008e\r\3\2\2\2\u008f\u0090\7(\2\2\u0090")
        buf.write("\u0091\7\4\2\2\u0091\u0092\5\26\f\2\u0092\u0096\7\5\2")
        buf.write("\2\u0093\u0097\5T+\2\u0094\u0097\7\35\2\2\u0095\u0097")
        buf.write("\7(\2\2\u0096\u0093\3\2\2\2\u0096\u0094\3\2\2\2\u0096")
        buf.write("\u0095\3\2\2\2\u0097\17\3\2\2\2\u0098\u0099\7(\2\2\u0099")
        buf.write("\u009a\7\4\2\2\u009a\u009b\5\30\r\2\u009b\u009f\7\5\2")
        buf.write("\2\u009c\u00a0\5Z.\2\u009d\u00a0\7\36\2\2\u009e\u00a0")
        buf.write("\7(\2\2\u009f\u009c\3\2\2\2\u009f\u009d\3\2\2\2\u009f")
        buf.write("\u009e\3\2\2\2\u00a0\21\3\2\2\2\u00a1\u00a2\7(\2\2\u00a2")
        buf.write("\u00a3\7\4\2\2\u00a3\u00a4\5\32\16\2\u00a4\u00a5\7\5\2")
        buf.write("\2\u00a5\u00a6\t\4\2\2\u00a6\23\3\2\2\2\u00a7\u00a8\7")
        buf.write("\b\2\2\u00a8\25\3\2\2\2\u00a9\u00aa\7\t\2\2\u00aa\27\3")
        buf.write("\2\2\2\u00ab\u00ac\7\n\2\2\u00ac\31\3\2\2\2\u00ad\u00ae")
        buf.write("\7\13\2\2\u00ae\33\3\2\2\2\u00af\u00b2\5\26\f\2\u00b0")
        buf.write("\u00b2\5\30\r\2\u00b1\u00af\3\2\2\2\u00b1\u00b0\3\2\2")
        buf.write("\2\u00b2\35\3\2\2\2\u00b3\u00b8\5\24\13\2\u00b4\u00b8")
        buf.write("\5\26\f\2\u00b5\u00b8\5\30\r\2\u00b6\u00b8\5\32\16\2\u00b7")
        buf.write("\u00b3\3\2\2\2\u00b7\u00b4\3\2\2\2\u00b7\u00b5\3\2\2\2")
        buf.write("\u00b7\u00b6\3\2\2\2\u00b8\37\3\2\2\2\u00b9\u00ba\7\f")
        buf.write("\2\2\u00ba!\3\2\2\2\u00bb\u00bc\7(\2\2\u00bc#\3\2\2\2")
        buf.write("\u00bd\u00be\5 \21\2\u00be\u00bf\5\"\22\2\u00bf\u00c1")
        buf.write("\7\6\2\2\u00c0\u00c2\5\b\5\2\u00c1\u00c0\3\2\2\2\u00c1")
        buf.write("\u00c2\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c4\7\7\2\2")
        buf.write("\u00c4\u00c8\7\r\2\2\u00c5\u00c7\5\62\32\2\u00c6\u00c5")
        buf.write("\3\2\2\2\u00c7\u00ca\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8")
        buf.write("\u00c9\3\2\2\2\u00c9\u00cb\3\2\2\2\u00ca\u00c8\3\2\2\2")
        buf.write("\u00cb\u00cc\7\16\2\2\u00cc%\3\2\2\2\u00cd\u00ce\5\"\22")
        buf.write("\2\u00ce\u00d0\7\6\2\2\u00cf\u00d1\5\6\4\2\u00d0\u00cf")
        buf.write("\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2")
        buf.write("\u00d3\7\7\2\2\u00d3\'\3\2\2\2\u00d4\u00d7\5,\27\2\u00d5")
        buf.write("\u00d7\5.\30\2\u00d6\u00d4\3\2\2\2\u00d6\u00d5\3\2\2\2")
        buf.write("\u00d7)\3\2\2\2\u00d8\u00d9\7\6\2\2\u00d9\u00de\5\60\31")
        buf.write("\2\u00da\u00db\7\3\2\2\u00db\u00dd\5\60\31\2\u00dc\u00da")
        buf.write("\3\2\2\2\u00dd\u00e0\3\2\2\2\u00de\u00dc\3\2\2\2\u00de")
        buf.write("\u00df\3\2\2\2\u00df\u00e1\3\2\2\2\u00e0\u00de\3\2\2\2")
        buf.write("\u00e1\u00e2\7\7\2\2\u00e2+\3\2\2\2\u00e3\u00e4\7\17\2")
        buf.write("\2\u00e4\u00e6\7\'\2\2\u00e5\u00e7\5*\26\2\u00e6\u00e5")
        buf.write("\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7-\3\2\2\2\u00e8\u00e9")
        buf.write("\5,\27\2\u00e9\u00ed\7\r\2\2\u00ea\u00ec\5\62\32\2\u00eb")
        buf.write("\u00ea\3\2\2\2\u00ec\u00ef\3\2\2\2\u00ed\u00eb\3\2\2\2")
        buf.write("\u00ed\u00ee\3\2\2\2\u00ee\u00f0\3\2\2\2\u00ef\u00ed\3")
        buf.write("\2\2\2\u00f0\u00f1\7\16\2\2\u00f1/\3\2\2\2\u00f2\u00f3")
        buf.write("\7(\2\2\u00f3\u00f4\7\4\2\2\u00f4\u00f5\5\36\20\2\u00f5")
        buf.write("\61\3\2\2\2\u00f6\u00ff\5`\61\2\u00f7\u00ff\5\66\34\2")
        buf.write("\u00f8\u00ff\5\60\31\2\u00f9\u00ff\5(\25\2\u00fa\u00ff")
        buf.write("\5$\23\2\u00fb\u00ff\5&\24\2\u00fc\u00ff\7)\2\2\u00fd")
        buf.write("\u00ff\7&\2\2\u00fe\u00f6\3\2\2\2\u00fe\u00f7\3\2\2\2")
        buf.write("\u00fe\u00f8\3\2\2\2\u00fe\u00f9\3\2\2\2\u00fe\u00fa\3")
        buf.write("\2\2\2\u00fe\u00fb\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00fd")
        buf.write("\3\2\2\2\u00ff\63\3\2\2\2\u0100\u0105\5`\61\2\u0101\u0105")
        buf.write("\5\66\34\2\u0102\u0105\5\60\31\2\u0103\u0105\5&\24\2\u0104")
        buf.write("\u0100\3\2\2\2\u0104\u0101\3\2\2\2\u0104\u0102\3\2\2\2")
        buf.write("\u0104\u0103\3\2\2\2\u0105\65\3\2\2\2\u0106\u010a\58\35")
        buf.write("\2\u0107\u010a\5> \2\u0108\u010a\5R*\2\u0109\u0106\3\2")
        buf.write("\2\2\u0109\u0107\3\2\2\2\u0109\u0108\3\2\2\2\u010a\67")
        buf.write("\3\2\2\2\u010b\u010e\5:\36\2\u010c\u010e\5<\37\2\u010d")
        buf.write("\u010b\3\2\2\2\u010d\u010c\3\2\2\2\u010e9\3\2\2\2\u010f")
        buf.write("\u0110\7\20\2\2\u0110\u0111\5L\'\2\u0111\u0115\7\r\2\2")
        buf.write("\u0112\u0114\5\62\32\2\u0113\u0112\3\2\2\2\u0114\u0117")
        buf.write("\3\2\2\2\u0115\u0113\3\2\2\2\u0115\u0116\3\2\2\2\u0116")
        buf.write("\u0118\3\2\2\2\u0117\u0115\3\2\2\2\u0118\u0119\7\16\2")
        buf.write("\2\u0119;\3\2\2\2\u011a\u011b\7\21\2\2\u011b\u011c\7(")
        buf.write("\2\2\u011c\u011d\7\22\2\2\u011d\u011e\7(\2\2\u011e\u0122")
        buf.write("\7\r\2\2\u011f\u0121\5\62\32\2\u0120\u011f\3\2\2\2\u0121")
        buf.write("\u0124\3\2\2\2\u0122\u0120\3\2\2\2\u0122\u0123\3\2\2\2")
        buf.write("\u0123\u0125\3\2\2\2\u0124\u0122\3\2\2\2\u0125\u0126\7")
        buf.write("\16\2\2\u0126=\3\2\2\2\u0127\u0129\5H%\2\u0128\u012a\5")
        buf.write("J&\2\u0129\u0128\3\2\2\2\u0129\u012a\3\2\2\2\u012a\u012d")
        buf.write("\3\2\2\2\u012b\u012d\5@!\2\u012c\u0127\3\2\2\2\u012c\u012b")
        buf.write("\3\2\2\2\u012d?\3\2\2\2\u012e\u012f\7\23\2\2\u012f\u0130")
        buf.write("\t\5\2\2\u0130\u0131\7\r\2\2\u0131\u0132\5B\"\2\u0132")
        buf.write("\u0133\7\16\2\2\u0133A\3\2\2\2\u0134\u0136\5D#\2\u0135")
        buf.write("\u0134\3\2\2\2\u0136\u0139\3\2\2\2\u0137\u0135\3\2\2\2")
        buf.write("\u0137\u0138\3\2\2\2\u0138\u013a\3\2\2\2\u0139\u0137\3")
        buf.write("\2\2\2\u013a\u013b\5F$\2\u013bC\3\2\2\2\u013c\u013f\7")
        buf.write("\24\2\2\u013d\u0140\7(\2\2\u013e\u0140\5L\'\2\u013f\u013d")
        buf.write("\3\2\2\2\u013f\u013e\3\2\2\2\u0140\u0141\3\2\2\2\u0141")
        buf.write("\u0145\7\r\2\2\u0142\u0144\5\64\33\2\u0143\u0142\3\2\2")
        buf.write("\2\u0144\u0147\3\2\2\2\u0145\u0143\3\2\2\2\u0145\u0146")
        buf.write("\3\2\2\2\u0146\u0148\3\2\2\2\u0147\u0145\3\2\2\2\u0148")
        buf.write("\u0149\7\16\2\2\u0149E\3\2\2\2\u014a\u014b\7\25\2\2\u014b")
        buf.write("\u014f\7\r\2\2\u014c\u014e\5\64\33\2\u014d\u014c\3\2\2")
        buf.write("\2\u014e\u0151\3\2\2\2\u014f\u014d\3\2\2\2\u014f\u0150")
        buf.write("\3\2\2\2\u0150\u0152\3\2\2\2\u0151\u014f\3\2\2\2\u0152")
        buf.write("\u0153\7\16\2\2\u0153G\3\2\2\2\u0154\u0155\7\26\2\2\u0155")
        buf.write("\u0156\5L\'\2\u0156\u015a\7\r\2\2\u0157\u0159\5\62\32")
        buf.write("\2\u0158\u0157\3\2\2\2\u0159\u015c\3\2\2\2\u015a\u0158")
        buf.write("\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u015d\3\2\2\2\u015c")
        buf.write("\u015a\3\2\2\2\u015d\u015e\7\16\2\2\u015eI\3\2\2\2\u015f")
        buf.write("\u0160\7\25\2\2\u0160\u0164\7\r\2\2\u0161\u0163\5\62\32")
        buf.write("\2\u0162\u0161\3\2\2\2\u0163\u0166\3\2\2\2\u0164\u0162")
        buf.write("\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0167\3\2\2\2\u0166")
        buf.write("\u0164\3\2\2\2\u0167\u0168\7\16\2\2\u0168K\3\2\2\2\u0169")
        buf.write("\u016a\5N(\2\u016a\u016b\5P)\2\u016b\u016c\5N(\2\u016c")
        buf.write("\u016f\3\2\2\2\u016d\u016f\7 \2\2\u016e\u0169\3\2\2\2")
        buf.write("\u016e\u016d\3\2\2\2\u016fM\3\2\2\2\u0170\u0175\7\35\2")
        buf.write("\2\u0171\u0175\7\36\2\2\u0172\u0175\7(\2\2\u0173\u0175")
        buf.write("\5R*\2\u0174\u0170\3\2\2\2\u0174\u0171\3\2\2\2\u0174\u0172")
        buf.write("\3\2\2\2\u0174\u0173\3\2\2\2\u0175O\3\2\2\2\u0176\u0177")
        buf.write("\t\6\2\2\u0177Q\3\2\2\2\u0178\u017b\5T+\2\u0179\u017b")
        buf.write("\5Z.\2\u017a\u0178\3\2\2\2\u017a\u0179\3\2\2\2\u017bS")
        buf.write("\3\2\2\2\u017c\u017f\5V,\2\u017d\u017f\5X-\2\u017e\u017c")
        buf.write("\3\2\2\2\u017e\u017d\3\2\2\2\u017fU\3\2\2\2\u0180\u0186")
        buf.write("\7\35\2\2\u0181\u0182\7\6\2\2\u0182\u0183\5T+\2\u0183")
        buf.write("\u0184\7\7\2\2\u0184\u0186\3\2\2\2\u0185\u0180\3\2\2\2")
        buf.write("\u0185\u0181\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u018e\t")
        buf.write("\7\2\2\u0188\u018f\7\35\2\2\u0189\u018f\5T+\2\u018a\u018b")
        buf.write("\7\6\2\2\u018b\u018c\5T+\2\u018c\u018d\7\7\2\2\u018d\u018f")
        buf.write("\3\2\2\2\u018e\u0188\3\2\2\2\u018e\u0189\3\2\2\2\u018e")
        buf.write("\u018a\3\2\2\2\u018fW\3\2\2\2\u0190\u0196\7\35\2\2\u0191")
        buf.write("\u0192\7\6\2\2\u0192\u0193\5T+\2\u0193\u0194\7\7\2\2\u0194")
        buf.write("\u0196\3\2\2\2\u0195\u0190\3\2\2\2\u0195\u0191\3\2\2\2")
        buf.write("\u0196\u0197\3\2\2\2\u0197\u019e\t\b\2\2\u0198\u019f\7")
        buf.write("\35\2\2\u0199\u019f\5T+\2\u019a\u019b\7\6\2\2\u019b\u019c")
        buf.write("\5T+\2\u019c\u019d\7\7\2\2\u019d\u019f\3\2\2\2\u019e\u0198")
        buf.write("\3\2\2\2\u019e\u0199\3\2\2\2\u019e\u019a\3\2\2\2\u019f")
        buf.write("Y\3\2\2\2\u01a0\u01a3\5^\60\2\u01a1\u01a3\5\\/\2\u01a2")
        buf.write("\u01a0\3\2\2\2\u01a2\u01a1\3\2\2\2\u01a3[\3\2\2\2\u01a4")
        buf.write("\u01a5\7\36\2\2\u01a5\u01a9\t\7\2\2\u01a6\u01aa\7\35\2")
        buf.write("\2\u01a7\u01aa\7\36\2\2\u01a8\u01aa\5\\/\2\u01a9\u01a6")
        buf.write("\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01a8\3\2\2\2\u01aa")
        buf.write("]\3\2\2\2\u01ab\u01ae\7\36\2\2\u01ac\u01ae\5\\/\2\u01ad")
        buf.write("\u01ab\3\2\2\2\u01ad\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2")
        buf.write("\u01af\u01b3\t\b\2\2\u01b0\u01b4\7\35\2\2\u01b1\u01b4")
        buf.write("\7\36\2\2\u01b2\u01b4\5^\60\2\u01b3\u01b0\3\2\2\2\u01b3")
        buf.write("\u01b1\3\2\2\2\u01b3\u01b2\3\2\2\2\u01b4_\3\2\2\2\u01b5")
        buf.write("\u01bb\5\n\6\2\u01b6\u01bb\5\f\7\2\u01b7\u01bb\5\20\t")
        buf.write("\2\u01b8\u01bb\5\16\b\2\u01b9\u01bb\5\22\n\2\u01ba\u01b5")
        buf.write("\3\2\2\2\u01ba\u01b6\3\2\2\2\u01ba\u01b7\3\2\2\2\u01ba")
        buf.write("\u01b8\3\2\2\2\u01ba\u01b9\3\2\2\2\u01bba\3\2\2\2\u01bc")
        buf.write("\u01bd\t\t\2\2\u01bdc\3\2\2\2,gs{\u0085\u0096\u009f\u00b1")
        buf.write("\u00b7\u00c1\u00c8\u00d0\u00d6\u00de\u00e6\u00ed\u00fe")
        buf.write("\u0104\u0109\u010d\u0115\u0122\u0129\u012c\u0137\u013f")
        buf.write("\u0145\u014f\u015a\u0164\u016e\u0174\u017a\u017e\u0185")
        buf.write("\u018e\u0195\u019e\u01a2\u01a9\u01ad\u01b3\u01ba")
        return buf.getvalue()


class pirParser ( Parser ):

    grammarFileName = "pir.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "':'", "'='", "'('", "')'", "'Boolean'", 
                     "'Integer'", "'Float'", "'Char'", "'ahoy'", "'{'", 
                     "'}'", "'class'", "'while'", "'for'", "'in'", "'switch'", 
                     "'case'", "'else'", "'if'", "'>'", "'<'", "'>='", "'<='", 
                     "'=='", "'!='", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IntegerLiteral", 
                      "FloatLiteral", "CharLiteral", "BooleanLiteral", "GeneralLiteral", 
                      "AdditionOperator", "SubtractionOperator", "MultiplicationOperator", 
                      "DivisionOperator", "NewLine", "ClassIdentifier", 
                      "Identifier", "Comment", "WS" ]

    RULE_start = 0
    RULE_generalArgument = 1
    RULE_generalArguments = 2
    RULE_typedArguments = 3
    RULE_classAssignment = 4
    RULE_booleanAssignment = 5
    RULE_integerAssignment = 6
    RULE_floatAssignment = 7
    RULE_charAssignment = 8
    RULE_booleanType = 9
    RULE_integerType = 10
    RULE_floatType = 11
    RULE_charType = 12
    RULE_numberType = 13
    RULE_genericType = 14
    RULE_functionKeyword = 15
    RULE_functionName = 16
    RULE_functionDeclaration = 17
    RULE_functionInvocation = 18
    RULE_classDeclaration = 19
    RULE_classConstructor = 20
    RULE_simpleClassDeclaration = 21
    RULE_completeClassDeclaration = 22
    RULE_typeDeclaration = 23
    RULE_generalDeclaration = 24
    RULE_generalInvocation = 25
    RULE_generalExpression = 26
    RULE_loopExpression = 27
    RULE_whileExpression = 28
    RULE_forExpression = 29
    RULE_controlExpression = 30
    RULE_switchCaseExpression = 31
    RULE_switchCaseBody = 32
    RULE_switchCaseCaseBranch = 33
    RULE_switchCaseElseBranch = 34
    RULE_ifExpression = 35
    RULE_elseExpression = 36
    RULE_comparisonExpression = 37
    RULE_comparisonOperand = 38
    RULE_comparisonOperator = 39
    RULE_algebraicExpression = 40
    RULE_integerAlgebraicExpression = 41
    RULE_integerMultiplicationExpression = 42
    RULE_integerSummationExpression = 43
    RULE_floatAlgebraicExpression = 44
    RULE_floatMultiplicationExpression = 45
    RULE_floatSummationExpression = 46
    RULE_generalAssignment = 47
    RULE_baseParameter = 48

    ruleNames =  [ "start", "generalArgument", "generalArguments", "typedArguments", 
                   "classAssignment", "booleanAssignment", "integerAssignment", 
                   "floatAssignment", "charAssignment", "booleanType", "integerType", 
                   "floatType", "charType", "numberType", "genericType", 
                   "functionKeyword", "functionName", "functionDeclaration", 
                   "functionInvocation", "classDeclaration", "classConstructor", 
                   "simpleClassDeclaration", "completeClassDeclaration", 
                   "typeDeclaration", "generalDeclaration", "generalInvocation", 
                   "generalExpression", "loopExpression", "whileExpression", 
                   "forExpression", "controlExpression", "switchCaseExpression", 
                   "switchCaseBody", "switchCaseCaseBranch", "switchCaseElseBranch", 
                   "ifExpression", "elseExpression", "comparisonExpression", 
                   "comparisonOperand", "comparisonOperator", "algebraicExpression", 
                   "integerAlgebraicExpression", "integerMultiplicationExpression", 
                   "integerSummationExpression", "floatAlgebraicExpression", 
                   "floatMultiplicationExpression", "floatSummationExpression", 
                   "generalAssignment", "baseParameter" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    IntegerLiteral=27
    FloatLiteral=28
    CharLiteral=29
    BooleanLiteral=30
    GeneralLiteral=31
    AdditionOperator=32
    SubtractionOperator=33
    MultiplicationOperator=34
    DivisionOperator=35
    NewLine=36
    ClassIdentifier=37
    Identifier=38
    Comment=39
    WS=40

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(pirParser.EOF, 0)

        def generalDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pirParser.GeneralDeclarationContext)
            else:
                return self.getTypedRuleContext(pirParser.GeneralDeclarationContext,i)


        def getRuleIndex(self):
            return pirParser.RULE_start

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = pirParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pirParser.T__3) | (1 << pirParser.T__9) | (1 << pirParser.T__12) | (1 << pirParser.T__13) | (1 << pirParser.T__14) | (1 << pirParser.T__16) | (1 << pirParser.T__19) | (1 << pirParser.IntegerLiteral) | (1 << pirParser.FloatLiteral) | (1 << pirParser.NewLine) | (1 << pirParser.Identifier) | (1 << pirParser.Comment))) != 0):
                self.state = 98
                self.generalDeclaration()
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 104
            self.match(pirParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GeneralArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(pirParser.Identifier, 0)

        def BooleanLiteral(self):
            return self.getToken(pirParser.BooleanLiteral, 0)

        def CharLiteral(self):
            return self.getToken(pirParser.CharLiteral, 0)

        def FloatLiteral(self):
            return self.getToken(pirParser.FloatLiteral, 0)

        def IntegerLiteral(self):
            return self.getToken(pirParser.IntegerLiteral, 0)

        def getRuleIndex(self):
            return pirParser.RULE_generalArgument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGeneralArgument" ):
                return visitor.visitGeneralArgument(self)
            else:
                return visitor.visitChildren(self)




    def generalArgument(self):

        localctx = pirParser.GeneralArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_generalArgument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pirParser.IntegerLiteral) | (1 << pirParser.FloatLiteral) | (1 << pirParser.CharLiteral) | (1 << pirParser.BooleanLiteral) | (1 << pirParser.Identifier))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GeneralArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def generalArgument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pirParser.GeneralArgumentContext)
            else:
                return self.getTypedRuleContext(pirParser.GeneralArgumentContext,i)


        def getRuleIndex(self):
            return pirParser.RULE_generalArguments

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGeneralArguments" ):
                return visitor.visitGeneralArguments(self)
            else:
                return visitor.visitChildren(self)




    def generalArguments(self):

        localctx = pirParser.GeneralArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_generalArguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.generalArgument()
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==pirParser.T__0:
                self.state = 109
                self.match(pirParser.T__0)
                self.state = 110
                self.generalArgument()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pirParser.TypeDeclarationContext)
            else:
                return self.getTypedRuleContext(pirParser.TypeDeclarationContext,i)


        def getRuleIndex(self):
            return pirParser.RULE_typedArguments

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypedArguments" ):
                return visitor.visitTypedArguments(self)
            else:
                return visitor.visitChildren(self)




    def typedArguments(self):

        localctx = pirParser.TypedArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_typedArguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.typeDeclaration()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==pirParser.T__0:
                self.state = 117
                self.match(pirParser.T__0)
                self.state = 118
                self.typeDeclaration()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(pirParser.Identifier, 0)

        def ClassIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(pirParser.ClassIdentifier)
            else:
                return self.getToken(pirParser.ClassIdentifier, i)

        def generalArguments(self):
            return self.getTypedRuleContext(pirParser.GeneralArgumentsContext,0)


        def getRuleIndex(self):
            return pirParser.RULE_classAssignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassAssignment" ):
                return visitor.visitClassAssignment(self)
            else:
                return visitor.visitChildren(self)




    def classAssignment(self):

        localctx = pirParser.ClassAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_classAssignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(pirParser.Identifier)
            self.state = 125
            self.match(pirParser.T__1)
            self.state = 126
            self.match(pirParser.ClassIdentifier)
            self.state = 127
            self.match(pirParser.T__2)
            self.state = 128
            self.match(pirParser.ClassIdentifier)
            self.state = 129
            self.match(pirParser.T__3)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pirParser.IntegerLiteral) | (1 << pirParser.FloatLiteral) | (1 << pirParser.CharLiteral) | (1 << pirParser.BooleanLiteral) | (1 << pirParser.Identifier))) != 0):
                self.state = 130
                self.generalArguments()


            self.state = 133
            self.match(pirParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(pirParser.Identifier)
            else:
                return self.getToken(pirParser.Identifier, i)

        def booleanType(self):
            return self.getTypedRuleContext(pirParser.BooleanTypeContext,0)


        def BooleanLiteral(self):
            return self.getToken(pirParser.BooleanLiteral, 0)

        def getRuleIndex(self):
            return pirParser.RULE_booleanAssignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanAssignment" ):
                return visitor.visitBooleanAssignment(self)
            else:
                return visitor.visitChildren(self)




    def booleanAssignment(self):

        localctx = pirParser.BooleanAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_booleanAssignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(pirParser.Identifier)
            self.state = 136
            self.match(pirParser.T__1)
            self.state = 137
            self.booleanType()
            self.state = 138
            self.match(pirParser.T__2)
            self.state = 139
            _la = self._input.LA(1)
            if not(_la==pirParser.BooleanLiteral or _la==pirParser.Identifier):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(pirParser.Identifier)
            else:
                return self.getToken(pirParser.Identifier, i)

        def integerType(self):
            return self.getTypedRuleContext(pirParser.IntegerTypeContext,0)


        def integerAlgebraicExpression(self):
            return self.getTypedRuleContext(pirParser.IntegerAlgebraicExpressionContext,0)


        def IntegerLiteral(self):
            return self.getToken(pirParser.IntegerLiteral, 0)

        def getRuleIndex(self):
            return pirParser.RULE_integerAssignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntegerAssignment" ):
                return visitor.visitIntegerAssignment(self)
            else:
                return visitor.visitChildren(self)




    def integerAssignment(self):

        localctx = pirParser.IntegerAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_integerAssignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(pirParser.Identifier)
            self.state = 142
            self.match(pirParser.T__1)
            self.state = 143
            self.integerType()
            self.state = 144
            self.match(pirParser.T__2)
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 145
                self.integerAlgebraicExpression()
                pass

            elif la_ == 2:
                self.state = 146
                self.match(pirParser.IntegerLiteral)
                pass

            elif la_ == 3:
                self.state = 147
                self.match(pirParser.Identifier)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(pirParser.Identifier)
            else:
                return self.getToken(pirParser.Identifier, i)

        def floatType(self):
            return self.getTypedRuleContext(pirParser.FloatTypeContext,0)


        def floatAlgebraicExpression(self):
            return self.getTypedRuleContext(pirParser.FloatAlgebraicExpressionContext,0)


        def FloatLiteral(self):
            return self.getToken(pirParser.FloatLiteral, 0)

        def getRuleIndex(self):
            return pirParser.RULE_floatAssignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatAssignment" ):
                return visitor.visitFloatAssignment(self)
            else:
                return visitor.visitChildren(self)




    def floatAssignment(self):

        localctx = pirParser.FloatAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_floatAssignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(pirParser.Identifier)
            self.state = 151
            self.match(pirParser.T__1)
            self.state = 152
            self.floatType()
            self.state = 153
            self.match(pirParser.T__2)
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 154
                self.floatAlgebraicExpression()
                pass

            elif la_ == 2:
                self.state = 155
                self.match(pirParser.FloatLiteral)
                pass

            elif la_ == 3:
                self.state = 156
                self.match(pirParser.Identifier)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(pirParser.Identifier)
            else:
                return self.getToken(pirParser.Identifier, i)

        def charType(self):
            return self.getTypedRuleContext(pirParser.CharTypeContext,0)


        def CharLiteral(self):
            return self.getToken(pirParser.CharLiteral, 0)

        def getRuleIndex(self):
            return pirParser.RULE_charAssignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharAssignment" ):
                return visitor.visitCharAssignment(self)
            else:
                return visitor.visitChildren(self)




    def charAssignment(self):

        localctx = pirParser.CharAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_charAssignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(pirParser.Identifier)
            self.state = 160
            self.match(pirParser.T__1)
            self.state = 161
            self.charType()
            self.state = 162
            self.match(pirParser.T__2)
            self.state = 163
            _la = self._input.LA(1)
            if not(_la==pirParser.CharLiteral or _la==pirParser.Identifier):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pirParser.RULE_booleanType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanType" ):
                return visitor.visitBooleanType(self)
            else:
                return visitor.visitChildren(self)




    def booleanType(self):

        localctx = pirParser.BooleanTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_booleanType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(pirParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pirParser.RULE_integerType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntegerType" ):
                return visitor.visitIntegerType(self)
            else:
                return visitor.visitChildren(self)




    def integerType(self):

        localctx = pirParser.IntegerTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_integerType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(pirParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pirParser.RULE_floatType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatType" ):
                return visitor.visitFloatType(self)
            else:
                return visitor.visitChildren(self)




    def floatType(self):

        localctx = pirParser.FloatTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_floatType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(pirParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pirParser.RULE_charType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharType" ):
                return visitor.visitCharType(self)
            else:
                return visitor.visitChildren(self)




    def charType(self):

        localctx = pirParser.CharTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_charType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(pirParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integerType(self):
            return self.getTypedRuleContext(pirParser.IntegerTypeContext,0)


        def floatType(self):
            return self.getTypedRuleContext(pirParser.FloatTypeContext,0)


        def getRuleIndex(self):
            return pirParser.RULE_numberType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberType" ):
                return visitor.visitNumberType(self)
            else:
                return visitor.visitChildren(self)




    def numberType(self):

        localctx = pirParser.NumberTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_numberType)
        try:
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pirParser.T__6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.integerType()
                pass
            elif token in [pirParser.T__7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.floatType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GenericTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def booleanType(self):
            return self.getTypedRuleContext(pirParser.BooleanTypeContext,0)


        def integerType(self):
            return self.getTypedRuleContext(pirParser.IntegerTypeContext,0)


        def floatType(self):
            return self.getTypedRuleContext(pirParser.FloatTypeContext,0)


        def charType(self):
            return self.getTypedRuleContext(pirParser.CharTypeContext,0)


        def getRuleIndex(self):
            return pirParser.RULE_genericType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGenericType" ):
                return visitor.visitGenericType(self)
            else:
                return visitor.visitChildren(self)




    def genericType(self):

        localctx = pirParser.GenericTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_genericType)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pirParser.T__5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.booleanType()
                pass
            elif token in [pirParser.T__6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.integerType()
                pass
            elif token in [pirParser.T__7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 179
                self.floatType()
                pass
            elif token in [pirParser.T__8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 180
                self.charType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionKeywordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pirParser.RULE_functionKeyword

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionKeyword" ):
                return visitor.visitFunctionKeyword(self)
            else:
                return visitor.visitChildren(self)




    def functionKeyword(self):

        localctx = pirParser.FunctionKeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_functionKeyword)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(pirParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(pirParser.Identifier, 0)

        def getRuleIndex(self):
            return pirParser.RULE_functionName

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionName" ):
                return visitor.visitFunctionName(self)
            else:
                return visitor.visitChildren(self)




    def functionName(self):

        localctx = pirParser.FunctionNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_functionName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(pirParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionKeyword(self):
            return self.getTypedRuleContext(pirParser.FunctionKeywordContext,0)


        def functionName(self):
            return self.getTypedRuleContext(pirParser.FunctionNameContext,0)


        def typedArguments(self):
            return self.getTypedRuleContext(pirParser.TypedArgumentsContext,0)


        def generalDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pirParser.GeneralDeclarationContext)
            else:
                return self.getTypedRuleContext(pirParser.GeneralDeclarationContext,i)


        def getRuleIndex(self):
            return pirParser.RULE_functionDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclaration" ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclaration(self):

        localctx = pirParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.functionKeyword()
            self.state = 188
            self.functionName()
            self.state = 189
            self.match(pirParser.T__3)
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==pirParser.Identifier:
                self.state = 190
                self.typedArguments()


            self.state = 193
            self.match(pirParser.T__4)
            self.state = 194
            self.match(pirParser.T__10)
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pirParser.T__3) | (1 << pirParser.T__9) | (1 << pirParser.T__12) | (1 << pirParser.T__13) | (1 << pirParser.T__14) | (1 << pirParser.T__16) | (1 << pirParser.T__19) | (1 << pirParser.IntegerLiteral) | (1 << pirParser.FloatLiteral) | (1 << pirParser.NewLine) | (1 << pirParser.Identifier) | (1 << pirParser.Comment))) != 0):
                self.state = 195
                self.generalDeclaration()
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 201
            self.match(pirParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionInvocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionName(self):
            return self.getTypedRuleContext(pirParser.FunctionNameContext,0)


        def generalArguments(self):
            return self.getTypedRuleContext(pirParser.GeneralArgumentsContext,0)


        def getRuleIndex(self):
            return pirParser.RULE_functionInvocation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionInvocation" ):
                return visitor.visitFunctionInvocation(self)
            else:
                return visitor.visitChildren(self)




    def functionInvocation(self):

        localctx = pirParser.FunctionInvocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_functionInvocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.functionName()
            self.state = 204
            self.match(pirParser.T__3)
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pirParser.IntegerLiteral) | (1 << pirParser.FloatLiteral) | (1 << pirParser.CharLiteral) | (1 << pirParser.BooleanLiteral) | (1 << pirParser.Identifier))) != 0):
                self.state = 205
                self.generalArguments()


            self.state = 208
            self.match(pirParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleClassDeclaration(self):
            return self.getTypedRuleContext(pirParser.SimpleClassDeclarationContext,0)


        def completeClassDeclaration(self):
            return self.getTypedRuleContext(pirParser.CompleteClassDeclarationContext,0)


        def getRuleIndex(self):
            return pirParser.RULE_classDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDeclaration" ):
                return visitor.visitClassDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def classDeclaration(self):

        localctx = pirParser.ClassDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_classDeclaration)
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.simpleClassDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.completeClassDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassConstructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pirParser.TypeDeclarationContext)
            else:
                return self.getTypedRuleContext(pirParser.TypeDeclarationContext,i)


        def getRuleIndex(self):
            return pirParser.RULE_classConstructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassConstructor" ):
                return visitor.visitClassConstructor(self)
            else:
                return visitor.visitChildren(self)




    def classConstructor(self):

        localctx = pirParser.ClassConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_classConstructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(pirParser.T__3)
            self.state = 215
            self.typeDeclaration()
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==pirParser.T__0:
                self.state = 216
                self.match(pirParser.T__0)
                self.state = 217
                self.typeDeclaration()
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 223
            self.match(pirParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleClassDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ClassIdentifier(self):
            return self.getToken(pirParser.ClassIdentifier, 0)

        def classConstructor(self):
            return self.getTypedRuleContext(pirParser.ClassConstructorContext,0)


        def getRuleIndex(self):
            return pirParser.RULE_simpleClassDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleClassDeclaration" ):
                return visitor.visitSimpleClassDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def simpleClassDeclaration(self):

        localctx = pirParser.SimpleClassDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_simpleClassDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(pirParser.T__12)
            self.state = 226
            self.match(pirParser.ClassIdentifier)
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 227
                self.classConstructor()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompleteClassDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleClassDeclaration(self):
            return self.getTypedRuleContext(pirParser.SimpleClassDeclarationContext,0)


        def generalDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pirParser.GeneralDeclarationContext)
            else:
                return self.getTypedRuleContext(pirParser.GeneralDeclarationContext,i)


        def getRuleIndex(self):
            return pirParser.RULE_completeClassDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompleteClassDeclaration" ):
                return visitor.visitCompleteClassDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def completeClassDeclaration(self):

        localctx = pirParser.CompleteClassDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_completeClassDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.simpleClassDeclaration()
            self.state = 231
            self.match(pirParser.T__10)
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pirParser.T__3) | (1 << pirParser.T__9) | (1 << pirParser.T__12) | (1 << pirParser.T__13) | (1 << pirParser.T__14) | (1 << pirParser.T__16) | (1 << pirParser.T__19) | (1 << pirParser.IntegerLiteral) | (1 << pirParser.FloatLiteral) | (1 << pirParser.NewLine) | (1 << pirParser.Identifier) | (1 << pirParser.Comment))) != 0):
                self.state = 232
                self.generalDeclaration()
                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 238
            self.match(pirParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(pirParser.Identifier, 0)

        def genericType(self):
            return self.getTypedRuleContext(pirParser.GenericTypeContext,0)


        def getRuleIndex(self):
            return pirParser.RULE_typeDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeDeclaration" ):
                return visitor.visitTypeDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def typeDeclaration(self):

        localctx = pirParser.TypeDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_typeDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(pirParser.Identifier)
            self.state = 241
            self.match(pirParser.T__1)
            self.state = 242
            self.genericType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GeneralDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def generalAssignment(self):
            return self.getTypedRuleContext(pirParser.GeneralAssignmentContext,0)


        def generalExpression(self):
            return self.getTypedRuleContext(pirParser.GeneralExpressionContext,0)


        def typeDeclaration(self):
            return self.getTypedRuleContext(pirParser.TypeDeclarationContext,0)


        def classDeclaration(self):
            return self.getTypedRuleContext(pirParser.ClassDeclarationContext,0)


        def functionDeclaration(self):
            return self.getTypedRuleContext(pirParser.FunctionDeclarationContext,0)


        def functionInvocation(self):
            return self.getTypedRuleContext(pirParser.FunctionInvocationContext,0)


        def Comment(self):
            return self.getToken(pirParser.Comment, 0)

        def NewLine(self):
            return self.getToken(pirParser.NewLine, 0)

        def getRuleIndex(self):
            return pirParser.RULE_generalDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGeneralDeclaration" ):
                return visitor.visitGeneralDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def generalDeclaration(self):

        localctx = pirParser.GeneralDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_generalDeclaration)
        try:
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.generalAssignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.generalExpression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 246
                self.typeDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 247
                self.classDeclaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 248
                self.functionDeclaration()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 249
                self.functionInvocation()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 250
                self.match(pirParser.Comment)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 251
                self.match(pirParser.NewLine)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GeneralInvocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def generalAssignment(self):
            return self.getTypedRuleContext(pirParser.GeneralAssignmentContext,0)


        def generalExpression(self):
            return self.getTypedRuleContext(pirParser.GeneralExpressionContext,0)


        def typeDeclaration(self):
            return self.getTypedRuleContext(pirParser.TypeDeclarationContext,0)


        def functionInvocation(self):
            return self.getTypedRuleContext(pirParser.FunctionInvocationContext,0)


        def getRuleIndex(self):
            return pirParser.RULE_generalInvocation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGeneralInvocation" ):
                return visitor.visitGeneralInvocation(self)
            else:
                return visitor.visitChildren(self)




    def generalInvocation(self):

        localctx = pirParser.GeneralInvocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_generalInvocation)
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.generalAssignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.generalExpression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 256
                self.typeDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 257
                self.functionInvocation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GeneralExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loopExpression(self):
            return self.getTypedRuleContext(pirParser.LoopExpressionContext,0)


        def controlExpression(self):
            return self.getTypedRuleContext(pirParser.ControlExpressionContext,0)


        def algebraicExpression(self):
            return self.getTypedRuleContext(pirParser.AlgebraicExpressionContext,0)


        def getRuleIndex(self):
            return pirParser.RULE_generalExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGeneralExpression" ):
                return visitor.visitGeneralExpression(self)
            else:
                return visitor.visitChildren(self)




    def generalExpression(self):

        localctx = pirParser.GeneralExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_generalExpression)
        try:
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pirParser.T__13, pirParser.T__14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.loopExpression()
                pass
            elif token in [pirParser.T__16, pirParser.T__19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
                self.controlExpression()
                pass
            elif token in [pirParser.T__3, pirParser.IntegerLiteral, pirParser.FloatLiteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 262
                self.algebraicExpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def whileExpression(self):
            return self.getTypedRuleContext(pirParser.WhileExpressionContext,0)


        def forExpression(self):
            return self.getTypedRuleContext(pirParser.ForExpressionContext,0)


        def getRuleIndex(self):
            return pirParser.RULE_loopExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopExpression" ):
                return visitor.visitLoopExpression(self)
            else:
                return visitor.visitChildren(self)




    def loopExpression(self):

        localctx = pirParser.LoopExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_loopExpression)
        try:
            self.state = 267
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pirParser.T__13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.whileExpression()
                pass
            elif token in [pirParser.T__14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
                self.forExpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.cond = None # ComparisonExpressionContext

        def comparisonExpression(self):
            return self.getTypedRuleContext(pirParser.ComparisonExpressionContext,0)


        def generalDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pirParser.GeneralDeclarationContext)
            else:
                return self.getTypedRuleContext(pirParser.GeneralDeclarationContext,i)


        def getRuleIndex(self):
            return pirParser.RULE_whileExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileExpression" ):
                return visitor.visitWhileExpression(self)
            else:
                return visitor.visitChildren(self)




    def whileExpression(self):

        localctx = pirParser.WhileExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_whileExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(pirParser.T__13)
            self.state = 270
            localctx.cond = self.comparisonExpression()
            self.state = 271
            self.match(pirParser.T__10)
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pirParser.T__3) | (1 << pirParser.T__9) | (1 << pirParser.T__12) | (1 << pirParser.T__13) | (1 << pirParser.T__14) | (1 << pirParser.T__16) | (1 << pirParser.T__19) | (1 << pirParser.IntegerLiteral) | (1 << pirParser.FloatLiteral) | (1 << pirParser.NewLine) | (1 << pirParser.Identifier) | (1 << pirParser.Comment))) != 0):
                self.state = 272
                self.generalDeclaration()
                self.state = 277
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 278
            self.match(pirParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(pirParser.Identifier)
            else:
                return self.getToken(pirParser.Identifier, i)

        def generalDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pirParser.GeneralDeclarationContext)
            else:
                return self.getTypedRuleContext(pirParser.GeneralDeclarationContext,i)


        def getRuleIndex(self):
            return pirParser.RULE_forExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForExpression" ):
                return visitor.visitForExpression(self)
            else:
                return visitor.visitChildren(self)




    def forExpression(self):

        localctx = pirParser.ForExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_forExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(pirParser.T__14)
            self.state = 281
            self.match(pirParser.Identifier)
            self.state = 282
            self.match(pirParser.T__15)
            self.state = 283
            self.match(pirParser.Identifier)
            self.state = 284
            self.match(pirParser.T__10)
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pirParser.T__3) | (1 << pirParser.T__9) | (1 << pirParser.T__12) | (1 << pirParser.T__13) | (1 << pirParser.T__14) | (1 << pirParser.T__16) | (1 << pirParser.T__19) | (1 << pirParser.IntegerLiteral) | (1 << pirParser.FloatLiteral) | (1 << pirParser.NewLine) | (1 << pirParser.Identifier) | (1 << pirParser.Comment))) != 0):
                self.state = 285
                self.generalDeclaration()
                self.state = 290
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 291
            self.match(pirParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ControlExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifExpression(self):
            return self.getTypedRuleContext(pirParser.IfExpressionContext,0)


        def elseExpression(self):
            return self.getTypedRuleContext(pirParser.ElseExpressionContext,0)


        def switchCaseExpression(self):
            return self.getTypedRuleContext(pirParser.SwitchCaseExpressionContext,0)


        def getRuleIndex(self):
            return pirParser.RULE_controlExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitControlExpression" ):
                return visitor.visitControlExpression(self)
            else:
                return visitor.visitChildren(self)




    def controlExpression(self):

        localctx = pirParser.ControlExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_controlExpression)
        self._la = 0 # Token type
        try:
            self.state = 298
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pirParser.T__19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.ifExpression()
                self.state = 295
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==pirParser.T__18:
                    self.state = 294
                    self.elseExpression()


                pass
            elif token in [pirParser.T__16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.switchCaseExpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchCaseExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def switchCaseBody(self):
            return self.getTypedRuleContext(pirParser.SwitchCaseBodyContext,0)


        def Identifier(self):
            return self.getToken(pirParser.Identifier, 0)

        def GeneralLiteral(self):
            return self.getToken(pirParser.GeneralLiteral, 0)

        def getRuleIndex(self):
            return pirParser.RULE_switchCaseExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchCaseExpression" ):
                return visitor.visitSwitchCaseExpression(self)
            else:
                return visitor.visitChildren(self)




    def switchCaseExpression(self):

        localctx = pirParser.SwitchCaseExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_switchCaseExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(pirParser.T__16)
            self.state = 301
            _la = self._input.LA(1)
            if not(_la==pirParser.GeneralLiteral or _la==pirParser.Identifier):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 302
            self.match(pirParser.T__10)
            self.state = 303
            self.switchCaseBody()
            self.state = 304
            self.match(pirParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchCaseBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def switchCaseElseBranch(self):
            return self.getTypedRuleContext(pirParser.SwitchCaseElseBranchContext,0)


        def switchCaseCaseBranch(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pirParser.SwitchCaseCaseBranchContext)
            else:
                return self.getTypedRuleContext(pirParser.SwitchCaseCaseBranchContext,i)


        def getRuleIndex(self):
            return pirParser.RULE_switchCaseBody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchCaseBody" ):
                return visitor.visitSwitchCaseBody(self)
            else:
                return visitor.visitChildren(self)




    def switchCaseBody(self):

        localctx = pirParser.SwitchCaseBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_switchCaseBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==pirParser.T__17:
                self.state = 306
                self.switchCaseCaseBranch()
                self.state = 311
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 312
            self.switchCaseElseBranch()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchCaseCaseBranchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(pirParser.Identifier, 0)

        def comparisonExpression(self):
            return self.getTypedRuleContext(pirParser.ComparisonExpressionContext,0)


        def generalInvocation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pirParser.GeneralInvocationContext)
            else:
                return self.getTypedRuleContext(pirParser.GeneralInvocationContext,i)


        def getRuleIndex(self):
            return pirParser.RULE_switchCaseCaseBranch

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchCaseCaseBranch" ):
                return visitor.visitSwitchCaseCaseBranch(self)
            else:
                return visitor.visitChildren(self)




    def switchCaseCaseBranch(self):

        localctx = pirParser.SwitchCaseCaseBranchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_switchCaseCaseBranch)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(pirParser.T__17)
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 315
                self.match(pirParser.Identifier)
                pass

            elif la_ == 2:
                self.state = 316
                self.comparisonExpression()
                pass


            self.state = 319
            self.match(pirParser.T__10)
            self.state = 323
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pirParser.T__3) | (1 << pirParser.T__13) | (1 << pirParser.T__14) | (1 << pirParser.T__16) | (1 << pirParser.T__19) | (1 << pirParser.IntegerLiteral) | (1 << pirParser.FloatLiteral) | (1 << pirParser.Identifier))) != 0):
                self.state = 320
                self.generalInvocation()
                self.state = 325
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 326
            self.match(pirParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchCaseElseBranchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def generalInvocation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pirParser.GeneralInvocationContext)
            else:
                return self.getTypedRuleContext(pirParser.GeneralInvocationContext,i)


        def getRuleIndex(self):
            return pirParser.RULE_switchCaseElseBranch

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchCaseElseBranch" ):
                return visitor.visitSwitchCaseElseBranch(self)
            else:
                return visitor.visitChildren(self)




    def switchCaseElseBranch(self):

        localctx = pirParser.SwitchCaseElseBranchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_switchCaseElseBranch)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(pirParser.T__18)
            self.state = 329
            self.match(pirParser.T__10)
            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pirParser.T__3) | (1 << pirParser.T__13) | (1 << pirParser.T__14) | (1 << pirParser.T__16) | (1 << pirParser.T__19) | (1 << pirParser.IntegerLiteral) | (1 << pirParser.FloatLiteral) | (1 << pirParser.Identifier))) != 0):
                self.state = 330
                self.generalInvocation()
                self.state = 335
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 336
            self.match(pirParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.cond = None # ComparisonExpressionContext

        def comparisonExpression(self):
            return self.getTypedRuleContext(pirParser.ComparisonExpressionContext,0)


        def generalDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pirParser.GeneralDeclarationContext)
            else:
                return self.getTypedRuleContext(pirParser.GeneralDeclarationContext,i)


        def getRuleIndex(self):
            return pirParser.RULE_ifExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfExpression" ):
                return visitor.visitIfExpression(self)
            else:
                return visitor.visitChildren(self)




    def ifExpression(self):

        localctx = pirParser.IfExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_ifExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(pirParser.T__19)
            self.state = 339
            localctx.cond = self.comparisonExpression()
            self.state = 340
            self.match(pirParser.T__10)
            self.state = 344
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pirParser.T__3) | (1 << pirParser.T__9) | (1 << pirParser.T__12) | (1 << pirParser.T__13) | (1 << pirParser.T__14) | (1 << pirParser.T__16) | (1 << pirParser.T__19) | (1 << pirParser.IntegerLiteral) | (1 << pirParser.FloatLiteral) | (1 << pirParser.NewLine) | (1 << pirParser.Identifier) | (1 << pirParser.Comment))) != 0):
                self.state = 341
                self.generalDeclaration()
                self.state = 346
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 347
            self.match(pirParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def generalDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pirParser.GeneralDeclarationContext)
            else:
                return self.getTypedRuleContext(pirParser.GeneralDeclarationContext,i)


        def getRuleIndex(self):
            return pirParser.RULE_elseExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseExpression" ):
                return visitor.visitElseExpression(self)
            else:
                return visitor.visitChildren(self)




    def elseExpression(self):

        localctx = pirParser.ElseExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_elseExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(pirParser.T__18)
            self.state = 350
            self.match(pirParser.T__10)
            self.state = 354
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pirParser.T__3) | (1 << pirParser.T__9) | (1 << pirParser.T__12) | (1 << pirParser.T__13) | (1 << pirParser.T__14) | (1 << pirParser.T__16) | (1 << pirParser.T__19) | (1 << pirParser.IntegerLiteral) | (1 << pirParser.FloatLiteral) | (1 << pirParser.NewLine) | (1 << pirParser.Identifier) | (1 << pirParser.Comment))) != 0):
                self.state = 351
                self.generalDeclaration()
                self.state = 356
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 357
            self.match(pirParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparisonOperand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pirParser.ComparisonOperandContext)
            else:
                return self.getTypedRuleContext(pirParser.ComparisonOperandContext,i)


        def comparisonOperator(self):
            return self.getTypedRuleContext(pirParser.ComparisonOperatorContext,0)


        def BooleanLiteral(self):
            return self.getToken(pirParser.BooleanLiteral, 0)

        def getRuleIndex(self):
            return pirParser.RULE_comparisonExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonExpression" ):
                return visitor.visitComparisonExpression(self)
            else:
                return visitor.visitChildren(self)




    def comparisonExpression(self):

        localctx = pirParser.ComparisonExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_comparisonExpression)
        try:
            self.state = 364
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pirParser.T__3, pirParser.IntegerLiteral, pirParser.FloatLiteral, pirParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.comparisonOperand()
                self.state = 360
                self.comparisonOperator()
                self.state = 361
                self.comparisonOperand()
                pass
            elif token in [pirParser.BooleanLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
                self.match(pirParser.BooleanLiteral)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonOperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IntegerLiteral(self):
            return self.getToken(pirParser.IntegerLiteral, 0)

        def FloatLiteral(self):
            return self.getToken(pirParser.FloatLiteral, 0)

        def Identifier(self):
            return self.getToken(pirParser.Identifier, 0)

        def algebraicExpression(self):
            return self.getTypedRuleContext(pirParser.AlgebraicExpressionContext,0)


        def getRuleIndex(self):
            return pirParser.RULE_comparisonOperand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonOperand" ):
                return visitor.visitComparisonOperand(self)
            else:
                return visitor.visitChildren(self)




    def comparisonOperand(self):

        localctx = pirParser.ComparisonOperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_comparisonOperand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 366
                self.match(pirParser.IntegerLiteral)
                pass

            elif la_ == 2:
                self.state = 367
                self.match(pirParser.FloatLiteral)
                pass

            elif la_ == 3:
                self.state = 368
                self.match(pirParser.Identifier)
                pass

            elif la_ == 4:
                self.state = 369
                self.algebraicExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pirParser.RULE_comparisonOperator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonOperator" ):
                return visitor.visitComparisonOperator(self)
            else:
                return visitor.visitChildren(self)




    def comparisonOperator(self):

        localctx = pirParser.ComparisonOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_comparisonOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pirParser.T__20) | (1 << pirParser.T__21) | (1 << pirParser.T__22) | (1 << pirParser.T__23) | (1 << pirParser.T__24) | (1 << pirParser.T__25))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AlgebraicExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integerAlgebraicExpression(self):
            return self.getTypedRuleContext(pirParser.IntegerAlgebraicExpressionContext,0)


        def floatAlgebraicExpression(self):
            return self.getTypedRuleContext(pirParser.FloatAlgebraicExpressionContext,0)


        def getRuleIndex(self):
            return pirParser.RULE_algebraicExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlgebraicExpression" ):
                return visitor.visitAlgebraicExpression(self)
            else:
                return visitor.visitChildren(self)




    def algebraicExpression(self):

        localctx = pirParser.AlgebraicExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_algebraicExpression)
        try:
            self.state = 376
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pirParser.T__3, pirParser.IntegerLiteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.integerAlgebraicExpression()
                pass
            elif token in [pirParser.FloatLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
                self.floatAlgebraicExpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerAlgebraicExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integerMultiplicationExpression(self):
            return self.getTypedRuleContext(pirParser.IntegerMultiplicationExpressionContext,0)


        def integerSummationExpression(self):
            return self.getTypedRuleContext(pirParser.IntegerSummationExpressionContext,0)


        def getRuleIndex(self):
            return pirParser.RULE_integerAlgebraicExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntegerAlgebraicExpression" ):
                return visitor.visitIntegerAlgebraicExpression(self)
            else:
                return visitor.visitChildren(self)




    def integerAlgebraicExpression(self):

        localctx = pirParser.IntegerAlgebraicExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_integerAlgebraicExpression)
        try:
            self.state = 380
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 378
                self.integerMultiplicationExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 379
                self.integerSummationExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerMultiplicationExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MultiplicationOperator(self):
            return self.getToken(pirParser.MultiplicationOperator, 0)

        def DivisionOperator(self):
            return self.getToken(pirParser.DivisionOperator, 0)

        def IntegerLiteral(self, i:int=None):
            if i is None:
                return self.getTokens(pirParser.IntegerLiteral)
            else:
                return self.getToken(pirParser.IntegerLiteral, i)

        def integerAlgebraicExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pirParser.IntegerAlgebraicExpressionContext)
            else:
                return self.getTypedRuleContext(pirParser.IntegerAlgebraicExpressionContext,i)


        def getRuleIndex(self):
            return pirParser.RULE_integerMultiplicationExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntegerMultiplicationExpression" ):
                return visitor.visitIntegerMultiplicationExpression(self)
            else:
                return visitor.visitChildren(self)




    def integerMultiplicationExpression(self):

        localctx = pirParser.IntegerMultiplicationExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_integerMultiplicationExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pirParser.IntegerLiteral]:
                self.state = 382
                self.match(pirParser.IntegerLiteral)
                pass
            elif token in [pirParser.T__3]:
                self.state = 383
                self.match(pirParser.T__3)
                self.state = 384
                self.integerAlgebraicExpression()
                self.state = 385
                self.match(pirParser.T__4)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 389
            _la = self._input.LA(1)
            if not(_la==pirParser.MultiplicationOperator or _la==pirParser.DivisionOperator):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 396
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 390
                self.match(pirParser.IntegerLiteral)
                pass

            elif la_ == 2:
                self.state = 391
                self.integerAlgebraicExpression()
                pass

            elif la_ == 3:
                self.state = 392
                self.match(pirParser.T__3)
                self.state = 393
                self.integerAlgebraicExpression()
                self.state = 394
                self.match(pirParser.T__4)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerSummationExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AdditionOperator(self):
            return self.getToken(pirParser.AdditionOperator, 0)

        def SubtractionOperator(self):
            return self.getToken(pirParser.SubtractionOperator, 0)

        def IntegerLiteral(self, i:int=None):
            if i is None:
                return self.getTokens(pirParser.IntegerLiteral)
            else:
                return self.getToken(pirParser.IntegerLiteral, i)

        def integerAlgebraicExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pirParser.IntegerAlgebraicExpressionContext)
            else:
                return self.getTypedRuleContext(pirParser.IntegerAlgebraicExpressionContext,i)


        def getRuleIndex(self):
            return pirParser.RULE_integerSummationExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntegerSummationExpression" ):
                return visitor.visitIntegerSummationExpression(self)
            else:
                return visitor.visitChildren(self)




    def integerSummationExpression(self):

        localctx = pirParser.IntegerSummationExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_integerSummationExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pirParser.IntegerLiteral]:
                self.state = 398
                self.match(pirParser.IntegerLiteral)
                pass
            elif token in [pirParser.T__3]:
                self.state = 399
                self.match(pirParser.T__3)
                self.state = 400
                self.integerAlgebraicExpression()
                self.state = 401
                self.match(pirParser.T__4)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 405
            _la = self._input.LA(1)
            if not(_la==pirParser.AdditionOperator or _la==pirParser.SubtractionOperator):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 412
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 406
                self.match(pirParser.IntegerLiteral)
                pass

            elif la_ == 2:
                self.state = 407
                self.integerAlgebraicExpression()
                pass

            elif la_ == 3:
                self.state = 408
                self.match(pirParser.T__3)
                self.state = 409
                self.integerAlgebraicExpression()
                self.state = 410
                self.match(pirParser.T__4)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatAlgebraicExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def floatSummationExpression(self):
            return self.getTypedRuleContext(pirParser.FloatSummationExpressionContext,0)


        def floatMultiplicationExpression(self):
            return self.getTypedRuleContext(pirParser.FloatMultiplicationExpressionContext,0)


        def getRuleIndex(self):
            return pirParser.RULE_floatAlgebraicExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatAlgebraicExpression" ):
                return visitor.visitFloatAlgebraicExpression(self)
            else:
                return visitor.visitChildren(self)




    def floatAlgebraicExpression(self):

        localctx = pirParser.FloatAlgebraicExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_floatAlgebraicExpression)
        try:
            self.state = 416
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 414
                self.floatSummationExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 415
                self.floatMultiplicationExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatMultiplicationExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FloatLiteral(self, i:int=None):
            if i is None:
                return self.getTokens(pirParser.FloatLiteral)
            else:
                return self.getToken(pirParser.FloatLiteral, i)

        def MultiplicationOperator(self):
            return self.getToken(pirParser.MultiplicationOperator, 0)

        def DivisionOperator(self):
            return self.getToken(pirParser.DivisionOperator, 0)

        def IntegerLiteral(self):
            return self.getToken(pirParser.IntegerLiteral, 0)

        def floatMultiplicationExpression(self):
            return self.getTypedRuleContext(pirParser.FloatMultiplicationExpressionContext,0)


        def getRuleIndex(self):
            return pirParser.RULE_floatMultiplicationExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatMultiplicationExpression" ):
                return visitor.visitFloatMultiplicationExpression(self)
            else:
                return visitor.visitChildren(self)




    def floatMultiplicationExpression(self):

        localctx = pirParser.FloatMultiplicationExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_floatMultiplicationExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.match(pirParser.FloatLiteral)
            self.state = 419
            _la = self._input.LA(1)
            if not(_la==pirParser.MultiplicationOperator or _la==pirParser.DivisionOperator):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 423
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 420
                self.match(pirParser.IntegerLiteral)
                pass

            elif la_ == 2:
                self.state = 421
                self.match(pirParser.FloatLiteral)
                pass

            elif la_ == 3:
                self.state = 422
                self.floatMultiplicationExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatSummationExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AdditionOperator(self):
            return self.getToken(pirParser.AdditionOperator, 0)

        def SubtractionOperator(self):
            return self.getToken(pirParser.SubtractionOperator, 0)

        def FloatLiteral(self, i:int=None):
            if i is None:
                return self.getTokens(pirParser.FloatLiteral)
            else:
                return self.getToken(pirParser.FloatLiteral, i)

        def floatMultiplicationExpression(self):
            return self.getTypedRuleContext(pirParser.FloatMultiplicationExpressionContext,0)


        def IntegerLiteral(self):
            return self.getToken(pirParser.IntegerLiteral, 0)

        def floatSummationExpression(self):
            return self.getTypedRuleContext(pirParser.FloatSummationExpressionContext,0)


        def getRuleIndex(self):
            return pirParser.RULE_floatSummationExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatSummationExpression" ):
                return visitor.visitFloatSummationExpression(self)
            else:
                return visitor.visitChildren(self)




    def floatSummationExpression(self):

        localctx = pirParser.FloatSummationExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_floatSummationExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 425
                self.match(pirParser.FloatLiteral)
                pass

            elif la_ == 2:
                self.state = 426
                self.floatMultiplicationExpression()
                pass


            self.state = 429
            _la = self._input.LA(1)
            if not(_la==pirParser.AdditionOperator or _la==pirParser.SubtractionOperator):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 430
                self.match(pirParser.IntegerLiteral)
                pass

            elif la_ == 2:
                self.state = 431
                self.match(pirParser.FloatLiteral)
                pass

            elif la_ == 3:
                self.state = 432
                self.floatSummationExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GeneralAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classAssignment(self):
            return self.getTypedRuleContext(pirParser.ClassAssignmentContext,0)


        def booleanAssignment(self):
            return self.getTypedRuleContext(pirParser.BooleanAssignmentContext,0)


        def floatAssignment(self):
            return self.getTypedRuleContext(pirParser.FloatAssignmentContext,0)


        def integerAssignment(self):
            return self.getTypedRuleContext(pirParser.IntegerAssignmentContext,0)


        def charAssignment(self):
            return self.getTypedRuleContext(pirParser.CharAssignmentContext,0)


        def getRuleIndex(self):
            return pirParser.RULE_generalAssignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGeneralAssignment" ):
                return visitor.visitGeneralAssignment(self)
            else:
                return visitor.visitChildren(self)




    def generalAssignment(self):

        localctx = pirParser.GeneralAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_generalAssignment)
        try:
            self.state = 440
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.classAssignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 436
                self.booleanAssignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 437
                self.floatAssignment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 438
                self.integerAssignment()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 439
                self.charAssignment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BaseParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(pirParser.Identifier, 0)

        def IntegerLiteral(self):
            return self.getToken(pirParser.IntegerLiteral, 0)

        def FloatLiteral(self):
            return self.getToken(pirParser.FloatLiteral, 0)

        def getRuleIndex(self):
            return pirParser.RULE_baseParameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBaseParameter" ):
                return visitor.visitBaseParameter(self)
            else:
                return visitor.visitChildren(self)




    def baseParameter(self):

        localctx = pirParser.BaseParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_baseParameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pirParser.IntegerLiteral) | (1 << pirParser.FloatLiteral) | (1 << pirParser.Identifier))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





