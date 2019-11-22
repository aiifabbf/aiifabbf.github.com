import bottle
import os

app = bottle.Bottle()

@app.get("/<path:path>")
def serve(path: str): # simulate what happens on github pages: github returns 404.html (if exists) if resource not found
    if os.path.exists(path):
        return bottle.static_file(path, root="./")
    else:
        return bottle.static_file("404.html", root="./")

@app.get("/")
def serve():
    return bottle.static_file("404.html", root="./")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
