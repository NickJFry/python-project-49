#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.game_even import is_even

def greet():
	print('Welcome to the Brain Games!')

welcome_user()
is_even()

def main():
	greet()


if __name__ == '__main__':
    main()
