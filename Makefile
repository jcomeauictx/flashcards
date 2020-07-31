GLOB ?= ~/Downloads/Clanceys*.pdf
#GLOB ?= ~/Downloads/*Definitions.docx.pdf
export
env:
	$@
run:
	python3 flashcards.py '' 1 3 '$(GLOB)'
