import React from 'react'
import { connect } from 'react-redux'
class Home extends React.Component {

    render() {
        return (
            <div>
                Home. created by {this.props.user}
            </div>
        );
    }
}

function mapState(state) {
    const { authentication } = state;
    const { user } = authentication;
    return { user };
}

export default connect(
    mapState
)(Home)