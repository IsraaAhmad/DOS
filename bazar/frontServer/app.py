import requests
from flask import Flask

app = Flask(__name__)


# return the books information(ID,title) with the given topic
# this req send to the catalog server
@app.route('/search/<topic>', methods=['Get'])
def search(topic):
    response = requests.get("http://192.168.1.30:5000/search/" + topic)
    return response.content

# return all information about all books
# this req send to catalog server 
@app.route('/information/all', methods=['Get'])
def information_all():
    response = requests.get("http://192.168.1.30:5000/information/all")
    return response.content

# return all information about specific book according to given ID
# this req send to catalog server 
@app.route('/information/<int:id>', methods=['Get'])
def information_id(id):
    response = requests.get("http://192.168.1.30:5000/information/" + str(id))
    return response.content
# this req will be used from the internal system by the admin in order to
#update price of specific book - it will send to catalog server
@app.route('/update_price/<int:id>', methods=['Put'])
def update_price(id):
    price = request.json['price']
    response = requests.put("http://192.168.1.30:5000/update_price/" + str(id), {'price': price})
    return response.content


if __name__ == '__main__':
    app.run(debug=True, port=3500)
