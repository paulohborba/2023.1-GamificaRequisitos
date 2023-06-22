import { getDatabase, onValue, ref, get, set } from "https://www.gstatic.com/firebasejs/9.22.2/firebase-database.js";
import { application } from './app.js';
const database = getDatabase(application);
async function allocate_user(type, id, email) {
    let allocation_data;
    if (type == 'admin') {
        allocation_data = {
            'online_status': false,
            'email': email,
        };
    } else if (type == 'regular') {
        allocation_data = {
            'online_status': false,
            'name': '<sem_nome>',
            'email': email,
            'team': '<sem_grupo>',
        };
    } else {
        console.log('invalid type:');
        return;
    }
    const self_reference=ref(database, '/user_registers/' + type + '/' + id);
    await set(self_reference, allocation_data);
    return self_reference;
}
function get_directory_snapshot_value(directory) {
    return get(ref(database, directory))
        .then((snapshot) => {
            if (snapshot.exists()) {
                return snapshot.val();
            } else {
                return null;
            }
        });
}
async function get_user_info_by_id(id) {
    let snapshot = await get_directory_snapshot_value('/user_registers/admin/');
    for (let key in snapshot) {
        if (key == id) {
            return ['admin', snapshot[key]];
        }
    }
    snapshot = await get_directory_snapshot_value('/user_registers/regular/');
    for (let key in snapshot) {
        if (key == id) {
            return ['regular', snapshot[key]];
        }
    }
    return [null, null];
}

async function get_online_users() {
    let online_users = [];
    let snapshot = await get_directory_snapshot_value('/user_registers/admin/');
    if (snapshot) {
        for (let key in snapshot) {
            if (snapshot[key].online_status) {
                online_users.push(snapshot[key]);
            }
        }
    }
    snapshot = await get_directory_snapshot_value('/user_registers/regular/');
    if (snapshot) {
        for (let key in snapshot) {
            if (snapshot[key].online_status) {
                online_users.push(snapshot[key]);
            }
        }
    }
    return online_users;
}
async function set_user_online_status(userOrUid, status) {
    let id = typeof userOrUid === 'string' ? userOrUid : userOrUid.uid;
    const [type] = await get_user_info_by_id(id);
    if(type !== null){
        set(ref(database, '/user_registers/' + type + '/' + id + '/online_status'), status);
        return type;
    } else {
        console.error("Invalid user type");
    }
}
export { database, onValue, ref, set, allocate_user, get_user_info_by_id, get_online_users, set_user_online_status };
