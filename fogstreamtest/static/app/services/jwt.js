'use strict';

import Axios from 'axios';

class JWT {

    static isToken() {
        return localStorage.getItem("username") !== null;
    }

    static storeToken(token) {

        window.localStorage.setItem('jwt', token);
    }

    static getToken() {
        return window.localStorage.getItem('jwt');
    }
}

export default JWT;