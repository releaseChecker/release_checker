import { userConstants } from '../constants/user.constants'
import { userService } from '../services/userService'
import { history } from '../helpers/history'

const login = dispatch => (username, password) => {
    console.log("userAction.login", username, password);

    dispatch({ type: userConstants.LOGIN_REQUEST })
    userService.login(username, password)
        .then(user => {
            console.log("userAction.login.then", username, password, user)
            dispatch({ type: userConstants.LOGIN_SUCCESS, user: user })
            history.push("/")
        }).catch(error => {
            console.log("userAction.login.catch", username, password, error)
            dispatch({ type: userConstants.LOGIN_FAILURE, error: error.toString() })
        });
}

const logout = dispatch => () => {
    console.log("userAction.logout")
    userService.logout();
    dispatch({ type: userConstants.LOGOUT })
}

export const userActions = {
    login,
    logout
}