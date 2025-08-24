import argparse
import os
import pickle
from collections import Counter
from datasets import load_dataset

from evaluation import evaluate_solution_sets, print_metrics

parser = argparse.ArgumentParser()
parser.add_argument("--samples", required=True, type=str)
parser.add_argument('-v', '--verbose', action='store_true', help='whether to print result metrics')
parser.add_argument('-m', '--mode', help='fail_fast or eval_all', default='fail_fast')
parser.add_argument('-r', '--rs', help='file path to save results (default is results.pickle)', default='result_sets.pickle')
args = parser.parse_args()

# eval
ds = load_dataset("junhongmit/USACOBench")['test']
problem_dict = {problem["cp_id"]: problem for problem in ds}

solution_dict = {}
for task_id in os.listdir(args.samples):
    task_path = os.path.join(args.samples, task_id)
    if not os.path.isdir(task_path):
        continue

    solution_dict[task_id] = []
    for solution_id in os.listdir(task_path):
        solution_path = os.path.join(task_path, solution_id)
        if os.path.isfile(solution_path) and solution_path.endswith(".py"):
            with open(solution_path, "r") as f:
                completion = f.read()
            solution_dict[task_id].append(completion)

result_sets = evaluate_solution_sets(solution_dict, problem_dict, mode=args.mode)

# print
if args.verbose:
    print_metrics(result_sets)
    print('Result summary:')
    result_types = [result['result_type'] for result_set in result_sets for result in result_set]
    print(Counter(result_types))
    print()

# save
fname = args.rs
print('Saving results at {}...'.format(fname))
with open(fname, 'wb') as f:
    pickle.dump(result_sets, f)