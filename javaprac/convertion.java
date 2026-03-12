package javaprac;
import java.util.*;
import java.io.*;
import java.net.*;


public class convertion {
    public static void main(String [] args) throws Exception{
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the Temperature in Fahreheit : ");
        double F=sc.nextDouble();
        sc.close();

        URL url = new URL("http://127.0.0.1:5245/convert");
        HttpURLConnection con=(HttpURLConnection) url.openConnection();

        con.setRequestMethod("POST");
        con.setRequestProperty("Content-Type","application/json");
        con.setDoOutput(true);

        String json ="{\"F\":" + F + "}";

        try (OutputStream os= con.getOutputStream()){
            os.write(json.getBytes());
        }

        
        BufferedReader br = new BufferedReader(
            new InputStreamReader(con.getInputStream()));
      
        String line,response="";
        while ( ((line=br.readLine()))!=null){
            response +=line;
        }

        System.out.println("ResponseCode" + con.getResponseCode());
        System.out.println("Response" + response);  


    }
    
}
