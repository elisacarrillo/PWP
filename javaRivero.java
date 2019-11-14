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

        if (name.equals("f")){
          System.out.println(name);
          HttpRequest request = HttpRequest.newBuilder()
                    .GET()
                    .uri(URI.create("HTTP://192.168.1.108:8080/fwd"))
                    .setHeader("User-Agent", "Java 11 HttpClient Bot")
                    .build();

          HttpResponse<String> response = httpClient.send(request,
          HttpResponse.BodyHandlers.ofString());

          // print status code
          System.out.println(response.statusCode());

          // print response body
          System.out.println(response.body());
        }
        if (name.equals("b")){
          System.out.println(name);
          HttpRequest request = HttpRequest.newBuilder()
                    .GET()
                    .uri(URI.create("HTTP://192.168.1.108:8080/bwd"))
                    .setHeader("User-Agent", "Java 11 HttpClient Bot")
                    .build();

          HttpResponse<String> response = httpClient.send(request,
          HttpResponse.BodyHandlers.ofString());

          // print status code
          System.out.println(response.statusCode());

          // print response body
          System.out.println(response.body());
        }
        if (name.equals("l")){
          System.out.println(name);
          HttpRequest request = HttpRequest.newBuilder()
                    .GET()
                    .uri(URI.create("HTTP://192.168.1.108:8080/lt"))
                    .setHeader("User-Agent", "Java 11 HttpClient Bot")
                    .build();

          HttpResponse<String> response = httpClient.send(request,
          HttpResponse.BodyHandlers.ofString());

          // print status code
          System.out.println(response.statusCode());

          // print response body
          System.out.println(response.body());
        }
        if (name.equals("r")){
          System.out.println(name);
          HttpRequest request = HttpRequest.newBuilder()
                    .GET()
                    .uri(URI.create("HTTP://192.168.1.108:8080/rt"))
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
