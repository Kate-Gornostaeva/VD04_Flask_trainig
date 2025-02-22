from flask import Flask, render_template
from datetime import datetime

app = Flask (__name__)

@app.route("/")
def First():
    return render_template("first.html")

@app.route("/second/")
def Second():
    return render_template("second.html")

@app.route("/third/")
def Third():
    return render_template("third.html")


@app.route("/date")
def show_date():
    now = datetime.now()
    current_time_date = now.strftime("%d-%m-%Y")
    current_time_time = now.strftime("%H:%M:%S")

    return f"""
        <h3>Текущая дата:</h3>
        <p>{current_time_date}</p>
        <h3>Текущее время:</h3>
        <p>{current_time_time}</p>
        <p><a href="/">Вернуться на главную</a></p>
        """
if __name__ == "__main__":
    app.run()