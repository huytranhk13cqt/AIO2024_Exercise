# AIO2024_Exercise

This repository contains all the weekly assignments of the AIO2024 course including practice exercises and explanations for multiple choice exercises

## Notes

0. automatically create basic folder

```bash
foreach ($week in "week1", "week2", "week3", "week4") {
    New-Item -ItemType Directory -Path $week\practice_exercise -Force
    New-Item -ItemType Directory -Path $week\multiple_choice_exercise -Force
    New-Item -ItemType File -Path $week\multiple_choice_exercise\solution_$week.md -Force
}

```

1. import function from any python files

```python
import os
import sys

# add root into sys.path
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', '..')))

try:
    from module_number.week_number.practice_exercise.python_file import function_name
except ModuleNotFoundError as e:
    print(f"Error importing module: {e}")
    print("Current sys.path:", sys.path)
```

2. avoid unexpected result from test in python file when import

```python
if __name__ == "__main__":
    # testing here...
```
