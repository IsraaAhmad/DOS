from flask import Flask,jsonify
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
    return jsonify({'response': rows})


if __name__ == '__main__':
    app.run(debug=True, port=3500)

