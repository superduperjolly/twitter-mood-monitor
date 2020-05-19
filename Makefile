build:
	docker build -t twitter-mood-monitor:latest .

run:
	docker run -it --rm -p 5000:4000 twitter-mood-monitor:latest 

process_tweets:
	python tw_mood_monitor/nlp_tools.py
