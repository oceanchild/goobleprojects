package com.gooble.logic.app.db;

import android.provider.BaseColumns;

public class Tables {

   public static final String _ID = BaseColumns._ID;
   
   public static final class Puzzle implements BaseColumns{
      public static final String NAME = "name";
      public static final String MAINVARIABLEID = "mainvariableid";
   }

   public static final class Variable implements BaseColumns{
      public static final String NAME = "name";
      public static final String PUZZLEID = "puzzleid";
      public static final String TYPE = "type";
   }
   public static final class Variablevalue implements BaseColumns{
      public static final String VALUE = "value";
      public static final String VARIABLEID = "variableid";
   }
   public static final class Term implements BaseColumns{
      public static final String VALUE = "value"; // if it's a variable it will have this eg X Y Z
      public static final String VARIABLEID = "variableid";
      public static final String VARIABLEVALUEID = "variablevalueid"; // if it's not a variable it will have this instead
   }
   
   /*
    * Hints
    */
   public static final class Hint implements BaseColumns{
      public static final String PUZZLEID = "puzzleid";
   }
   public static final class Hintvariable implements BaseColumns{
      public static final String NAME = "name"; // like X Y Z
      public static final String HINTID = "hintid";
      public static final String VARIABLEID = "variableid";
   }
   public static final class Hintrelation implements BaseColumns{
      public static final String HINTID = "hintid";
      public static final String RELATIONID = "relationid";
   }
   public static final class Hintrelationterm implements BaseColumns{
      public static final String HINTRELATIONID = "hintrelationid";
      public static final String VARIABLEVALUEID = "variablevalueid"; // has this
      public static final String HINTVARIABLEID = "hintvariableid"; // or has this. not both though, and not neither
   }
   public static final class Property implements BaseColumns{
      public static final String HINTID = "hintid";
   }
   public static final class Propertyterm implements BaseColumns{
      public static final String PROPERTYID = "propertyid";
      public static final String HINTVARIABLEID = "hintvariableid";
      public static final String VARIABLEVALUEID = "variablevalueid";
   }
   
   /*
    * relation definitions (for the overall puzzle; not specific instances for hints) 
    */
   public static final class Relation implements BaseColumns{
      public static final String NAME = "name";
      public static final String BIDIRECTIONAL = "bidirectional"; // if a relation is bidirectional, it means that if rel(X, Y) is true, rel(Y, X) is true
      public static final String UNIQUEVALUE = "uniquevalue"; // if a relation is unique, it means if rel(X, Y) is true, rel(X, Z) cannot be true for any Z s.t Z != Y 
      public static final String VARIABLEID = "variableid";
      public static final String PUZZLEID = "puzzleid";
   }
   public static final class Relationterm implements BaseColumns{
      public static final String RELATIONID = "relationid";
      public static final String TERMID = "termid";
      public static final String RELATIONORDER = "relationorder"; // the order that this variable comes in in the relation. eg for rel(X, Y) , RELATIONORDER(X) must be less than RELATIONORDER(Y)
   }
   public static final class Conditionset implements BaseColumns{
      public static final String RELATIONID = "relationid";
      public static final String NAME = "name";
   }
   public static final class Condition implements BaseColumns{
      public static final String CONDITIONSETID = "conditionsetid";
      public static final String OPERATOR = "operator";
   }
   public static final class Conditionterm implements BaseColumns{
      public static final String CONDITIONID = "conditionid";
      public static final String TERMID = "termid";
   }
   
}
 