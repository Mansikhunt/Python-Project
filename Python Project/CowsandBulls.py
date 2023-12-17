import random

def generate_secret_code(length):
    return [random.randint(0, 9) for _ in range(length)]

def evaluate_guess(secret_code, guess):
    cows = sum((1 for x, y in zip(secret_code, guess) if x == y))
    bulls = sum((1 for x in guess if x in secret_code)) - cows
    return cows, bulls

def main():
    print("Welcome to the Cows and Bulls Game!")
    code_length = 4
    secret_code = generate_secret_code(code_length)
    
    attempts = 0
    
    while True:
        
        guess_str = input(f"Enter your guess (a {code_length}-digit number): ")
        
        
        if not guess_str.isdigit() or len(guess_str) != code_length:
            print("Invalid input. Please enter a valid guess.")
            continue
        
        guess = [int(digit) for digit in guess_str]
        
        cows, bulls = evaluate_guess(secret_code, guess)
        
        print(f"Result: {cows} cows, {bulls} bulls")
        
        if cows == code_length:
            print(f"Congratulations! You guessed the secret code {secret_code} in {attempts} attempts.")
            break
        
        attempts += 1

if __name__ == "__main__":
    main()
