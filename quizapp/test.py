import openai
import re
import time
import threading
import queue
import signal
openai.organization = "org-jKAD0Y9d2zsRXCuOQ1hQFRi4"
openai.api_key = "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" # replace with your OpenAI API key

def generate_question(topic):
    def prompt_openai():
        prompt = f"Generate a question related to {topic}"
        completions = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=60, n=1, stop=None, temperature=0.5)
        message = completions.choices[0].text
        question_match = re.search(r"\w.*\?", message)
        answer_match = re.search(r"\s-\s(.*)\n", message)
        if question_match and answer_match:
            question = question_match.group(0)
            answer = answer_match.group(1)
            return question, answer
        else:
            return None

    t = threading.Timer(30.0, lambda: None) # 12 second timeout
    t.start()
    result = prompt_openai()
    t.cancel()

    if result is not None:
        return result
    else:
        raise TimeoutError("OpenAI API call timed out")

def user_input(question_queue, result_queue):
    while True:
        question = question_queue.get()
        answer = input(f"Enter the answer for {question}: ")
        result_queue.put(answer)

questions_asked = 0
question_queue = queue.Queue()
result_queue = queue.Queue()
user_input_thread = threading.Thread(target=user_input, args=(question_queue, result_queue))
user_input_thread.start()

while questions_asked < 10:
    topic = input("Enter the topic: ")
    question, answer = generate_question(topic)
    print(f"Question {questions_asked + 1}: {question}")
    question_queue.put(question)
    user_answer = result_queue.get()
    chatgpt_response = openai.Completion.create(
        engine="davinci", prompt=f"is {user_answer} a valid answer to '{question}'?", max_tokens=1, n=1,
        stop=None, temperature=0.5).choices[0].text.strip()
    if chatgpt_response.lower() == "yes":
        print("Correct!")
    else:
        print(f"Incorrect! The correct answer is {answer}")
    questions_asked += 1

print("Thank you!")