import requests
from flask import Flask

app = Flask(__name__)


# return the books information(ID,title) with the given topic
# this req send to the catalog server
@app.route('/search/<topic>', methods=['Get'])
def search(topic):
    response = requests.get("http://192.168.1.30:5000/search/" + topic)
    return response.content


if __name__ == '__main__':
    app.run(debug=True, port=3500)
