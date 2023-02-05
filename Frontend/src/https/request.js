import axios from 'axios';

const api = axios.create({
    baseURL: "http://localhost:5000/",
    withCredentials: true,
    headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json',
    }
});

export const search = (data) => api.post('/apilink', data);
export const store = (data) => api.post('/apilink/store', data);
export const que = (data) => api.post('/apilink/que', data);