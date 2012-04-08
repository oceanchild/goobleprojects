package main.kb.stmts;

import main.kb.Constant;
import main.kb.Statement;

public class GreaterThan extends Operator{

   public GreaterThan(Constant<Number> limit, Constant<?> constant) {
      super(">", limit, constant);
   }
   
   @Override
   protected Statement createStatement(Constant<?>[] constants){
      return new GreaterThan((Constant<Number>) constants[0], constants[1]);
   }

   @Override
   protected boolean evaluateInternal(Constant<Number> limit, Constant<Number> constant) {
      return ((Number) constant.getValue()).floatValue() > limit.getValue().floatValue();
   }
   
}