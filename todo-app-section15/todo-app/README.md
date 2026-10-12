# todo-app — Section 15 version

Python Mega Course (Udemy), **Section 15: Built-in Tools & Version Control (Standard Modules, Git)**.

A command line todo app: add, show, edit and complete todos saved in `todos.txt`.

## Run it

```
python main.py
```

```
It is Oct 12, 2026 11:42:49.
Type add, show, edit, complete or exit: add buy milk
Type add, show, edit, complete or exit: show
1-computer 2
2-buy milk
```

## What Section 15 added

| Lecture | What | Where |
|---|---|---|
| 146. Add a "Date" Feature | `import time`, `time.strftime(...)`; the app shows the date and time; `FILEPATH` constant | `main.py`, `functions.py` |
| 147. Code Experiments | standard modules `glob`, `csv`, `shutil`, `webbrowser` | `e1_glob.py` to `e4_webbrowser.py`, `weather.csv`, `files/` |
| 148. Bonus Example | JSON quiz: `json.loads`, list of dictionaries | `bonus/bonus15.py`, `bonus/questions.json` |
| 151. Using Git | project tracked with Git; `.gitignore` | `.gitignore` |

## Files

| File | What it is |
|---|---|
| `main.py` | the app (frontend: input/print) |
| `functions.py` | `get_todos()` and `write_todos()` (backend) |
| `todos.txt` | the todo data |
| `e1_glob.py` | prints every `.txt` file in `files/` |
| `e2_csv.py` | reads `weather.csv`, looks up a city's temperature |
| `e3_shutil.py` | zips the `files` folder into `output.zip` |
| `e4_webbrowser.py` | opens a Google search for your term |
| `bonus/bonus15.py` | quiz from `bonus/questions.json` |

Only standard modules are used: nothing to install.
