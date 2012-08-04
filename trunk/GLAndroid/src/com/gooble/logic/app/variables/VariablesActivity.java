package com.gooble.logic.app.variables;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;

import com.gooble.logic.api.VariableDomain;
import com.gooble.logic.api.VariableFacade;
import com.gooble.logic.app.R;
import com.gooble.logic.app.R.id;
import com.gooble.logic.app.R.layout;

public class VariablesActivity extends Activity {
   
   private VariableFacade variableFacade;

   public VariablesActivity() {
      this.variableFacade = new VariableDomain();
   }
   
   @Override
   public void onCreate(Bundle icicle) {
      super.onCreate(icicle);
      setContentView(R.layout.variables);
      
      /*
       * TODO: Load all existing variable names with Edit and Delete buttons next to them
       * TODO: need radio set which states which one is the main variable--- 
       *       or maybe this should go on the variable screen.
       */
      
      final Activity activity = this;
      Button addVariableButton = (Button) findViewById(R.id.add_variable_button);
      Button saveVariablesButton = (Button) findViewById(R.id.save_variables_button);
      saveVariablesButton.setOnClickListener(new OnClickListener() {
         public void onClick(View v) {
            variableFacade.save();
            // TODO: maybe go back to previous activity here? Finish?
         }
      });
      
      final LinearLayout layout = (LinearLayout) findViewById(R.id.variable_container);
      addVariableButton.setOnClickListener(new OnClickListener() {
         public void onClick(View v) {
            LayoutInflater inflater = getLayoutInflater();
            final View newVariable = inflater.inflate(R.layout.variable_row, layout, false);
            
            /*
             * TODO: Onclick for this button should go to the Add Variable Values activity
             * set the clicked variable as the current variable that's being edited
             * 
             * it will also have to do the same thing as the "save" button
             *  (i.e save to DB all the variables for this puzzle)
             */
            Button addVariableValuesButton = (Button) newVariable.findViewById(R.id.add_values_button);
            addVariableValuesButton.setOnClickListener(new OnClickListener() {
               public void onClick(View v) {
                  variableFacade.save();
                  Intent intent = new Intent(activity, VariableValuesActivity.class);
                  String name = ((EditText)newVariable.findViewById(R.id.variable_name)).getText().toString();
                  intent.putExtra("name", name);
                  activity.startActivity(intent);
               }
            });
            
            Button deleteButton = (Button) newVariable.findViewById(R.id.delete_variable_button);
            deleteButton.setOnClickListener(new OnClickListener() {
               public void onClick(View v) {
                  layout.removeView(newVariable);
               }
            });
            layout.addView(newVariable);
         }
      });
   }
}
