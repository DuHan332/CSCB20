from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to my CSCB20 website!"
    
@app.route("/<section>")
def data(section):
    return "Welcome, " + generateResponse(section) + ", to my CSCB20 website!"
    

def generateResponse(visitor:str):
    if visitor.isalpha():
        if visitor.isupper():
            return visitor.lower()
        elif visitor.islower():
            return visitor.upper()
        else:
            return visitor
    else:
        name = ""
        for char in visitor:
            if char.isalpha():
                name=name+char
        return name

if __name__ == "__main__":
    app.run(debug=True)