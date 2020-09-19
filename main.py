# Author: Woosung Lim wml5207@psu.edu

def digit_sum(n):
   return 0 if n == 0 else int(n%10) + digit_sum(int(n//10)) 

if __name__ == "__main__":
  num=int(input("Enter an int: "))
  print(f"sum of digits of {num} is {digit_sum(num)}.")