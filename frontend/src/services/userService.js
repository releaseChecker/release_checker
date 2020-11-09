import axios from 'axios';

export const userService = {
    login,
    logout
};

function login(username, password) {
    console.log("userService.login", username, password)
    return axios.post("/token/", {
        username: username,
        password: password
    }).then(({ data }) => {
        console.log("userService.login, success", username, password)
        localStorage.setItem("user", data["access"]);
    })
}

function logout() {
    localStorage.removeItem("user");
}