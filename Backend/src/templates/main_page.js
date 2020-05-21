const url = "https://rikilg.pythonanywhere.com/";
const apiurl = url + 'api/';
const testurl = url + 'test';

function newBubble(side) {
    let chatobj = document.getElementById('bubble-template').cloneNode(true);
    if (side == "bot" || side == "Bot") {
        return chatobj;
    }
    chatobj.classList.remove('bot-side')
    chatobj.classList.add('user-side')
    return chatobj;
}

function createBubble(side, content) {
    let chatView = document.querySelector('.flex-vertical')
    let chatobj = newBubble(side)
    chatobj.children[0].innerHTML = content
    chatView.append(chatobj)
}

function testConnection() {
    fetch(testurl)
    .then(data => data.text())
    .then(res => {
        console.log(res)
        if (res == "Test Successful!") {
            console.log("Connected to server!")
        }
    })
    .catch(err => {
        console.log(err)
    })
}

function sendQuery() {
    let textbox = document.querySelector('.textbox');
    let query = textbox.value;
    textbox.value = "";
    createBubble("user", query)
    fetch(apiurl, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({query: query})
    }).then(data => data.json())
    .then(res => {
        createBubble('bot', res.response)
    })
    .catch(err => {
        console.log(err)
    })
}

function addListeners() {
    document.querySelector('.textbox').addEventListener('keyup', (k) => {
        if (k.key == "Enter") {
            sendQuery();
        }
    })
    document.querySelector('.button').addEventListener('click', (me) => {
        sendQuery();
    })
}

addListeners();
testConnection();