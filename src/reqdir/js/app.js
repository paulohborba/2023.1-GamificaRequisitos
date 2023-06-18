import { getDatabase } from "../../node_modules/firebase/firebase-database";
import { initializeApp } from "../../node_modules/firebase/firebase-app";

const firebaseConfig = {
  apiKey: "AIzaSyA224zrzRZ7Iy7rrNRE9dWCUs-Kr23ktiE",
  authDomain: "disciplinareq.firebaseapp.com",
  databaseURL: "https://disciplinareq-default-rtdb.firebaseio.com",
  projectId: "disciplinareq",
  storageBucket: "disciplinareq.appspot.com",
  messagingSenderId: "292130692921",
  appId: "1:292130692921:web:29ab9b610e1c220d5652e8",
  measurementId: "G-FLC6D2WGBC"
};

const firebase = initializeApp(firebaseConfig);
const db = getDatabase();