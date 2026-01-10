# Advanced-Python-Project-Showcase
A Python project that demonstrates custom data structures (`Array`, `Grid`), algorithmic thinking, and object-oriented programming by generating a **round-robin** schedule of weekly 1:1 coffee chats.

## Problem
Given _n_ employees (where n is even), schedule weekly coffee chats so that:
- each week, every employee meets with **exactly one** other employee, and
- across the full schedule, each employee meets **every other employee exactly once**.

## Solution
The program generates **n/2 pairs per week** for **n − 1 weeks** using round-robin rotation; one position is held fixed while the others rotate each week, producing a complete set of unique pairings.
A doc string-contained sample output is included at the end of the program.
