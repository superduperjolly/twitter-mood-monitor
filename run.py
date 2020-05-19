"""Main module to run the Dash app"""

from tw_mood_monitor.app import web_app


# Run the Dash server
if __name__ == "__main__":
    web_app.run_server(debug=True, host="0.0.0.0", port="4000")
