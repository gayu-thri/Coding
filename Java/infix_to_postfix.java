import java.util.Scanner;
import java.util.Stack;
 
class InfixToPostfix
{
    // A utility function to return precedence of a given operator
    // Higher returned value means higher precedence
    static int Prec(char ch)
    {
        switch (ch)
        {
        case '+':
        case '-':
            return 1;
      
        case '*':
        case '/':
            return 2;
      
        case '^':
            return 3;
        }
        return -1;
    }
      
    // The main method that converts given infix expression
    // to postfix expression. 
    static String infixToPostfix(String exp)
    {
        // initializing empty String for result
        String result = new String("");
         
        // initializing empty stack
        stack<Character> S = new StackArray<Character>();
        int i;
        char ch;
        
        for(i=0;i<exp.length();i++){
            
            ch = exp.charAt(i);
            if(Character.isLetter(ch))
                {
                    result += ch;
                }
            else if(ch == '(')    
                S.push(ch);
            else if(ch == ')')    
                {
                    while(!S.isEmpty() && S.top()!='(')
                           result += S.pop();
                           if(!S.isEmpty() && S.top()!='(')
                            {
                                return "Invalid Expression";
                            }
                            else
                            S.pop();
                } 
                 else if(!S.isEmpty()&&(ch=='+'||ch=='-'||ch=='/'||ch=='*')&&(ch==S.top()))
        {
              return "Invalid Expression";
        }
            else{
                   
                  while (!S.isEmpty() && Prec(ch) <= Prec(S.top()))
                    result += S.pop();
                  S.push(ch);
            }
        }
         while (!S.isEmpty())
            result += S.pop();
        
      
        return result;
    }
   
    // Driver method 
    public static void main(String[] args) 
    {
      Scanner scan = new Scanner(System.in);
      int testcases = Integer.parseInt(scan.nextLine());
        //String exp = "a+b*(c^d-e)^(f+g*h)-i";
      
      CapacityGetterSetter getset = new CapacityGetterSetter();
      getset.setCapacity(10000);
      while(testcases!=0)
      {
        String exp=scan.nextLine();
        System.out.println(infixToPostfix(exp));
        testcases--;
      }
        
    }
}
 
interface stack<E> {
  int size();
 
  boolean isEmpty();
 
  void push(E e);
 
  E pop();
 
  E top();
  
  
 
  void printStack();
}
 
class CapacityGetterSetter {
  private static int stackcap;
 
  public int getCapacity() {
    return this.stackcap;
  }
 
  public void setCapacity(int cap) {
    stackcap = cap;
  }
}
 
class StackArray<E> implements stack<E> {
  // public static final int CAPACITY=20;
  CapacityGetterSetter getset = new CapacityGetterSetter();
  private E[] data; // array container
  private int t = -1; // index to top position
  
  // constructor
  int CAPACITY=0;
 
  public StackArray() {
    CAPACITY = getset.getCapacity();
    data = (E[]) new Object[CAPACITY];
  }
 
  public int size() {
    // TODO Auto-generated method stub
    return (t + 1);
    
    
  }
 
  public boolean isEmpty() {
    // TODO Auto-generated method stub
    return (t < 0);
    
    
    
    
  }
 
  public void push(E e) {
    // TODO Auto-generated method stub
    if (size() == CAPACITY)
    {
        
        
      System.out.println("Stack full exception");
    }
    else {
      t = t + 1;
      data[t] = e;
    }
  }
 
  public E top() {
    // TODO Auto-generated method stub
    if (isEmpty())
      System.out.println("Stack Empty");
    return data[t];
  }
  
  
  
  
 
  public E pop() {
    // TODO Auto-generated method stub
    if (isEmpty()) {
      System.out.println("Stack Empty");
      return null;
    } else {
      E temp = data[t];
      data[t] = null;
      t = t - 1;
      
      
      return temp;
    }
 
  }
 
  public void printStack() {


for (int i = 0; i < CAPACITY; i++) {
      if(data[i]!=null)
      System.out.print(data[i] + " ");
    }
    System.out.println("  ");
  }
}

