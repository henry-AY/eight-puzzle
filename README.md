# CS170 Eight Puzzle Problem

## Introduction
A sliding tile puzzle is a combination puzzle (see Figure 1 for an example of starting and goal state), where
you slide around a blank tile with numbered tiles, in hopes of reaching the goal state (generally tiles
arranged in sequential pieces). The most common sizes are the 3x3 (8-puzzle) and the 4x4 (15-puzzle).
In this project, I worked on the 3x3 puzzle, solving with the Uniform Cost Algorithm and A-star with
two different heuristics. Feel free to run this repository and experiment with the different algorithms and puzzles.

## Cloning the Repository

### 1. Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/<your-user-name>/eight-puzzle.git
```

### 2. Navigate into the Project Directory

```bash
cd eight-puzzle
```

### 3. Run the Program

There are **no dependencies required**. You can run the program directly with Python:

```bash
python src/main.py
```

## Command Line Options

The program supports the following CLI flags (in any combination):

### `-s`

Runs the **simple 27 depth 8 puzzle problem**.

```bash
python src/main.py -s
```

### `-d`

Enables **verbose output**.

```bash
python src/main.py -d
```

### `-dd`

Enables **more verbose output** ( detailed debugging output).

```bash
python src/main.py -dd
```
