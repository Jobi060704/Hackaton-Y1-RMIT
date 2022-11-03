import org.json.simple.JSONObject;

// class main{
//     public static void main(String[] args) {
//         JSONObject json_file = new JSONObject("AC2-07337-anon.json");
//         JSONArray the_json_array = json_file.getJSONArray("PartInformation");
//     }
// }

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.json.JSONString;    
public class JsonExample1{    
public static void main(String args[]){    
JSONObject obj=new JSONObject();    
  obj.put("name","sonoo");    
  obj.put("age",new Integer(27));    
  obj.put("salary",new Double(600000));    
   System.out.print(obj);    
}}    