import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;

public class Java11HttpClientExample {

    // one instance, reuse
    private final HttpClient httpClient = HttpClient.newBuilder()
            .version(HttpClient.Version.HTTP_2)
            .build();

    public static void main(String[] args) throws Exception {

      Java11HttpClientExample obj = new Java11HttpClientExample();

      System.out.println("Testing 1 - Send Http GET request");
      obj.sendGet();

      //System.out.println("Testing 2 - Send Http POST request");
      //obj.sendPost();


    }

    private void sendGet() throws Exception {
      int lap = 0;

      for(;lap<1;){
        // Using Console to input data from user
        String name = System.console().readLine();

        if (name.charAt(0) == 'f'){
          System.out.println(name);
          String bam = "" + name.charAt(1);
          System.out.println(bam);
          //char f = name.charAt(1);
          //int kay = f - '0';

          //int bam = Integer.parseInt(name.charAt(1));
          HttpRequest request = HttpRequest.newBuilder()
                    .GET()
                    .uri(URI.create("HTTP://192.168.1.108:8080/fwd/" + bam))
                    .setHeader("User-Agent", "Java 11 HttpClient Bot")
                    .build();

          HttpResponse<String> response = httpClient.send(request,
          HttpResponse.BodyHandlers.ofString());

          // print status code
          System.out.println(response.statusCode());

          // print response body
          System.out.println(response.body());
        }
        if (name.charAt(0) == 'b'){
          System.out.println(name);
          String bam = "" + name.charAt(1);
          System.out.println(bam);
          HttpRequest request = HttpRequest.newBuilder()
                    .GET()
                    .uri(URI.create("HTTP://192.168.1.108:8080/bwd/"+bam))
                    .setHeader("User-Agent", "Java 11 HttpClient Bot")
                    .build();

          HttpResponse<String> response = httpClient.send(request,
          HttpResponse.BodyHandlers.ofString());

          // print status code
          System.out.println(response.statusCode());

          // print response body
          System.out.println(response.body());
        }
        if (name.charAt(0) == 'l'){
          System.out.println(name);
          //String bam = "" + name.charAt(1);
          //System.out.println(bam);
          //String f = name.charAt(1) + name.charAt(2);
          String kate = name.substring(1);
          int kay = Integer.parseInt(kate);
          int mam = 0;
          //int final = 0;
          mam =  kay /180;
          String final1 = Integer.toString(mam);

          HttpRequest request = HttpRequest.newBuilder()
                    .GET()
                    .uri(URI.create("HTTP://192.168.1.108:8080/lt/"+final1))
                    .setHeader("User-Agent", "Java 11 HttpClient Bot")
                    .build();

          HttpResponse<String> response = httpClient.send(request,
          HttpResponse.BodyHandlers.ofString());

          // print status code
          System.out.println(response.statusCode());

          // print response body
          System.out.println(response.body());
        }
        if (name.charAt(0) == 'r'){
          System.out.println(name);
          String kate = name.substring(1);
          int kay = Integer.parseInt(kate);
          int mam = 0;
          //int final = 0;
          mam =  kay /180;
          String final1 = Integer.toString(mam);
          HttpRequest request = HttpRequest.newBuilder()
                    .GET()
                    .uri(URI.create("HTTP://192.168.1.108:8080/rt/" + final1))
                    .setHeader("User-Agent", "Java 11 HttpClient Bot")
                    .build();

          HttpResponse<String> response = httpClient.send(request,
          HttpResponse.BodyHandlers.ofString());

          // print status code
          System.out.println(response.statusCode());

          // print response body
          System.out.println(response.body());
        }
        if(name.equals("e")){
          lap = 1;
        }
      }










    }


}
