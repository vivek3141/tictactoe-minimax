# TicTacToe
TicTacToe singler player using the MINIMAX algorithm

### Requirements
```bash
pip install -r requirements.txt
```
* `PyQt5` - `pip install PyQt5`

## Running the Program
```bash 
python3 main.py
```
![UI](https://i.imgur.com/6rL8NbI.png)

Click the buttons to make a move. The first move usually takes a lot longer as there are a lot more cases to go through.

## How it works

![Source: geeksforgeeks.com](https://cdncontribute.geeksforgeeks.org/wp-content/uploads/minmax.png)
<br>
Source: geeksforgeeks.com

Minimax is a backtracking algorithm that is used to find
the optimal move for each position, assuming that the
opponent plays optimally. 

Essentially we are finding the most optimal path based off a given end result.

In the above example, the first turn attempts to maximize, whereas the turn after that is minimizing. Looking at each possible case and performing some pruning, we can figure out the best path to take. 

The first move is trying to maximize, so it would pick Left, because it assumes that the opponent will play optimally. The next move is trying to minimize, so it would pick 3, leaving us with the optimal path. 

This is generalized to tictactoe, where each parent has a lot more branches for each of the possible moves. 

Pseudocode for minimax is as follows: 
```
function minimax(node, depth, maximizingPlayer) is
    if depth = 0 or node is a terminal node then
        return the heuristic value of node
    if maximizingPlayer then
        value := −∞ 
        for each child of node do
            value := max(value, minimax(child, depth − 1, FALSE))
        return value
    else (* minimizing player *)
        value := +∞
        for each child of node do
            value := min(value, minimax(child, depth − 1, TRUE))
        return value
```
Source: wikipedia.org