from flask import Flask, render_template, redirect, jsonify


app = Flask(__name__)



@app.route("/")
def home():

    # Find one record of data from the mongo database

    # Return template and data
    return render_template("dashboard.html")


@app.route("/barchart")
def Barcharts():

    # Return template and data
    return render_template("Barchart.html")

@app.route("/code")
def coding():

    # Return template and data
    return render_template("code.html")

@app.route("/video")
def Videos():

    # Return template and data
    return render_template("video.html")

@app.route("/maps")
def Maps():

    # Return template and data
    return render_template("Map.html")

@app.route("/drugcost")
def drgcosts():

    # Return template and data
    return render_template("Drugcost.html")


@app.route("/frequent")
def FP():

    # Return template and data
    return render_template("FruentlyP.html")

@app.route("/insulins")
def Insulin():

    # Return template and data
    return render_template("Insulins.html")

@app.route("/tiotropium")
def Tiotro():

    # Return template and data
    return render_template("Tiotropium.html")

@app.route("/esomerprazole")
def Esomerpra():

    # Return template and data
    return render_template("Esomerprazole.html")

@app.route("/rouvastatin")
def Rouvasta():

    # Return template and data
    return render_template("Rouvastatin.html")

@app.route("/hydroco")
def Narcotics():

    # Return template and data
    return render_template("Hydrocodone.html")

@app.route("/opioids")
def Opio():

    # Return template and data
    return render_template("Opioids.html")




if __name__ == '__main__':
    app.run(debug=True)