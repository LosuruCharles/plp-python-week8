# Personal Mini-Toolkit

A menu-driven Python program that bundles four small tools into one terminal app. It was built as the final project for the Python course (Week 8) and uses variables, input/output, conditionals, loops, lists and f-strings.

## What the toolkit does

When you start the program you see a welcome message and a numbered menu. After each tool finishes you return to the menu, and it keeps running until you choose **Quit**. Anything that isn't on the menu gets a polite message instead of a crash.

| # | Tool | What it does |
|---|------|--------------|
| 1 | **To-Do List** | Add, view and remove tasks that are kept while the program runs. |
| 2 | **Calculator** | Takes two numbers and an operator (`+`, `-`, `*`, `/`) and shows the result. Handles bad input and divide-by-zero. |
| 3 | **Number Guessing Game** | Picks a secret number from 1 to 100; you get 7 tries with "too high / too low" hints and a list of your guesses at the end. |
| 4 | **Expense Tracker** | Records expenses with amounts and shows the full list with the total. |
| 5 | **Quit** | Says goodbye and ends the program. |

## How to run it

1. Install [Python 3](https://www.python.org/downloads/) (any recent version).
2. Download or clone this repository.
3. Open a terminal in the project folder and run:

```bash
python toolkit.py
```

(On some systems use `python3 toolkit.py`.)

Data such as tasks and expenses lives in lists in memory, so it is cleared when you quit.

## Files

- `toolkit_plan.txt` — my plan: tools, menu text and the concepts each tool uses
- `toolkit.py` — the program
- `screenshots/` — the menu (including an invalid choice) and each tool running

## Reflection

<!-- WRITE THIS IN YOUR OWN WORDS (5-8 sentences). Replace everything below, including this comment. -->

The hardest part of this project was **[the part that was hardest for you, e.g. keeping the menus and nested loops straight]** because **[why]**. The bug that took me longest to fix was **[describe the bug, what you saw, and what finally fixed it]**. I learned that **[one thing you learned, e.g. checking input before converting it]**. Testing every menu path, including bad input, showed me **[something you noticed]**. If I had one more week, I would add **[your idea, e.g. saving tasks to a file, a unit converter, or a high-score list]** because **[why]**.