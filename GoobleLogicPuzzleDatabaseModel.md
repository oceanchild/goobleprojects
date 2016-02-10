# Introduction #

## What are relations? ##

"x is next To y"
---> it can be two variables, or two literals, and there's an order involed
nextTo(X, Y) -> this is bi-directional, nonunique, meaning that nextTo(X, Y) can be true, and nextTo(X, Z) can be true at the same time


Relation
id
bidirectional
unique
name


Each relation has multiple TERMS -- this is it, TERMS. Terms have an ORDER.

Term
id
relationid -> link back to relation
relationorder (1 for first, 2 for second, etc)
value - X, Y, 1, 2, bob
variable - true/false

There could be multiple conditions which make the relation true.
I.e. lessThan(X, Y) is true if X < Y:

Condition
id
relationid
operator --- links to operator table?
--> multiple operands, and operand order? is this TERMS again? it would be the same term as in the relation. but how to link term back to condition, instead of relation? a conditionid? or would we assume always that there are Two operands? maybe a Conditionterm table?

Conditionterm
id
conditionid
termid

## What are Properties? ##

it states that Bob Has Blue Shoes
or Bob's shoes are X
-- So, two terms; any combination of variables & values
-- so a property is just two terms - but these terms do not link to relations, they link to properties
-- should term not have a Relationid? because they are not necessarily linked to relations. Relationterm, Propertyterm


# Tables #

Puzzle
  * id
  * name
  * mainvariableid references variable(id)

Variable
  * id
  * puzzleid references puzzle(id)
  * name

Variablevalue
  * id
  * variableid references variable(id)
  * value

Relation
  * id
  * puzzleid references puzzle(id)
  * bidirectional **bool**
  * unique **bool**
  * name
  * variableid references variable(id)

Condition
  * id
  * relationid references relation(id)
  * operator **const**

Term
  * id
  * value
  * variable **bool**
  * variableid references variable(id)

Hint
  * id
  * puzzleid references puzzle(id)

Property
  * id
  * hintid references hint(id)

Propertyterm
  * id
  * termid references term(id)
  * propertyid references property(id)

Conditionterm
  * id
  * termid references term(id)
  * conditionid references condition(id)

Relationterm
  * id
  * relationid references relation(id)
  * termid references term(id)
  * relationorder **int**