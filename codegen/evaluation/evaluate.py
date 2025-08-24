import os
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Tuple, Union, Callable

from .judges.usaco_batch_judge import USACOBatchJudge

Problem = Dict[Any, Any]
Solution = Dict[str, Union[str, None]]
SolutionSet = List[Solution]
Result = Dict[str, str]
ResultSet = List[Result]

def evaluate_solution_sets(
        solution_dict: Dict[str, SolutionSet],
        problem_dict: Dict[str, Problem],
        return_solution_sets=False,
        **kwargs
    ) -> Dict[str, ResultSet]:
    judge = USACOBatchJudge()

    path = Path('judge_sandbox/predictions/')
    path.mkdir(parents=True, exist_ok=True)
    path = Path('judge_sandbox/tests/')
    path.mkdir(parents=True, exist_ok=True)
    for problem_id in solution_dict.keys():
        problem = problem_dict[problem_id]
        for idx, case in enumerate(problem["tests"], start=1):
            path = Path(f"judge_sandbox/tests/{problem["cp_id"]}")
            path.mkdir(parents=True, exist_ok=True)
            in_path = path / f"{idx}.in"
            out_path = path / f"{idx}.out"
            with open(in_path, "w", encoding="utf-8") as f:
                f.write(case["input"].rstrip() + "\n")
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(case["output"].rstrip() + "\n")
    
    result_sets = judge.judge(solution_dict, problem_dict, **kwargs)
    return result_sets
