'use strcit';

import JWT from './jwt'
import Axios from "axios";

class Auth {

    static checkAuth(instance) {
        Axios.post('/api/check-token', {
            token: JWT.getToken()
        }).then((response) => {
            if (response.status === 200) {
                console.log('status', 200)
                instance.authorized = true;
            }
        }).catch((error) => {
            console.log('errorerror', error)
        });

    }

    static checkToken(router) {
        Axios.post('/api/check-token', {

            token: JWT.getToken()
        }).catch((error) => {
            if (error.response.status === 400) {
                router.push({ name: 'login', })
            }
        });
    }

    static getAuthorizationHeader() {
        return {'Authorization': `JWT ${JWT.getToken()}`};
    }
}

export default Auth;