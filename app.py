
from flask import Flask, escape, request, render_template
import pickle
    


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("2.html")

@app.route('/2', methods=['GET', 'POST'])

def prediction():
    if request.method == "POST":
        news = str(request.form['news'])
        print(news)

        predict = model.predict(vector.transform([news]))[0]
        print(predict)

        return render_template("2.html", prediction_text="News headline is -> {}".format(predict))


    else:
        return render_template("2.html")


if __name__ == '__main__':
    app.debug = True
    app.run()