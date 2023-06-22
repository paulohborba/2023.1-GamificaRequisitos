import { getAuth, onAuthStateChanged, createUserWithEmailAndPassword, signInWithEmailAndPassword, signOut } from "https://www.gstatic.com/firebasejs/9.22.2/firebase-auth.js";
import { database, allocate_user, get_user_info_by_id, set_user_online_status } from "./database.js";
import { application } from './app.js';
let authentication = getAuth(application);
onAuthStateChanged(authentication, (user) => {
    const stored_authentication_name = 'authUid';
    if (user) {
        localStorage.setItem(stored_authentication_name, user.uid);
        set_user_online_status(user, true);
    } else {
        set_user_online_status(localStorage.getItem(stored_authentication_name), false);
        localStorage.removeItem(stored_authentication_name);
    }
});
async function create_account(type, email, password) {
    try {
        const userCredential = await createUserWithEmailAndPassword(authentication, email, password);
        const allocated_user = await allocate_user(type, userCredential.user.uid, email);
        alert('Conta Criada com Sucesso\n' + email);
        return [userCredential.user.uid, allocated_user];
    } catch (error) {
        console.log(error);
        alert('Falha no Registramento');
    }
}
async function login(email, password) {
    await signInWithEmailAndPassword(authentication, email, password)
        .then(async (userCredential) => {
            const type = await set_user_online_status(userCredential.user, true);
            let page_redirection;
            if (type == 'admin') {
                page_redirection = 'adm_index.html';
            } else if (type == 'regular') {
                page_redirection = 'student_index.html';
            }
            if (page_redirection) {
                localStorage.setItem("email", email);
                localStorage.setItem("password", password);
                localStorage.setItem('id', userCredential.user.uid);
                window.location.replace(page_redirection);
            }
        })
        .catch((error) => {
            console.log(error);
            alert('E-mail ou senha incorretos');
        });
}
function logout(redirection_page) {
    signOut(authentication)
        .then(() => {
            const uid = localStorage.getItem('authUid');
            if (uid) {
                get_user_info_by_id(uid).then(user_info => {
                    set(ref(database, '/user_registers/' + user_info[0] + '/' + uid + '/online_status'), false);
                    localStorage.removeItem('authUid');
                    if (redirection_page) {
                        window.location.replace(redirection_page);
                    }
                });
            }
        })
        .catch((error) => {
            console.log(error);
        });
}
export { authentication, create_account, login, logout };