class Communication
{
  public static void main(String[] args)
  {
    if (args.length > 0)
    {
      System.out.println("somethings working");
      int x = Integer.valueOf(args[0]);
      System.out.println(x);
      for (String val:args)
        System.out.println(val);
    }
    else
    {
      System.out.println("bamboom");
    }
  }
}
