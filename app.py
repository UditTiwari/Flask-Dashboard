from flask import Flask,render_template
import csv

app = Flask(__name__)

# https://www.chartjs.org/

csv_file_path = 'flask_env\data.csv'

@app.get('/')
def home():
    data = read_csv(csv_file_path)
    # return csv_data
    return render_template('dashboard.html',data=data)

def read_csv(csv_file):
    with open(csv_file,'r') as f:
        csv_reader = csv.DictReader(f)
        data = [row for row in csv_reader]
    return data


if __name__=='__main__':
    app.run(debug=True)