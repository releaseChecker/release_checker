export const userService = {
    login,
    logout
};

function login(username, password) {
    // TODO Integrate with login api
    console.log("userService.login", username, password)
    return new Promise((resolve, reject) => {
        console.log("userService.login.promise", username, password)
        localStorage.setItem("user", "usertoken");
        resolve("usertoken");

        const flag = false;
        if (flag) {
            reject(new Error("Error"))
        }
    })    
}

function logout() {
    localStorage.removeItem("user");
}