from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def prompt():
    return render_template('form_prompt.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
       
      state = str(request.form['state'])
      url = "https://api.schooldigger.com/v1.2/rankings/schools/"+state+"?appID=f14c813a&appKey=560e6e0400648906909977e5c7ff3a43"
      response = requests.get(url)
      data = response.text
      school_data = json.loads(data)
      schoolList_data = school_data["schoolList"][0:5]

      schoolList = [[] for school in schoolList_data]
      
      for i in range(0,5):
          schoolList[i] += [schoolList_data[i]["schoolName"]]
          schoolList[i] += [schoolList_data[i]["phone"]]
          city = schoolList_data[i]["address"]["city"]
          schoolList[i] += [city]

          url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=d8c155b6234b83e3ca5d68e3e5a6deed"
          response = requests.get(url)
          data = response.text
          weather_data = json.loads(data)

          schoolList[i] += [weather_data["weather"][0]["main"]]
      
      return render_template('form_results.html', schoolList = schoolList)
    
if __name__ == '__main__':
    app.run(debug = True)
