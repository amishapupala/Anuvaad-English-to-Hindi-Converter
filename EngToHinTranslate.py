#pip install flask
#>py -m venv env
#>env\scripts\activate
#>set FLASK_APP=EngToHinTranslate.py
#pip insall englisttohindi
#>flask run



from flask import *  
from englisttohindi.englisttohindi import EngtoHindi
  

app = Flask(__name__)  
 



@app.route('/')  
def message():  
      return render_template('index.html')  



@app.route('/',methods = ['POST'])  
def login():  
      messageToTranslate=request.form['inputtext'] 
      result = EngtoHindi(messageToTranslate)    
      return render_template('index.html', translatedtext=result.convert)
if __name__ == '__main__':  
   app.run()  