package com.gooble.logic.test.kb.terms;

import static com.gooble.logic.kb.encoding.TermEncoding.constant;
import static com.gooble.logic.kb.encoding.TermEncoding.variable;
import static junit.framework.Assert.assertTrue;
import static org.junit.Assert.assertFalse;

import org.junit.Test;

public class ConstantTest {

   @Test 
   public void match_only_constants_of_same_value() throws Exception{
      assertTrue(constant("x").match(constant("x")));
      assertFalse(constant("x").match(constant(10)));
      assertFalse(constant("x").match(variable("X")));
   }
   
   @Test
   public void constants_equals() throws Exception{
      assertTrue(constant("x").equals(constant("x")));
      assertFalse(constant("x").equals(constant("X")));
      assertFalse(constant("x").equals(constant(10)));
      assertTrue(constant(10).equals(constant(10)));
      assertTrue(constant(10).equals(constant(10.0)));
   }
   
}
