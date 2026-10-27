from pyscript import document, display

nonmetals = {
    'H': ('Hydrogen', 1, 1.008),
    'C': ('Carbon', 6, 12.011),
    'N': ('Nitrogen', 7, 14.007),
    'O': ('Oxygen', 8, 15.999),
    'F': ('Fluorine', 9, 18.998),
    'P': ('Phosphorus', 15, 30.974),
    'S': ('Sulfur', 16, 32.06),
    'Cl': ('Chlorine', 17, 35.45),
    'Se': ('Selenium', 34, 78.96),
    'Br': ('Bromine', 35, 79.904),
    'I': ('Iodine', 53, 126.904),
    'He': ('Helium', 2, 4.0026),
    'Ne': ('Neon', 10, 20.180),
    'Ar': ('Argon', 18, 39.95),
    'Kr': ('Krypton', 36, 83.798),
    'Xe': ('Xenon', 54, 131.293),
    'Rn': ('Radon', 86, 222)
}

def finder(e):
    # Clear the old result box
    document.getElementById("result-box").innerHTML = ""

    # Get the symbol from the input field
    symbol = document.getElementById("symbol").value.strip()

    # Use .get() to look up the symbol, and also checks if it doesn't exist (not found)
    result = nonmetals.get(symbol, ("Element not found", "-", "-"))
    
    output_html = f"""
    <b>Symbol:</b> {symbol.title()} <br>
    <b>Element Name:</b> {result[0]} <br>
    <b>Atomic Number:</b> {result[1]} <br>
    <b>Atomic Mass:</b> {result[2]} <br>
    """
    
    # Display the result inside the result-box div
    document.getElementById("result-box").innerHTML = output_html