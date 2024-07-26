ef perform_integer_division():
  
    n = int(input())
    
    for _ in range(n):
        
        a, b = input().split()
        
        try:
           
            result = int(a) // int(b)  
            print(result)
        except ZeroDivisionError as e:
            
            print("Error Code:", e)
        except ValueError as e:
           
            print("Error Code:", e)

perform_integer_division()
