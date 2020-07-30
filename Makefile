GLOB := ~/Downloads/Clanceys*.pdf
export
env:
	$@
run:
	python3 flashcards.py '' 1 3 '$(GLOB)'
