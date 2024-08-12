import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000/api/auth/';

const login = (username, password) => {
  return axios.post(API_URL + 'login', {
    username,
    password,
  });
};

const getCurrentUser = () => {
  return JSON.parse(localStorage.getItem('user'));
};

export default {
  login,
  getCurrentUser,
};
