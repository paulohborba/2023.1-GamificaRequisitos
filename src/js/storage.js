import { application } from "./app.js";
import { ref, getStorage, uploadBytesResumable, getDownloadURL } from "https://www.gstatic.com/firebasejs/9.22.2/firebase-storage.js";
function upload_sigaa_file(update_progress, e) {
    var file = e.target.files[0];
    const storage = getStorage(application);
    const storageRef = ref(storage, '/sigaa_files/' + file.name);
    const uploadTask = uploadBytesResumable(storageRef, file);
    uploadTask.on('state_changed',
        (snapshot) => {
            var progress = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
            console.log('Upload: ' + progress + '%');
            update_progress(progress);
        },
        (error) => {
            console.log(error);
        },
        () => {
            getDownloadURL(uploadTask.snapshot.ref).then((downloadURL) => {
                console.log('File available at', downloadURL);
                alert('Envio Completo');
            });
        }
    );
}

export { upload_sigaa_file };