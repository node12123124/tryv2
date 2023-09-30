from flask import Flask, request, jsonify
import openai
# import bardapi
import os
from test import get_chatgpt_response
app = Flask(__name__)
from concurrent.futures import ThreadPoolExecutor
import threading
curr_dir = os.path.dirname(os.path.abspath(__file__))
problems_dir = os.path.join(curr_dir,"problems/")
solutions_dir = "solution/"
# Send an API request and get a response.

@app.route('/solve', methods=['GET'])
def solve_problem():
    # Get the coding problem from the request
    # data = request.get_json()
    problem = request.args.get('problem', '')

    if not problem:
        return jsonify({'error': 'Please provide a coding problem'}), 400

    # print(response.choices[0])
    # solution = response.choices[0].text.strip()

    solution = get_chatgpt_response(problem)
    return jsonify({'solution': solution})


@app.route('/save', methods=['GET'])
def save_problem():
    
    problem_id = request.args.get('id', '')
    problem = request.args.get('problem', '')

    if not problem:
        return jsonify({'error': 'Please provide a coding problem'}), 400

    # Save the coding problem to a file
    problem_file_name = f"{problems_dir}{problem_id}.txt"
    with open(problem_file_name, 'w') as problem_file:
        problem_file.write(problem)

    return jsonify({'message': 'Problem saved successfully'})


def solve_problem_from_file(problem_id):
    problem_file_name = os.path.join(problems_dir, f"{problem_id}.txt")
    solution_file_name = os.path.join(solutions_dir, f"{problem_id}_solution.txt")

    try:
        # Read the coding problem from the specified file
        with open(problem_file_name, 'r') as problem_file:
            problem = problem_file.read()

        # Call the ChatGPT API to generate a solution  
        response = get_chatgpt_response(problem)

        # Save the solution to the specified file
        with open(solution_file_name, 'w') as solution_file:
            solution_file.write(response)

        print({'message': 'Problem solved and solution saved successfully'})
        return 
    except Exception as e:
        return {'error': str(e)}


@app.route('/invoke/<problem_id>', methods=['GET'])
def invoke_problem(problem_id):
    thread = threading.Thread(target=solve_problem_from_file, args=(problem_id,))
    thread.daemon = True
    thread.start()
    return jsonify({'message': 'Problem received and is being solved in the background'})

# @app.route('/reset', methods=['GET'])
# def reset_ip():

@app.route('/solution/<problem_id>', methods=['GET'])
def get_solution(problem_id):
    solution_file_name = os.path.join(solutions_dir, f"{problem_id}_solution.txt")
    with open(solution_file_name, 'r') as s:
        solution = s.read()

    if 'error' in solution:
        return jsonify({'error': solution['error']}), 500
    else:
        return jsonify({'solution': solution}), 200

if __name__ == '__main__':
    app.run(debug=True)
