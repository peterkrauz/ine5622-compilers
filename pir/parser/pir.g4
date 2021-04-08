grammar pir;

start: generalDeclaration* EOF;

booleanAssignment:
	Identifier ':' booleanType '=' BooleanLiteral;
integerAssignment:
	Identifier ':' integerType '=' IntegerLiteral;
floatAssignment: Identifier ':' floatType '=' FloatLiteral;
charAssignment: Identifier ':' charType '=' CharLiteral;
classAssignment:
	Identifier ':' ClassIdentifier '=' ClassIdentifier '(' classParameters? ')';

BooleanLiteral: 'Aye' | 'Nay';
IntegerLiteral: [0-9]+;
FloatLiteral: [0-9]+ '.' [0-9]+;
CharLiteral: '\'' [a-zA-Z] '\'';
ClassIdentifier: [A-Z][a-zA-Z]*;

booleanType: 'Boolean';
integerType: 'Integer';
floatType: 'Float';
charType: 'Char';

type: booleanType | integerType | floatType | charType;

typeDeclaration: Identifier ':' type;

generalDeclaration:
	assignment
	| typeDeclaration
	| functionDeclaration
	| classDeclaration
	| NewLine;

assignment:
	booleanAssignment
	| floatAssignment
	| classAssignment
	| integerAssignment
	| charAssignment;

baseParameter: Identifier | IntegerLiteral | FloatLiteral;

classKeyword: 'class';
classMembers: typeDeclaration (',' typeDeclaration)*;
classBody: '{' NewLine* generalDeclaration* NewLine* '}';
classParameters: baseParameter (',' baseParameter*);

classDeclaration:
	classKeyword name = ClassIdentifier '(' classMembers? ')'
	| classKeyword name = ClassIdentifier '(' classMembers? ')' classBody;

functionKeyword: 'ahoy';
functionArguments: typeDeclaration (',' typeDeclaration)*;
functionInvocation:
	name = Identifier '(' functionParameters? ')';
functionParameters: baseParameter (',' baseParameter*);

functionDeclaration:
	functionKeyword name = Identifier '(' functionArguments? ')' '{' NewLine+ statements NewLine+
		'}';

statements: assignment*;

expressions: expression (',' expression)*;
expression:
	left = sumExpression (
		op = ('>' | '<' | '>=' | '<=' | '==' | '!=') right = expression
	)*;
sumExpression:
	left = multiplicationExpression (
		op = ('+' | '-') right = sumExpression
	)*;

multiplicationExpression:
	left = atomicExpression (
		op = ('*' | '/') right = multiplicationExpression
	)*;

atomicExpression:
	'(' expression ')'
	| IntegerLiteral
	| FloatLiteral
	| functionDeclaration;

NewLine: '\n';
Identifier: [a-zA-Z]+;
WS: [\n\r\u0020\u0009\u000C]+ -> skip;