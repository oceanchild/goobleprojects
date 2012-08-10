package com.gooble.logic.api;

import java.util.ArrayList;
import java.util.List;

import android.content.Context;

import com.gooble.logic.app.db.entity.VariableAdapter;
import com.gooble.logic.app.entity.Variable;

public class VariableDomain implements VariableFacade{

   public List<Long> save(Context context, Long puzzleId, List<Long> ids, List<String> names) {
      VariableAdapter helper = new VariableAdapter(context);
      List<Long> newIds = new ArrayList<Long>();
      for (int i = 0; i < ids.size(); i++){
         Long id = ids.get(i);
         String name = names.get(i);
         Variable var = helper.getById(id);
         if (var == null) {
            var = helper.create();
            var.setPuzzleid(puzzleId);
            var.setName(name);
         } else {
            var.setName(name);
         }
         newIds.add(var.getId());
         helper.store(var);
      }
      return newIds;
   }

}
