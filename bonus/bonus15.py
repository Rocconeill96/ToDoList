import json 

try:
    with open("bonus/questions.json","r") as file:
        content = file.read()
        
    data = json.loads(content)

    print(data)
    print("type of variable 'data':", type(data))
    print("type of variable 'content':", type(content))
    
except FileNotFoundError:
    print("No good! trying an alternative")
    
    f = open("bonus/questions.json","r")
    data = json.load(f)
    print(data)
    print("type of variable 'data':", type(data))
    print("type of variable 'content':",type(content))
 

score = 0   
for question in data:
    print(question["question_text"]) 
    
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)
    
    user_answer = int(input("Enter your answer: "))
    question["user_answer"] = user_answer
    if question["user_answer"] == question["correct_answer"]:
        score+=1
        
score = 0   
for index, question in enumerate(data):
    if question["user_answer"] == question["correct_answer"]:
        score+=1
        result = "Correct Answer!"
        
    else:
        result = "Wrong Answer!"
        print(result)
    message = f"{index+1} {result} - Your answer: {question['user_answer']}, " \
              f"Correct answer: {question['correct_answer']}"      
    print(message)