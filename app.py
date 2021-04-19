from urllib import request
from flask import Flask, request

app = Flask(__name__)
ListOfMessages = []


@app.route('/')
def hello_world():
    return 'Messenger Flask server is running!' \
           '<br> <a href="/status">Check status</a>'


@app.route('/status')
def status():
    return {'messages_count': len(ListOfMessages)}


@app.route('/api/Messenger', methods=['POST'])
def sendMessage():
    msg = request.json
    print(msg)
    ListOfMessages.append(msg)
    msg_text = f"{msg['UserName']} <{msg['TimeStamp']}>: {msg['MessageText']}"
    print(f"Всего сообщений: {len(ListOfMessages)} Посланное сообщение: {msg_text}")
    return f"Сообщение отослано успешно. Всего сообщений: {len(ListOfMessages)}", 200


@app.route('/api/Messenger/<int:id>')
def getMessage(id):
    print(id)
    if 0 <= id < len(ListOfMessages):
        print(ListOfMessages[id])
        return ListOfMessages[id], 200
    else:
        return "Not Found", 404


if __name__ == '__main__':
    app.run()
