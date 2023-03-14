# Makefile
rpi: #run poetry install
	poetry install

brain-games: #run brain-games
	poetry run brain-games

build: #run poetry build
	poetry build

publish: #выполнит poetry publish --dry-run
	poetry publish --dry-run

package-install: #выполнит python3 -m pip install --user dist/*.whl
	python3 -m pip install --user dist/*.whl



