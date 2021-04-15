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

// Assignments

classAssignment:
	Identifier ':' ClassIdentifier '=' ClassIdentifier '(' generalArguments? ')';

booleanAssignment:
	Identifier ':' booleanType '=' (BooleanLiteral | Identifier);

integerAssignment:
	Identifier ':' integerType '=' (
		integerAlgebraicExpression
		| IntegerLiteral
		| Identifier
	);

floatAssignment:
	Identifier ':' floatType '=' (
		floatAlgebraicExpression
		| FloatLiteral
		| Identifier
	);

charAssignment:
	Identifier ':' charType '=' (CharLiteral | Identifier);

// Literals

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

// Functions

functionKeyword: 'ahoy';
functionName: Identifier;
functionDeclaration:
	functionKeyword functionName '(' typedArguments? ')' '{' generalDeclaration* '}';

functionInvocation: functionName '(' generalArguments? ')';

// Classes

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

generalInvocation:
	generalAssignment
	| generalExpression
	| typeDeclaration
	| functionInvocation;

// Epressions

generalExpression:
	loopExpression
	| controlExpression
	| algebraicExpression;

loopExpression: whileExpression | forExpression;

whileExpression:
	'while' cond = comparisonExpression '{' generalDeclaration* '}';
forExpression:
	'for' Identifier 'in' Identifier '{' generalDeclaration* '}';

controlExpression:
	ifExpression elseExpression?
	| switchCaseExpression;

switchCaseExpression:
	'switch' (Identifier | GeneralLiteral) '{' switchCaseBody '}';

switchCaseBody: switchCaseCaseBranch* switchCaseElseBranch;
switchCaseCaseBranch:
	'case' (Identifier | comparisonExpression) '{' generalInvocation* '}';
switchCaseElseBranch: 'else' '{' generalInvocation* '}';

ifExpression:
	'if' cond = comparisonExpression '{' generalDeclaration* '}';

elseExpression: 'else' '{' generalDeclaration* '}';

comparisonExpression:
	(comparisonOperand comparisonOperator comparisonOperand)
	| BooleanLiteral;
comparisonOperand: (
		IntegerLiteral
		| FloatLiteral
		| Identifier
		| algebraicExpression
	);
comparisonOperator: '>' | '<' | '>=' | '<=' | '==' | '!=';

algebraicExpression:
	integerAlgebraicExpression
	| floatAlgebraicExpression;

// Integer

integerAlgebraicExpression:
	integerSummationExpression
	| integerMultiplicationExpression;

integerMultiplicationExpression:
	IntegerLiteral (MultiplicationOperator | DivisionOperator) (
		IntegerLiteral
		| integerMultiplicationExpression
	);

integerSummationExpression:
	(IntegerLiteral | integerMultiplicationExpression) (
		AdditionOperator
		| SubtractionOperator
	) (IntegerLiteral | integerAlgebraicExpression);

// Float

floatAlgebraicExpression:
	floatSummationExpression
	| floatMultiplicationExpression;

floatMultiplicationExpression:
	FloatLiteral (MultiplicationOperator | DivisionOperator) (
		IntegerLiteral
		| FloatLiteral
		| floatMultiplicationExpression
	);

floatSummationExpression:
	(FloatLiteral | floatMultiplicationExpression) (
		AdditionOperator
		| SubtractionOperator
	) (IntegerLiteral | FloatLiteral | floatSummationExpression);

AdditionOperator: '+';
SubtractionOperator: '-';
MultiplicationOperator: '*';
DivisionOperator: '/';

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
