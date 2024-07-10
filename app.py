from flask import Flask, request, jsonify

app = Flask(__name__)

 
@app.route('/')
def index():
 return 'Hello world'

#Dynamic Routing
"""@app.route('/<name>')
def print_name(name):
 return 'Hi, {}'.format(name)"""

#Books Api
books_list = [
  {
    'id': 0,
    'author': "Tarikul Abir",
    'language': "English",
    'title': "Python Programming"
  },
  {
    'id': 0,
    'author': "Tarikul Abir",
    'language': "English",
    'title': "Python Programming"
  },{
    'id': 0,
    'author': "Tarikul Abir",
    'language': "English",
    'title': "Python Programming"
  }
]
@app.route('/books', methods=['GET', 'POST'])
def books():
 if request.method == 'GET':
   if len(books_list) > 0:
      return jsonify(books_list)
   else:
     'Nothing Found', 404
 if request.method == 'POST':
   new_author = request.form['author']
   new_lang = request.form['language']
   new_title = request.form['title']
   iD = books_list[-1]['id']+1

   new_obj = {
     'id': iD,
     'author': new_author,
     'language': new_lang,
     'title': new_title
   }
   books_list.append(new_obj)
   return jsonify(books_list), 201
   





if  __name__ == "__main__":
    app.run(debug=True)