package com.gooble.logic.puzzle.domain;

import java.util.ArrayList;
import java.util.List;

import com.gooble.logic.kb.KnowledgeBaseFacade;
import com.gooble.logic.kb.Rule;
import com.gooble.logic.kb.stmts.Statement;
import com.gooble.logic.kb.terms.Constant;
import com.gooble.logic.kb.terms.Term;
import com.gooble.logic.kb.terms.Variable;
import com.gooble.logic.puzzle.StatementFrom;

public class DomainRules {

   private final DomainVariables variables;

   public DomainRules(DomainVariables variables) {
      this.variables = variables;
   }
   public void forProperties(KnowledgeBaseFacade kb){
      for (String varName : variables.secondaryTypes()){
         kb.add(new Rule(
               propertyStatement(varName, new Variable("X"), new Variable("Y")),
               new Statement(variables.getMain(), new Variable("X")), new Statement(varName, new Variable("Y"))));
      }
   }
   public void forSolution(KnowledgeBaseFacade kb){
      int numberOfOtherVariables = variables.numberOfSecondaryVariables();
      int solutionIndex = 1;
      for (Object mainVal : variables.mainValues()){
         Statement consequence = new StatementFrom("solution" + solutionIndex).numberOfVariables(numberOfOtherVariables);
         Statement[] antecedents = createAntecedentsForOtherVariables(mainVal, numberOfOtherVariables);
         kb.add(new Rule(consequence, antecedents));
         solutionIndex++;
      }
   }
   private Statement[] createAntecedentsForOtherVariables(Object mainVal, int numberOfOtherVariables) {
      List<Statement> antecedents = new ArrayList<Statement>();
      int variableIndex = 1;
      for (String varName : variables.secondaryTypes()){
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
