grammar pir;

start: generalDeclaration* EOF;

booleanAssignment:
	Identifier ':' booleanType '=' BooleanLiteral;
integerAssignment:
	Identifier ':' integerType '=' IntegerLiteral;
floatAssignment: Identifier ':' floatType '=' FloatLiteral;
charAssignment: Identifier ':' charType '=' CharLiteral;

BooleanLiteral: 'Aye' | 'Nay';
IntegerLiteral: [0-9]+;
FloatLiteral: [0-9]+ '.' [0-9]+;
NumberLiteral: IntegerLiteral | FloatLiteral;
CharLiteral: '\'' [a-zA-Z] '\'';
ClassIdentifier: [A-Z][a-zA-Z]*;

booleanType: 'Boolean';
integerType: 'Integer';
floatType: 'Float';
charType: 'Char';

numberType: integerType | floatType;
type: booleanType | integerType | floatType | charType;

typeDeclaration: Identifier ':' type;

generalDeclaration: assignment | typeDeclaration | NewLine;

assignment:
	booleanAssignment
	| floatAssignment
	| integerAssignment
	| charAssignment;

baseParameter: Identifier | IntegerLiteral | FloatLiteral;

NewLine: '\n';
Identifier: [a-zA-Z]+;
WS: [\n\r\u0020\u0009\u000C]+ -> skip;