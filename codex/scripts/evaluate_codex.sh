#!/bin/bash
set -e

if [ $# -ne 1 ]; then
    echo "Usage: $0 <samples_directory>"
    exit 1
fi

SAMPLES_DIR="$1"

export PYTHONPATH=$PYTHONPATH:$(pwd)
python codegen/evaluate_solution.py --samples "$SAMPLES_DIR" --verbose