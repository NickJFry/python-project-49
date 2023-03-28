#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.game_brain_even import is_even

def greet():
	print('Welcome to the Brain Games!')

def main():
	greet()
	welcome_user()
	is_even()


if __name__ == '__main__':
    main()
