package com.gooble.logic.kb.stmts;

import static com.gooble.logic.Logger.log;

import com.gooble.logic.kb.Constant;
import com.gooble.logic.kb.Statement;
import com.gooble.logic.kb.Term;


abstract public class Operator extends Statement {

   private final Term<?> constant;
   private final Term<?> limit;
   
   public Operator(String name, Term<?> limit, Term<?> constant) {
      super(name, limit, constant);
      this.limit = limit;
      this.constant = constant;
   }
   
   @Override
   public boolean evaluate(){
      log("evaluating statement: " + this);
      if (!(constant.getValue() instanceof Number) || !(limit.getValue() instanceof Number))
         return false;
      else
         return evaluateInternal((Constant<Number>) limit, (Constant<Number>) constant);
   }
   
   abstract protected boolean evaluateInternal(Constant<Number> limit, Constant<Number> constant);
   
   @Override
   public boolean isToBeEvaluated() {
      return true;
   }
   
   @Override
   protected Statement createStatement(Term<?>[] constants){
      throw new UnsupportedOperationException("Subclass of operator has not overridden create statement method!");
   }
   
   @Override
   public String toString(){
      return "(" + constant + " " + name + " " + limit + ")";
   }

}