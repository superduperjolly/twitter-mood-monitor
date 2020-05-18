build:
	docker build -t docker-practice:latest .

run:
	docker run -it --rm -p 5000:5000 docker-practice:latest 
