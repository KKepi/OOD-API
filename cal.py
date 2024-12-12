from flask import Flask, request, jsonify, make_response, render_template, session, redirect, url_for


app = Flask(__name__)

@app.route("/add?a=<x>&b=<y>")
def add(x, y):
    """Funkce pro scitani dvou cisel.
    
    Parameters
    ----------
    x : int
        Prvni cislo pro scitani.
    y : int
        Druhe cislo pro scitani .
        
    Returns
    -------
    int
        Vysledek scitani prvniho a druheho cisla.
    string
        Chybova hlaska pri pouziti argumentu typu, ktery neni int
        
    Examples
    --------
    >>> add(7, 4)
    11
    """
    
    if x.isalpha():
        if y.isalpha():
            return "Pouzijte argumenty typu int."
        
    return x+y

@app.route("/subtract?a=<x>&b=<y>")
def sub(x, y):
    """Funkce pro nasobeni dvou cisel.
    
    Parameters
    ----------
    x : int
        Prvni cislo pro nasobeni.
    y : int
        Druhe cislo pro nasobeni.
        
    Returns
    -------
    int
        Vysledek nasobku prvniho a druheho cisla.
    string
        Chybova hlaska pri pouziti argumentu typu, ktery neni int
        
    Examples
    --------
    >>> add(7, 10)
    70
    """
    
    if x.isalpha():
        if y.isalpha():
            return "Pouzijte argumenty typu int."
    
    return x-y

@app.route("/multiply?a=<x>&b=<y>")
def mul(x, y):
    """Funkce pro nasobeni cisla <a> cislem <b>.
    
    Parameters
    ----------
    x : int
        Prvni cislo pro nasobeni.
    y : int
        Druhe cislo pro nasobeni.
        
    Returns
    -------
    int
        Vysledek nasobeni prvniho cisla druhym cislem.
    string
        Chybova hlaska pri pouziti argumentu typu, ktery neni int
        
    Examples
    --------
    >>> add(7, 10)
    70
    """
    
    if x.isalpha():
        if y.isalpha():
            return "Pouzijte argumenty typu int."    
    
    return x*y

@app.route("/divide?a=<x>&b=<y>")
def div(x, y):
    """Funkce pro deleni cisla <a> cislem <b>.
    
    Parameters
    ----------
    x : int
        Prvni cislo pro deleni.
    y : int
        Druhe cislo pro deleni.
        
    Returns
    -------
    int
        Vysledek deleni prvniho cisla druhym cislem.
    string
        Chybova hlaska pri pouziti argumentu typu, ktery neni int.
    bool
        Chybova hodnota pri deleni nulou.
        
    Examples
    --------
    >>> add(70, 10)
    7
    """
    if x.isalpha():
        if y.isalpha():
            return "Pouzijte argumenty typu int."
        
    if y == 0:
        return False
    else:
        return (x/y)

# každá funkce popis v docstringu NumPy
# v dosctringu příklady použití (otestovat modulem doctest)
# Swagger k automatické dokumentaci API
# ....

if __name__ == "__main__":
    app.run(debug=True)
