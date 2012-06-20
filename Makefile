init:
	pip install -r requirements.txt

freeze:
	rm -fr requirements.txt
	pip freeze >requirements.txt

serve:
	rerun -p "**/*.py" foreman start