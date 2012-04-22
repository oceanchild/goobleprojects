package com.gooble.logic.kb;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import com.gooble.logic.kb.stmts.Statement;
import com.gooble.logic.kb.terms.Term;

public class RuleMerger {
   
   private final Rule rule2;
   private final Rule rule1;

   public RuleMerger(Rule rule1, Rule rule2){
      this.rule1 = rule1;
      this.rule2 = rule2;
   }

   public Rule merge() {
      return new Rule(mergeConsequent(), mergeAntecedents());
   }

   private Statement mergeConsequent() {
      return new Statement(mergeConsequentName(), mergeConsequentTerms());
   }

   private String mergeConsequentName() {
      return rule1.getConsequence().getName() + rule2.getConsequence().getName();
   }

   private Term<?>[] mergeConsequentTerms() {
      List<Term<?>> mergedConsequentTerms = new ArrayList<Term<?>>();
      mergedConsequentTerms.addAll(Arrays.asList(suffix(rule1.getConsequence().getTerms(), "1")));
      mergedConsequentTerms.addAll(Arrays.asList(suffix(rule2.getConsequence().getTerms(), "2")));
      return mergedConsequentTerms.toArray(new Term<?>[rule1.getConsequence().getTerms().length + rule2.getConsequence().getTerms().length]);
   }

   private Statement[] mergeAntecedents() {
      Statement[] allAntecedents = new Statement[rule1.getAntecedents().length + rule2.getAntecedents().length];
      for (int i = 0; i < rule1.getAntecedents().length; i++){
         allAntecedents[i] = new Statement(rule1.getAntecedents()[i].getName(), suffix(rule1.getAntecedents()[i].getTerms(), "1"));
      }
      for (int i = rule1.getAntecedents().length; i < allAntecedents.length; i++){
         int j = i - rule1.getAntecedents().length;
         allAntecedents[i] = new Statement(rule2.getAntecedents()[j].getName(), suffix(rule2.getAntecedents()[j].getTerms(), "2"));
      }
      return allAntecedents;
   }

   private static Term<?>[] suffix(Term<?>[] terms, String suffix) {
      Term<?>[] suffixedTerms = new Term<?>[terms.length];
      for (int i = 0; i < terms.length; i++){
         suffixedTerms[i] = terms[i].copyWithSuffix(suffix);
      }
      return suffixedTerms;
   }

}