import * as types from '../constants/auth';
import callApi from '../utils/call-api';

export function signup(username, email, password, repeatPassword){
    return (dispatch) => {
        dispatch({
            type: types.SIGNUP_REQUEST
        })
        return callApi('/api/users/', undefined, {method: "POST"},{
            username,
            password,
            email,
        })
        .then(json => {
            if (!json.token) {
                throw new Error('Джок токен!');
            }
            localStorage.setItem('token', json.token);
            dispatch({
                type: types.SIGNUP_SUCCESS,
                payload: json
            })
        })
        .catch(reason => dispatch({
            type: types.SIGNUP_FAILURE,
            payload: reason
        }));
    };
}

export function login(username, password){
    return (dispatch) => {
        dispatch({
            type: types.LOGIN_REQUEST
        })
        return callApi('/accounts/login/', undefined, {method: "POST"}, {
            username,
            password,
        })
        .then(json => {
            if (!json.token) {
                throw new Error('Джок токен!');
            }
            console.log(json);
            localStorage.setItem('token', json.token);

            dispatch({
                type: types.LOGIN_SUCCESS,
                payload: json
            })
        })
        .catch(reason => dispatch({
            type: types.LOGIN_FAILURE,
            payload: reason
        }));
    };
}

export function logout(){
    return (dispatch) => {
        dispatch({
        type: types.LOGOUT_REQUEST
        })
    };
}

export function recieveAuth() {
    return(dispatch, getState) => {
        const {token} = getState().auth;
        if (!token) {
            dispatch({
                type: types.RECIEVE_AUTH_FAILURE
            })
        }
        return callApi('/userauth', token)
            .then(json => {
                dispatch({
                    type: types.RECIEVE_AUTH_SUCCESS,
                    payload: json
                })
            })
        .catch(reason => dispatch({
            type: types.RECIEVE_AUTH_FAILURE,
            payload: reason
        }));
    }
}
