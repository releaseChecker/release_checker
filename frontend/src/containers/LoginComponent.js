import React, { Component } from 'react'
import { connect } from 'react-redux'
import { userActions } from '../actions/userActions'
class Login extends Component {

    constructor(props) {
        super(props)

        console.log("Login");
        this.props.logout();

        this.state = {
            username: '',
            password: ''
        };
    }

    handleChange = e => {
        const { name, value } = e.target;
        this.setState({ [name]: value });
    }

    handleSubmit = e => {
        e.preventDefault();
        const { username, password } = this.state;
        if (username && password) {
            this.props.login(username, password)
        }

        console.log("username, password", username, password);
    };

    render() {
        console.log("Login");
        return (
            <div>
                <h2>Login</h2>
                <form name="form" onSubmit={this.handleSubmit}>
                    <div>
                        <input type="text" placeholder="username" name="username" onChange={this.handleChange} />
                    </div>
                    <div>
                        <input type="password" placeholder="password" name="password" onChange={this.handleChange} />
                    </div>
                    <div>
                        <button type="submit">Login</button>
                    </div>
                </form>
            </div>
        );
    }
}

function mapState(state) {
    const { loggingIn } = state.authentication;
    return { loggingIn };
}

const actionCreators = dispatch => ({
    login: userActions.login(dispatch),
    logout: userActions.logout(dispatch)
})

export default connect(mapState, actionCreators)(Login)