import math

def is_palindrome(s):
    s_clean = s.lower().replace(" ", "")
    is_pal = s_clean == s_clean[::-1]
    char_freq = {}
    for char in s_clean:
        char_freq[char] = char_freq.get(char, 0) + 1
    return is_pal, char_freq

import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def main():
    results = []
    error_logs = []

    for _ in range(3):  
        try:
            
            user_string = input("Enter a string to check if it's a palindrome: ")
            palindrome_result, char_freq = is_palindrome(user_string)
            print(f"Palindrome: {palindrome_result}, Frequencies: {char_freq}")

            
            user_number = input("Enter a number to check if it's a prime: ")
            user_number = int(user_number) 
            prime_results = is_prime(user_number)
            print(f"Prime number results: {prime_results}")

          
            results.append({
                'user_input': user_string,
                'palindrome_check': (palindrome_result, char_freq),
                'prime_check': prime_results
            })
            break 

        except ValueError as e:
            error_logs.append((user_number, str(e)))
            print(f"Invalid input: {e}. Please enter a valid input.")
            if _ == 2:  
                print("Error logs:", error_logs)
                break

    
    print("Results:", results)

if __name__ == "__main__":
    main()