# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"


# @app.route("/profile/<username>")

# def page(username):
#     return f"<h1>Hello, {username}</h1><p>This is your rakhis page.</p>"

# from flask import Flask
# app = Flask(__name__)
# print(app)   # shows the directory Flask considers as the app root

# from flask import Flask, render_template,request

# app = Flask(__name__, template_folder="../views")

# @app.route("/",methods=["POST"])
# def hello_world():
#     name = request.args.get("abc", '')
#     print(name)
#     return render_template("login.html" ,customer=name) 
     


# from flask import Flask
# app = Flask(__name__)
# @app.route("/add/<int:num1>/<int:num2>")
# def add(num1, num2):
#     result = num1 + num2
#     return f"<h1>Result: {result}</h1>"

# from flask import Flask, redirect,url_for
# """Sends the client (browser) to a different URL."""

# app = Flask(__name__)

# @app.route("/old")
# def old_page():
#     return redirect("/new")

# @app.route("/new")
# def new_page():
#     return "This is the new page"


# from flask import Flask,redirect, url_for

# app = Flask(__name__)

# @app.route("/profile/<username>")
# def profile(username):
#     return f"Profile page of {username}"

# @app.route("/")
# def home():
#     # This is safe because we are **inside a request**
#     return redirect(url_for("profile",username="alice"))
    
# from flask import Flask, redirect, url_for

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Home page"

# @app.route("/go-to-home")
# def go_home():
#     return redirect(url_for("home"))



from flask import Flask, render_template, redirect, url_for, request,jsonify
from src.config.database import fetchRaw, insertRaw, updateRaw,fetchOneRaw
from hashids import Hashids

app = Flask(__name__, template_folder='../views')


# @app.route("/urls", methods=['POST'])
# def create_url():
#     url = request.form.get('url')
#     id = insertRaw(f"INSERT INTO urls (url) values ('{url}')")
#     print(id)
#     return str(id)

@app.route("/urls", methods=['POST'])
def create_url():
    url = request.form.get('url')
    id = insertRaw(f"INSERT INTO urls (url) values ('{url}')")
    hashids = Hashids(salt='sdfhj298 u2134b132b  23y4i23h4', min_length=10)
    hashid = hashids.encode(id)
    
    updateRaw(f"UPDATE urls SET short_url = '{hashid}' where id = {id}")
    short_url = 'https://bit.ly/'+hashid
    return jsonify({'success': True, 'short_url': short_url})
    

# @app.route("/<table_name>", methods=['POST'])
# def get_list(table_name):
        
#     data = request.form.to_dict()
#     columns = ", ".join(data.keys())
#     values = "', '".join(data.values())
#     query = f"INSERT INTO {table_name} ({columns}) VALUES ('{values}')"
#     id = insertRaw(query)
#     return jsonify({"success": True, "id": id})
    





@app.route("/<table_name>", methods=['GET'])
def get_list(table_name):
    data = fetchRaw(f"select * from {table_name}")
    return jsonify({'success': True, 'data': data})


@app.route("/<table_name>/<id>", methods=['GET'])
def get_detail(table_name, id):
    data = fetchOneRaw(f"select * from {table_name} where id = {id}")
    return jsonify({'success': True, 'data': data})




# @app.route("/urls", methods=['Get'])
# def list_urls():
#     id=request.form.get('id')

# @app.route("/url/<url>", methods=['GET'])
# def get_url():
#     name = request.args.get('abcdefg')
#     return render_template(["home/sub.html", "home/index"], customer=name)

# from flask import Flask, request

# app = Flask(__name__)

# @app.route("/submit", methods=[ "GET","POST"])
# def submit():
#     if request.method == "POST":
#         name = request.form.get("name")   # take input from the form
#         return f"Hello, {name}!"
#     return '''
#         <form method="POST">
#             <label>Enter your name:</label>
#             <input type="text" name="name">
#             <input type="submit" value="Send">
#         </form>
#     '''


