from flask import Flask, render_template,abort,request
app = Flask(__name__)	

import json,os
with open("msx.json") as fichero:
	datos=json.load(fichero)


## Para el despliegue de HEROKU
port=os.environ["PORT"]


## Programa para la página de inicio. 
@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("inicio.html")

## Programa para la pagina que contiene el formulario.
@app.route('/juegos',methods=['GET','POST'])
def programa_pag_juegos():

    ## CATEGORIAS DISPONIBLES
    # L_cat -> lista categorias.

    l_cat=[]

    for cat in datos:
        if cat["categoria"] not in l_cat:
            l_cat.append(cat["categoria"])

    ###########################

    if request.method == 'POST':
        

        ## bscat -> busqueda solo por categoria.
        if request.form.get("bscat"):

            con=1

            ## njxc -> nombre de los juegos por(x) categoria 
            njxc=[]
            
            b_cat=request.form.get("bscat")

            for nj in datos:
                if nj["categoria"] == b_cat:
                    dic={"numero":con,"nombre":nj["nombre"],"desarrollador":nj["desarrollador"],"id":nj["id"]}
                    njxc.append(dic)
                    con=con+1


            return render_template("template4.html",cat=b_cat,njuegos=len(njxc),lista5=njxc)
  
        
        
        elif not request.form.get("cad") and not request.form.get("ncat"):
        
            cadena=request.form.get("cadena")
        
            if len(cadena)==0:

                ## En la lista 1 se guardan todos los nombres de los juegos disponibles.
                lista1=[]

                ## nj -> nombre juego
                for nj in datos:
                    lista1.append(nj["nombre"])

                return render_template("template2.html",lista1=lista1,njuegos=len(lista1))

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
                    return render_template("template2.html",cadena=cadena)

                else:
                    return render_template("template2.html",lista2=lista2,cadena=cadena,njuegos=len(lista2))

        else:

            cadena=request.form.get("cad")
            nom_cat=request.form.get("ncat")

            ## En la lista 3 guardaremos los juegos cuyo nombre empiezan por la cadena introducida
            ## y coinciden con la categoria.

            lista3=[]

            ## En la lista 4 guardaremos el nombre de los juegos. Esta lista la utilizaremos para
            # saber si existen titulos que empiezen por dicha cadena pero que no pertenezcan a 
            # dicha categoría.

            lista4=[]
            
            con=1

            for nj in datos:
                if str(nj["nombre"]).startswith(cadena) and nj["categoria"] == nom_cat:
                    dic={"numero":con,"nombre":nj["nombre"],"desarrollador":nj["desarrollador"],"id":nj["id"]}
                    lista3.append(dic)
                    con=con+1
            
            for nj in datos:
                if str(nj["nombre"]).startswith(cadena):
                    lista4.append(nj["nombre"])

            if len(lista3) == 0:
                if len(lista4) == 0:
                    return render_template("template3.html",cadena=cadena,categoria=nom_cat)
                else:
                    return render_template("template3.html",cadena=cadena,categoria=nom_cat,nj=len(lista4))

            else:

                return render_template("template3.html",lista3=lista3,cadena=cadena,njuegos=len(lista3),nc=nom_cat)


    else:
        
        return render_template("template1.html",categorias=l_cat)

        




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
        return render_template("template5.html",nombre=nombre,detalles=detalles)


## Sirve para que escuche por cualquier puerto.
app.run('0.0.0.0',int(port), debug=True)
