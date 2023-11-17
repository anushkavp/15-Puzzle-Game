
from pynput import keyboard
from pynput.keyboard import Key
import numpy as np
import pandas as pd
import random


def generate_random_matrix():
    matrix_board = [[0] * 4 for _ in range(4)]

    numbers = list(range(1, 16))
    random.shuffle(numbers)

    for i in range(4):
        for j in range(4):
            if numbers:
                matrix_board[i][j] = numbers.pop(0)

    return matrix_board

def isSolvable(matrix_board):
    flat_array = [num for row in matrix_board for num in row]
    inv_count = getInvCount(flat_array)
    return inv_count % 2 == 0

def getInvCount(arr):
    inv_count = 0
    empty_value = 0

    for i in range(0, 16):
        for j in range(i + 1, 16):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1

    return inv_count

# Generate a solvable matrix
solvable_matrix = None
while not solvable_matrix:
    candidate_matrix = generate_random_matrix()
    if isSolvable(candidate_matrix):
        solvable_matrix = candidate_matrix


# for row in solvable_matrix:
#     print(row)
# print(type(solvable_matrix))
# print(type(np.array(solvable_matrix)))
# print(np.shape(np.array(solvable_matrix)))

matrix_board = np.array(solvable_matrix)#np.array([solvable_matrix[i:i+4] for i in range(0, len(solvable_matrix), 4)])

def print_15_puzzle(matrix_board):
    print("15 puzzle game:")
    if(matrix_board.size!=16):
        print("Incorrect input to print function. Length is not equal to 16")
    else:
        print("+----+----+----+----+")
        for row in matrix_board:
            print("|", end="")
            for num in row:
                if(num==0):
                    print("    |", end="")
                else:
                    print(f" {num:2} |", end="")
            print("\n+----+----+----+----+")
            
            
def move(board, direction):
    print("You have chosen to move in the ",direction,"direction.")
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:  # Find the blank space
                if direction == "up" and i < 3:
                    board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
                    return
                elif direction == "down" and i > 0:
                    board[i][j], board[i - 1][j] = board[i - 1][j], board[i][j]
                    return
                elif direction == "left" and j < 3:
                    board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
                    return
                elif direction == "right" and j > 0:
                    board[i][j], board[i][j - 1] = board[i][j - 1], board[i][j]
                    return
       
  
def is_puzzle_solved(board):
    flat_array = board.flatten()
    sorted_array = list(range(1,16))+[0]
    return (sorted_array == flat_array).all()
                


def on_key_release(key):
    if key == Key.right:
        print("Right key clicked")
    elif key == Key.left:
        print("Left key clicked")
    elif key == Key.up:
        print("Up key clicked")
    elif key == Key.down:
        print("Down key clicked")
    elif key == keyboard.Key.esc:
        exit()



def on_key_release(key):
    if key == Key.right:
        move(matrix_board, "right")
    elif key == Key.left:
        move(matrix_board, "left")
    elif key == Key.up:
        move(matrix_board, "up")
    elif key == Key.down:
        move(matrix_board, "down")
    elif key == keyboard.Key.esc:
        exit()
    print_15_puzzle(matrix_board)
    if is_puzzle_solved(matrix_board):
        print("CONGRATULATIONS, you won the game!!")
        exit()


print("Let's play the game")
print("Use your arrow keys to move the box tiles up, down, left or right until the numbers are sequentially arranged from 1 to 15.")
print("Good Luck!! \n\n\n")
print_15_puzzle(matrix_board)

with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()

