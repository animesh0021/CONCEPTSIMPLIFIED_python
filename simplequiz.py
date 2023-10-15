

print("Welcome to the Indian Geography Quiz!")

questions =[
    "What is the capital of India?", 
    "What is the currency of India?", 
    "What is the national bird of India?", 
    "What is the national animal of India?", 
    "Which of the following rivers has its origin in Mahabaleshwar?",
    "What is the name of India's largest desert?"
]

choices = [
    ["Mumbai", "New Delhi", "Kolkata", "Chennai"], 
    ["Dollar", "Euro", "Pound", "Rupee"], 
    ["Peacock", "Owl", "Eagle", "Pigeon"], 
    ["Tiger", "Lion", "Leopard", "Elephant"], 
    ["Kaveri", "Krishna", "Narmada", "Godavari"],
    ["Patagonian Desert","Kalahari Desert","Thar Desert","Gobi Desert"]
]

answers = [1, 3, 0, 0, 1, 2]

score = 0

for i in range(6):
    print("\nQuestion", i+1)
    print(questions[i])
    for j in range(4):
        print(j+1, choices[i][j])
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer == answers[i]+1:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {choices[i][answers[i]]}")
    print("Your current score is:", score)

print("\nThanks for playing! Your final score is:", score,"of out of 6")
