# Makefile
rpi: #run poetry install
	poetry install

brain-games: #run brain-games
	poetry run brain-games

brain-even: #run brain-even
	poetry run brain-even

brain-calc: #run brain-calc
	poetry run brain-calc

brain-gcd: #run brain-gcd
	poetry run brain-gcd

brain-prog: #run brain-progression
	poetry run brain-progression

brain-prime: #run brain-prime
	poetry run brain-prime

build: #run poetry build
	poetry build

publish: #выполнит poetry publish --dry-run
	poetry publish --dry-run

package-install: #выполнит python3 -m pip install --user dist/*.whl
	python3 -m pip install --user dist/*.whl

lint: #запускает poetry run flake8 brain_games
	poetry run flake8 brain_games

