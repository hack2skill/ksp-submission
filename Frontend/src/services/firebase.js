import firebase from 'firebase'
import 'firebase/auth'
import 'firebase/firestore'
import 'firebase/storage'

const firebaseConfig = {
    apiKey: "AIzaSyDIoKgcwLrRPh9Z0_SPKLWjTBhr9X_mh0M",
    authDomain: "licious-waffle.firebaseapp.com",
    databaseURL: "https://licious-waffle-default-rtdb.firebaseio.com",
    projectId: "licious-waffle",
    storageBucket: "licious-waffle.appspot.com",
    messagingSenderId: "160200066583",
    appId: "1:160200066583:web:4f8b7b72ec7e41cb69fe52",
    measurementId: "G-880BV9HWD3"
};

firebase.initializeApp(firebaseConfig);


export const auth = firebase.auth;

export const firestore = firebase.firestore();

export const storage = firebase.storage();
