import bottle

app = bottle.Bottle()

@app.error(404)
def index(code):
	print(code)
	return bottle.static_file("404.html", root=".")

@app.get("/<fp:path>")
def static(fp):
	bottle.response.content_type = "application/json"
	return bottle.static_file(fp, root=".")

app.run(port=80, debug=True, reloader=True)