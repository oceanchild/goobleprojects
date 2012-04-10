package main.kb.stmts;

import main.kb.Constant;
import main.kb.Statement;
import main.kb.Term;

public class LessThan extends Operator {

   public LessThan(Term<?> limit, Term<?> constant) {
      super("<", limit, constant);
   }
   
   @Override
   protected Statement createStatement(Term<?>[] constants){
      return new LessThan(constants[0], constants[1]);
   }

   @Override
   protected boolean evaluateInternal(Constant<Number> limit, Constant<Number> constant) {
      return ((Number) constant.getValue()).floatValue() < limit.getValue().floatValue();
   }

}