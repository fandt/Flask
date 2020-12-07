@app.route('/')
def hello_world():
    
    return '<html><head><b>Hello World</b></head><body>
    
@app.route('/BasicTemplate')
def BasicTemplate():
    
    return render_template('BasicTemplate.html')

@app.route('/index3rep', methods=['GET','POST'])
def index3rep():
        
    if 'POST' in request.method:
        startDate = request.form["doritos"]
        endDate = request.form["oreos"]
        fooDate = startDate,'to',endDate
        timestr = time.strftime("%Y-%m-%d")
