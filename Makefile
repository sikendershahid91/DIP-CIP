
all:
	@echo "Usage:"
	@echo "\tmake project " 
	@echo "\tmake clean   " 

project:
	python3 src/main.py 

filter:
	python3 src/filters.py

clean:
	@echo "Cleaning project"
	@find . -name "__pycache__" | xargs rm -rf ;
	@find . -name "*~" | xargs rm -f ;
	@find . -name ".#*" | xargs rm -f ; 
	@find . -name "#*#" | xargs rm -f ;
