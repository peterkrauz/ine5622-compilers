grammar pir;

start: generalDeclaration* EOF;

booleanAssignment:
	Identifier ':' booleanType '=' (BooleanLiteral | Identifier);
integerAssignment:
	Identifier ':' integerType '=' (IntegerLiteral | Identifier);
floatAssignment:
	Identifier ':' floatType '=' (FloatLiteral | Identifier);
charAssignment:
	Identifier ':' charType '=' (CharLiteral | Identifier);

BooleanLiteral: 'Aye' | 'Nay';
IntegerLiteral: [0-9]+;
FloatLiteral: [0-9]+ '.' [0-9]+;
CharLiteral: '\'' [a-zA-Z] '\'';
GeneralLiteral: BooleanLiteral | IntegerLiteral | FloatLiteral;

booleanType: 'Boolean';
integerType: 'Integer';
floatType: 'Float';
charType: 'Char';

numberType: integerType | floatType;
type: booleanType | integerType | floatType | charType;

typeDeclaration: Identifier ':' type;

generalDeclaration:
	generalAssignment
	| generalExpression
	| typeDeclaration
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
	booleanAssignment
	| floatAssignment
	| integerAssignment
	| charAssignment;

baseParameter: Identifier | IntegerLiteral | FloatLiteral;

NewLine: '\n';
Identifier: [a-zA-Z]+;
WS: [\n\r\u0020\u0009\u000C]+ -> skip;