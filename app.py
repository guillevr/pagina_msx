from flask import Flask, render_template,abort,request
app = Flask(__name__)	

import json
with open("msx.json") as fichero:
	datos=json.load(fichero)



## Programa para la página de inicio. 
@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("inicio.html")

## Programa para la pagina que contiene el formulario.
@app.route('/juegos')
def pag_juegos():
    return render_template("form_juegos.html")

## Programa formulario.
@app.route('/listajuegos',methods=["POST"])
def lista_juegos():

    cadena=request.form.get("cadena")

    if len(cadena)==0:

        ## En la lista 1 se guardan todos los nombres de los juegos disponibles.
        lista1=[]

        ## nj -> nombre juego
        for nj in datos:
            lista1.append(nj["nombre"])

        return render_template("lista_juegos.html",lista1=lista1,njuegos=len(lista1))

    else:
        
        ## En la lista 2 se guardan los juegos cuyo nombre empiezan por la cadena introducida.
        lista2=[]
        con=1
       
        for nj in datos:
            if str(nj["nombre"]).startswith(cadena):
                dic={"numero":con,"nombre":nj["nombre"],"desarrollador":nj["desarrollador"],"id":nj["id"]}
                lista2.append(dic)
                con=con+1
    
        if len(lista2) == 0:
            return render_template("lista_juegos.html",cadena=cadena)

        else:
            return render_template("lista_juegos.html",lista2=lista2,cadena=cadena,njuegos=len(lista2))

## Programa para la pagina de los datos del juego
@app.route('/juego/<int:identificador>')
def detalles_juegos(identificador):

    detalles=[]

    for juego in datos:
        if juego["id"]==identificador:
            nombre=juego["nombre"]
            dic={"id":juego["id"],"nombre":juego["nombre"],"sistema":juego["sistema"],"distribuidor":juego["distribuidor"],"desarrollador":juego["desarrollador"],"categoria":juego["categoria"],"año":juego["año"]}
            detalles.append(dic)

    if len(detalles) == 0:
        abort(404)
    else:
        return render_template("detalle_juego.html",nombre=nombre,detalles=detalles)

##

app.run(debug=True)
