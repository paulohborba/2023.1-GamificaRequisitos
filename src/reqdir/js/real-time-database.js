import { getDatabase, ref, push, onValue } from "../../node_modules/firebase/firebase-database.js";
const db = getDatabase();
var nameInput = document.getElementById('nameInput');
var ageInput = document.getElementById('ageInput');
var addButton = document.getElementById('addButton');
var usersList = document.getElementById('usersList');

addButton.addEventListener(
    'click',
    function () {
        create(nameInput.value, ageInput.value)
    }
)

function create(name, age) {
    var data = {
        name: name,
        age: age
    }
    return push(ref(db, 'users'), data);
}

onValue(ref(db, 'users'), (snapshot) => {
    usersList.innerHTML='';
    snapshot.forEach((item) => {
        var li=document.createElement('li');
        li.appendChild(document.createTextNode(item.val().name+' : '+item.val().age));
        usersList.appendChild(li);
    });
});