from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<int:num1>')
@app.route('/<int:num1>/<int:num2>/')
@app.route('/<int:num1>/<int:num2>/<string:color_1>')
@app.route('/<int:num1>/<int:num2>/<string:color_1>/<string:color_2>')
def play(num1=8,num2=8,color_1='red',color_2='black'):
    size_rem = 5*num1
    return render_template('play.html',num_x=num1,num_y=num2,size_rem=size_rem,color1=color_1,color2=color_2)

if __name__ == '__main__':
    app.run(debug=True)

