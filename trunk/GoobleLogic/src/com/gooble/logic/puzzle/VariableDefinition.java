package com.gooble.logic.puzzle;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.gooble.logic.kb.KnowledgeBaseFacade;
import com.gooble.logic.kb.Rule;
import com.gooble.logic.kb.stmts.Statement;
import com.gooble.logic.kb.terms.Constant;
import com.gooble.logic.kb.terms.Term;
import com.gooble.logic.kb.terms.Variable;

public class VariableDefinition implements Definition {
   private Map<String, List<?>> variables = new HashMap<String, List<?>>();
   private String main;

   public void add(String varName, Object... domainValues) {
      variables.put(varName, Arrays.asList(domainValues));
   }

   public void setMain(String varName) {
      main = varName;
   }

   public void augment(KnowledgeBaseFacade kb) {
      addStatements(kb);
      addRules(kb);
      addSolutions(kb);
   }

   private void addStatements(KnowledgeBaseFacade kb) {
      for (String varName : variables.keySet()){
         for (Object domainVal : variables.get(varName)){
            Term<?> term = new Constant<Object>(domainVal);
            kb.add(new Statement(varName, term));
         }
      }
   }

   private void addRules(KnowledgeBaseFacade kb) {
      for (String varName : variables.keySet()){
         if (varName.equals(main)) 
            continue;
         kb.add(new Rule(
               propertyStatement(varName, new Variable("X"), new Variable("Y")),
               new Statement(main, new Variable("X")), new Statement(varName, new Variable("Y"))));
      }
   }

   private void addSolutions(KnowledgeBaseFacade kb) {
      int numberOfOtherVariables = variables.keySet().size() - 1;
      int solutionIndex = 1;
      for (Object mainVal : variables.get(main)){
         Statement consequence = new StatementFrom("solution" + solutionIndex).numberOfVariables(numberOfOtherVariables);
         Statement[] antecedents = createAntecedentsForOtherVariables(mainVal, numberOfOtherVariables);
         kb.add(new Rule(consequence, antecedents));
         solutionIndex++;
      }
   }

   private Statement[] createAntecedentsForOtherVariables(Object mainVal, int numberOfOtherVariables) {
      List<Statement> antecedents = new ArrayList<Statement>();
      int variableIndex = 1;
      for (String varName : variables.keySet()){
         if (varName.equals(main)) 
            continue;
         antecedents.add(propertyStatement(varName, 
               new Constant<Object>(mainVal),
               new Variable("V" + variableIndex)
               ));
         variableIndex++;
      }
      return antecedents.toArray(new Statement[numberOfOtherVariables]);
   }
   
   private Statement propertyStatement(String varName, Term<?> term1, Term<?> term2){
      return new Statement(varName + "Of", new Term<?>[]{term1, term2});
   }
}
