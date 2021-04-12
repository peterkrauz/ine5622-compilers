grammar pir;

start: generalDeclaration* EOF;

generalArgument:
	Identifier
	| BooleanLiteral
	| CharLiteral
	| FloatLiteral
	| IntegerLiteral;

generalArguments: generalArgument (',' generalArgument)*;

typedArguments: typeDeclaration (',' typeDeclaration)*;

classAssignment:
	Identifier ':' ClassIdentifier '=' ClassIdentifier '(' generalArguments? ')';
booleanAssignment:
	Identifier ':' booleanType '=' (BooleanLiteral | Identifier);
integerAssignment:
	Identifier ':' integerType '=' (IntegerLiteral | Identifier);
floatAssignment:
	Identifier ':' floatType '=' (FloatLiteral | Identifier);
charAssignment:
	Identifier ':' charType '=' (CharLiteral | Identifier);

IntegerLiteral: [0-9]+;
FloatLiteral: [0-9]+ '.' [0-9]+;
CharLiteral: '\'' [a-zA-Z] '\'';
BooleanLiteral: 'Aye' | 'Nay';
GeneralLiteral:
	IntegerLiteral
	| FloatLiteral
	| CharLiteral
	| BooleanLiteral;

booleanType: 'Boolean';
integerType: 'Integer';
floatType: 'Float';
charType: 'Char';

numberType: integerType | floatType;
type: booleanType | integerType | floatType | charType;

functionKeyword: 'ahoy';
functionName: Identifier;
functionDeclaration:
	functionKeyword functionName '(' typedArguments? ')' '{' generalDeclaration* '}';

functionInvocation: functionName '(' generalArguments? ')';

classDeclaration:
	simpleClassDeclaration
	| completeClassDeclaration;

classConstructor:
	'(' typeDeclaration (',' typeDeclaration)* ')';
simpleClassDeclaration:
	'class' ClassIdentifier classConstructor?;
completeClassDeclaration:
	simpleClassDeclaration '{' generalDeclaration* '}';

typeDeclaration: Identifier ':' type;

generalDeclaration:
	generalAssignment
	| generalExpression
	| typeDeclaration
	| classDeclaration
	| functionDeclaration
	| functionInvocation
	| NewLine;

generalExpression: loopExpression | controlExpression;

loopExpression: whileExpression | forExpression;

whileExpression:
	'while' cond = comparisonExpression '{' generalDeclaration+ '}';
forExpression:
	'for' Identifier 'in' Identifier '{' generalDeclaration+ '}';

controlExpression: ifExpression elseExpression?;

ifExpression:
	'if' cond = comparisonExpression '{' generalDeclaration+ '}';

elseExpression: 'else' '{' generalDeclaration+ '}';

comparisonExpression:
	(comparisonOperand comparisonOperator comparisonOperand)
	| BooleanLiteral;
comparisonOperand: (IntegerLiteral | FloatLiteral | Identifier);
comparisonOperator: '>' | '<' | '>=' | '<=' | '==' | '!=';

generalAssignment:
	classAssignment
	| booleanAssignment
	| floatAssignment
	| integerAssignment
	| charAssignment;

baseParameter: Identifier | IntegerLiteral | FloatLiteral;

NewLine: '\n';
ClassIdentifier: [A-Z][a-zA-Z]*;
Identifier: [a-zA-Z]+;
WS: [\n\r\u0020\u0009\u000C]+ -> skip;