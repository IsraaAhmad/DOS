from flask import Flask,jsonify,request
import sqlite3


app = Flask(__name__)

def data_base(stetment):
    #database connection
    sqliteConnection = sqlite3.connect('catalogDB.db')
    cursor = sqliteConnection.cursor()
    #execute sql quary
    count  = cursor.execute(stetment)
    rows = cursor.fetchall()
    sqliteConnection.commit()
    cursor.close()
    sqliteConnection.close()
    return rows

#search function,return the information (ID,title) about the book with diven topic
@app.route('/search/<topic>', methods=['Get'])
def search(topic):
    topic1 = topic.replace("%20"," ")
    sqlite_query = 'select ID,title from catalog where topic = "' + topic1+'"'
    rows = data_base(sqlite_query)
    response = []
    for i in rows:
        dic = dict (ID = i[0], title = i[1])
        response.append(dic)
    return jsonify({'response': response})


#return the information of all books
@app.route('/information/all', methods=['Get'])
def information_all():
    sqlite_query = 'select * from catalog'
    rows = data_base(sqlite_query)
    response = []
    for i in rows:
        dic = dict (ID = i[0], title = i[1],price = i[2],quantity = i[3],topic = i[4])
        response.append(dic)
    return jsonify({'response': response})


#return the information for specific book according to given id
@app.route('/information/<int:id>', methods=['Get'])
def information_id(id):
    sqlite_query = 'select * from catalog where ID='+str(id)
    rows = data_base(sqlite_query)
    response = []
    for i in rows:
        dic = dict (ID = i[0], title = i[1],price = i[2],quantity = i[3],topic = i[4])
        response.append(dic)
    return jsonify({'response': response})


#check if the book is excit and update price
@app.route('/update_price/<int:id>', methods=['Put'])
def update_price(id):
    sqlite_query1 = 'select * from catalog where ID='+str(id)
    rows1 = data_base(sqlite_query1)
    if len(rows1)== 0:
        return "the book is not exist"
    price = request.form.get('price')
    sqlite_query = 'update catalog set price ='+str(price)+' where ID ='+str(id)
    rows = data_base(sqlite_query)
    return "price updated sucsesfully"



if __name__ == '__main__':
    app.run(debug=True, port=3500)



