## Sudoku Solver by:
### _De Heuristische Helden_

## Python version

3.x

## Synopsis

This program can solve a sudoku in .csv format.
The program uses a dictionary data structure in order to solve the given
sudoku. It uses a depth-first search, implemented iteratively with .

## Usage

In order to run the program run ```python solver.py filename``` with
'filename'  being the filename of the sudoku in .csv format.

## Heuristics

The program makes use of pruning by elimination in the function *reduce_ss* by determining which options are forfeit.


## Requirements

The program does not use any external libraries.

## Contributors

The program was written by Angelo Groot, with as challengers Joeri Fresen and
Tamar Vis.
