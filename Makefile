build:
	docker build -t flask-basic .

run:
	docker run -dp 5000:5000 -v ${PWD}:/lab-cicd flask-basic python hello.py

unit:
	docker run -v ${PWD}:/lab-cicd flask-basic pytest .