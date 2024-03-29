package com.gooble.logic.test.kb;

import static com.gooble.logic.kb.encoding.KBEncoding.replacement;
import static com.gooble.logic.kb.encoding.KBEncoding.rule;
import static com.gooble.logic.kb.encoding.KBEncoding.solution;
import static com.gooble.logic.kb.encoding.KBEncoding.statement;
import static junit.framework.Assert.assertFalse;
import static org.junit.Assert.assertEquals;

import java.util.Arrays;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import com.gooble.logic.Logger;
import com.gooble.logic.kb.ConsistentMerge;
import com.gooble.logic.kb.KnowledgeBase;
import com.gooble.logic.kb.Rule;
import com.gooble.logic.kb.solutions.SolutionSet;

public class CaseTest {

   private KnowledgeBase kb;

   @Before
   public void setup() throws Exception{
      kb = new KnowledgeBase();      
      // All women
      kb.add(statement("woman(adele)"));
      kb.add(statement("woman(jane)"));
      kb.add(statement("woman(laura)"));
      kb.add(statement("woman(molly)"));
      kb.add(statement("woman(sarah)"));

      // All houses
      kb.add(statement("house(1)"));
      kb.add(statement("house(3)"));
      kb.add(statement("house(2)"));
      kb.add(statement("house(4)"));
      kb.add(statement("house(5)"));

      kb.add(statement("directlyEastOf(1, 2)"));
      kb.add(statement("directlyEastOf(3, 4)"));

      kb.add(statement("nextTo(1, 3)"));
      kb.add(statement("nextTo(3, 1)"));
      kb.add(statement("nextTo(2, 4)"));
      kb.add(statement("nextTo(4, 2)"));
      kb.add(statement("nextTo(4, 5)"));
      kb.add(statement("nextTo(5, 4)"));

      kb.add(rule("house(X) ^ house(Y) ^ X > Y => northOf(X, Y)"));
      kb.add(rule("house(X) ^ house(Y) ^ X < Y => southOf(X, Y)"));      

      // All hair colours
      kb.add(statement("hairColour(black)"));
      kb.add(statement("hairColour(blonde)"));
      kb.add(statement("hairColour(brown)"));
      kb.add(statement("hairColour(chestnut)"));
      kb.add(statement("hairColour(grey)"));
   }

   @Test
   public void a_few_different_queries() throws Exception{
      kb.add(rule("house(X) ^ woman(Y) => livesAtHouse(X, Y)"));
      kb.add(rule("hairColour(C) ^ woman(W) => hairOf(W, C)"));
      kb.add(rule("woman(A) ^ livesAtHouse(B, A) ^ hairOf(A, C) => everythingAbout(A, B, C)"));

      assertEquals(Arrays.asList(solution(replacement("C", "black")),
            solution(replacement("C", "blonde")),
            solution(replacement("C", "brown")),
            solution(replacement("C", "chestnut")),
            solution(replacement("C", "grey"))),
            kb.findSolutions(statement("hairOf(molly, C)")).list());
      assertEquals(Arrays.asList(solution(replacement("H", 1)),
            solution(replacement("H", 3)),
            solution(replacement("H", 2)),
            solution(replacement("H", 4)),
            solution(replacement("H", 5))),
            kb.findSolutions(statement("livesAtHouse(H, molly)")).list());
      assertEquals(25, kb.findSolutions(statement("everythingAbout(molly, X, Y)")).list().size());
      assertEquals(Arrays.asList(solution(replacement("H", 4)), solution(replacement("H", 5))), kb.findSolutions(statement("northOf(H, 3)")).list());
      assertFalse(kb.query(statement("nextTo(1, 2)")));
   }

   @Test
   public void solve() throws Exception{
      kb.add(rule("house(X) ^ woman(Y) => livesAtHouse(X, Y)"));
      kb.add(rule("hairColour(C) ^ woman(W) => hairOf(W, C)"));

      Rule rule1 = rule("hairOf(W1, blonde) ^ livesAtHouse(H1, W1) ^ nextTo(H1, H2) ^ southOf(H2, H1) ^ livesAtHouse(H2, adele) ^ " +
            "directlyEastOf(H3, H2) ^ livesAtHouse(H3, laura) => solution1(W1, H1, H2, H3)" );

      Rule rule2 = rule("livesAtHouse(H4, sarah) ^ nextTo(H5, H4) ^ southOf(H5, H4) ^ livesAtHouse(H5, molly) => solution2(H4, H5)");
      Rule rule3 = rule("livesAtHouse(H6, W2) ^ directlyEastOf(H7, H6) ^ livesAtHouse(H7, jane) ^ northOf(H8, H7) ^ livesAtHouse(H8, W3) ^ hairOf(W3, grey) => solution3(H6, W2, H7, H8, W3)");
      Rule rule4 = rule("hairOf(W4, chestnut) ^ livesAtHouse(H9, W4) ^ nextTo(H10, H9) ^ northOf(H10, H9) ^ livesAtHouse(H10, W5) ^ hairOf(W5, black) => solution4(W4, H9, H10, W5)");

      kb.add(rule1);
      kb.add(rule2);
      kb.add(rule3);
      kb.add(rule4);

      SolutionSet solns1 = kb.findSolutions(statement("solution1(W1, H1, H2, H3)"));
      SolutionSet solns2 = kb.findSolutions(statement("solution2(H4, H5)"));
      SolutionSet solns3 = kb.findSolutions(statement("solution3(H6, W2, H7, H8, W3)"));
      SolutionSet solns4 = kb.findSolutions(statement("solution4(W4, H9, H10, W5)"));

      ConsistentMerge consistentMerge = new ConsistentMerge(rule1, solns1, rule2, solns2);
      consistentMerge.ignoring(Arrays.asList(statement("nextTo(X, Y)")));
      
      consistentMerge = new ConsistentMerge(consistentMerge.getMergedRule(), consistentMerge.getMergedSolutions(), rule3, solns3);
      consistentMerge.ignoring(Arrays.asList(statement("nextTo(X, Y)")));
      
      consistentMerge = new ConsistentMerge(consistentMerge.getMergedRule(), consistentMerge.getMergedSolutions(), rule4, solns4);
      consistentMerge.ignoring(Arrays.asList(statement("nextTo(X, Y)")));
      
      /*
       * QUERY true, SOLUTIONS: SOLUTION: 

[(VAR:W1111=CONST:molly),  -> molly is blonde
(VAR:H1111=CONST:4),  -> molly lives at house 4
(VAR:H2111=CONST:2),  -> adele lives at house 2
(VAR:H3111=CONST:1),  -> laura lives at house 1
(VAR:H4211=CONST:5),  -> sarah lives at house 5
(VAR:H5211=CONST:4),  -> molly lives at house 4
(VAR:H621=CONST:4),   -> molly lives at house 4
(VAR:W221=CONST:molly), -> molly is woman 2
(VAR:H721=CONST:3),   -> jane lives at house 3
(VAR:H821=CONST:5),   -> grey haired woman lives at house 5 -> sarah has grey hair
(VAR:W321=CONST:sarah), -> sarah has grey hair & lives at house 5
(VAR:W42=CONST:laura), -> laura has chestnut hair
(VAR:H92=CONST:1), -> laura lives at house 1
(VAR:H102=CONST:3), -> h10 is 3
(VAR:W52=CONST:jane)] -> jane has black hair, lives at house 3
       */
      
   }

   @After
   public void close(){
      Logger.close();
   }

}
