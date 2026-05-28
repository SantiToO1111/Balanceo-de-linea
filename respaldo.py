from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("Balanceo_de_linea.html")

@app.route('/Balanceo_de_linea', methods=['GET', 'POST'])
def balanceo():
    if request.method=="POST":
        tiempo1=float(request.form.get('tiempo1'))
        tiempo2=float(request.form.get('tiempo2'))
        tiempo3=float(request.form.get('tiempo3'))
        tiempo4=float(request.form.get('tiempo4'))
        tiempo5=float(request.form.get('tiempo5'))
        tiempo6=float(request.form.get('tiempo6'))
        tiempo7=float(request.form.get('tiempo7'))
        tiempo8=float(request.form.get('tiempo8'))
        tiempo9=float(request.form.get('tiempo9'))
        tiempo10=float(request.form.get('tiempo10'))

        tiempos=[tiempo1, tiempo2, tiempo3, tiempo4, tiempo5, tiempo6, tiempo7, tiempo8, tiempo9, tiempo10]
        
        precedencia1=float(request.form.get('precedencia1'))
        precedencia2=float(request.form.get('precedencia2'))
        precedencia3=float(request.form.get('precedencia3'))
        precedencia4=float(request.form.get('precedencia4'))
        precedencia5=float(request.form.get('precedencia5'))
        precedencia6=float(request.form.get('precedencia6'))
        precedencia7=float(request.form.get('precedencia7'))
        precedencia8=float(request.form.get('precedencia8'))
        precedencia9=float(request.form.get('precedencia9'))
        precedencia10=float(request.form.get('precedencia10'))

        definir_precedencia=[precedencia1, precedencia2, precedencia3, precedencia4, precedencia5, precedencia6, precedencia7, precedencia8, precedencia9, precedencia10]

        RPW1 = tiempos[1] + tiempos[2] + tiempos[3] + tiempos[4] + tiempos[5] + tiempos[6] + tiempos[7] + tiempos[8] + tiempos[9] + tiempos[10]
        RPW2 = tiempos[2] + tiempos[3] + tiempos[4] + tiempos[5] + tiempos[6] + tiempos[7] + tiempos[8] + tiempos[9] + tiempos[10]
        RPW3 = tiempos[3] + tiempos[4] + tiempos[5] + tiempos[6] + tiempos[7] + tiempos[8] + tiempos[9] + tiempos[10]
        RPW4 = tiempos[4] + tiempos[5] + tiempos[6] + tiempos[7] + tiempos[8] + tiempos[9] + tiempos[10]
        RPW5 = tiempos[5] + tiempos[6] + tiempos[7] + tiempos[8] + tiempos[9] + tiempos[10]
        RPW6 = tiempos[6] + tiempos[7] + tiempos[8] + tiempos[9] + tiempos[10]
        RPW7 = tiempos[7] + tiempos[8] + tiempos[9] + tiempos[10]
        RPW8 = tiempos[8] + tiempos[9] + tiempos[10]
        RPW9 = tiempos[9] + tiempos[10]
        RPW10 = tiempos[10]

        
        


        return render_template("Balanceo_de_linea.html", tiempos=tiempos)
    return render_template("Balanceo_de_linea.html")