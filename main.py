import argparse
import os
import maze as m
import elems
from robot import MoveError

def print_moves():
    print("move the robot, W|E|N|S (+ Shift), ex S3 for 3 steps South or E for one step East")

def choose_maze(maps_dir):
    map_files = next(os.walk(maps_dir))[2]
    map_file_dec = '\n'.join(map_files)
    print("Available mazes:")
    for i,f in enumerate(map_files):
        f_name = f.split(".")[0]
        print("{} - {}.".format(i+1, f_name))
    maze = None
    while not maze:
        try:
            choice = input("enter the number of a map: ")
            map_filename = map_files[int(choice) - 1]
            map_filepath = maps_dir + "/" + map_filename
            maze = m.Maze(map_filepath)
        except ValueError:
            print("number for dummys: 1,2,3,etc.")
    return maze

def play_turn(maze):
    print(maze)
    direction = None,
    shift = 1
    while direction not in {"W", "E", "N", "S"}:
        try:
            choice = input("\n> ")
            direction = choice[:1].upper()
            if len(choice) > 1:
                shift = int(choice[1:])
            else:
                shift = 1
        except ValueError:
            direction = None,
            print_moves()
        try:
            maze.robot.moveN(direction,shift)
        except MoveError as err:
            print(err)

def play(maze):
    print_moves()
    while type(maze.robot.pos.elem) is not elems.Exit:
        play_turn(maze)

if __name__ == "__main__":
    # parse command line
    parser = argparse.ArgumentParser(description='A Maze ing')
    parser.add_argument('--maps', type=str, default="maps", help='maze maps\' dir')
    args = parser.parse_args()

    #let's start playing
    maze = choose_maze(args.maps)
    print("\n*********** A Maze ing ***********!!!\n")
    play(maze)

    #we are out of the Maze
    print("*********** A Maze out ***********!!!")
    print(maze)

