package com.gooble.logic.app.db;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteDatabase.CursorFactory;
import android.database.sqlite.SQLiteOpenHelper;

public class DatabaseHelper extends SQLiteOpenHelper{

   public DatabaseHelper(Context context, String name, CursorFactory factory, int version) {
      super(context, name, factory, version);
   }

   @Override
   public void onCreate(SQLiteDatabase db) {
      new AllTables().create(db);
   }

   @Override
   public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
      new AllTables().drop(db);
   }

}
