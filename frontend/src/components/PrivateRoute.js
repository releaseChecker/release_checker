import React, {Component} from 'react'
import { Route, Redirect } from 'react-router-dom'

class PrivateRoute extends Component {
    render() {
        const { component: PrivateComponent, ...rest } = this.props;
        const isAuthenticated = true // TODO integrate with login

        return (
            <Route {...rest} render={props => (
                isAuthenticated ? <PrivateComponent {...props} />
                    : <Redirect to={{ pathname: '/login', state: { from: props.location } }} />
            )} />
        )
    }
}

export default PrivateRoute