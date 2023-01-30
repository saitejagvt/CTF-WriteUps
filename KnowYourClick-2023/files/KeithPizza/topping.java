import java.util.Scanner;

    public static void main(String[] args)
    {
        Scanner s = new Scanner(System.in);
        String input = s.next();
        if(input.length() != 9)
        {
            System.out.println("WRONG: try again! ");
            input = s.next();
        }
        else
        {
            String solution = change1(change2(input));
            if(solution == "djckktjbq")
                System.out.println("The flag is: " + input);
            else
            {
                System.out.println("WRONG: try again! ");
                input = s.next();
            }
        }
    }
    public static String change1(String w)
    {
        int[] vary = {4, 3, 5, 6, 1, 2, 3, 3, 1};
        char[] temp = new char[9];
        for(int i = 0; i < 9; i++)
        {
            temp[i] = (char)(w.charAt(i) + vary[i]);
        }
        return new String(temp);
    }
    public static String change2(String w)
    {
        int[] vary = {1, 7, 5, 3, 5, 4, 2, 6, 3};
        char[] temp = new char[9];
        for(int i = 0; i < 9; i++)
        {
            temp[i] = (char)(w.charAt(i) - vary[i]);
        }
        return new String(temp);
    }