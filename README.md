# 🌱 My Coding Journey at WeThinkCode_
**Name**: Zinhle  
**Start Date**: July 11, 2025  

## 📅 Week 0: Python Basics (Completed July 15, 2025)
### What I Learned:
- How to use `input()` and `print()`
- String methods like `.lower()` and `.replace()`
- Basic math operations

### Files Completed:
1. `indoor.py` - Makes text quiet (lowercase)
2. `playback.py` - Slows down speech with "..."
3. `faces.py` - Turns :) into 🙂 and :( into 🙁
4. `einstein.py` - Calculates E=mc²
5. `tip.py` - Calculates restaurant tips

### Big Challenges:
**July 12, 2025** - File Confusion  
- Created `hello.py` on my Desktop by mistake  
- Fixed by moving it:  
  ```bash
  mv ~/Desktop/hello.py ~/wethinkcode-pre-academy/
  
**July 13, 2025** - Git Problems
- Got "rejected" error when pushing to GitHub
- Solved with:
  ```bash
  git pull origin main
  git push origin main
  
**July 14, 2025** - Naming Issues
- Made files with spaces like Deep Thought.py
- Had to rename them:
   ```bash
   mv "Deep Thought.py" deep_thought.py

## Tools I'm Using:
- CS50 Codespace (for coding)
- GitHub (to save my work)
- VS Code (when I need to edit)

## 😅 How I Feel
- Proud I finished Week 0!
- Confused sometimes by Git
- Excited to learn conditionals next

##📝 What's Next?
cat << 'EOF' >> README.md

## Week 1: Conditional Logic (July 16-22, 2025)

### Key Learnings:
- Implemented decision-making flows with `if/elif/else` structures
- Mastered input standardization using `.lower()` and `.strip()`
- Solved time conversion challenges between 24-hour and decimal formats

### Project Highlights:
1. `deep.py` - The Ultimate Answer validator (42) 🔮  
   *Validates user input against the cosmic truth*
2. `bank.py` - Context-aware greeting analyzer 💰  
   *Financial incentive system based on greeting etiquette*
3. `extensions.py` - File type identifier 🧠  
   *Determines MIME types from file extensions*
4. `interpreter.py` - Arithmetic expression evaluator ➗  
   *Parses and computes basic math operations*
5. `meal.py` - Temporal meal detector 🍔  
   *Identifies appropriate dining periods based on time inputs*

### Confusing Moments:
**July 21:** Input validation in `deep.py`  
Refined case sensitivity handling:
```python
answer = input("...").strip().lower()  # Universal input normalization

**July 21:** Arithmetic parsing in interpreter.py
Initial implementation worked for basic cases:
```python
x, y, z = expression.split()  # Standard expression parsing
Note: Later discovered this doesn't handle negative numbers

## **Week 2: Loops**
- Practice Git commands daily
