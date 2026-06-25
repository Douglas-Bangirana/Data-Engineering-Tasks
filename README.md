# Data Engineering Tasks - Python Solutions

## Challenges Faced & Solutions
1. **Dynamic Counting Keys:** Hardcoding keys for tracking service variations causes scaling issues. 
   * *Solution:* Leveraged dictionary `.get(key, 0)` defaults to dynamically increment and track counts cleanly.
2. **CSV Cleanliness & Parsing Errors:** Variations in spaces and mismatched strings can easily disrupt numerical calculations.
   * *Solution:* Isolated transformations by checking field data validity via string functions (`.strip()`, `.lower()`, `.title()`) and safely managed conversions using structured `try-except` evaluation logic.

## Key Learnings
* Developed standard formatting habits for tracking internal state patterns cleanly inside loops.
* Learned how to extract headers dynamically and isolate messy lines using Python's native `csv.DictReader`.
* Gained experience creating standard automated validation logs to parse file rows against explicit rulesets.
