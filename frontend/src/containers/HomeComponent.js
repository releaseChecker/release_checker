import React from 'react'
import { connect } from 'react-redux'
class Home extends React.Component {
    render() {
        return (
            <div>
                Home. created by {this.props.author}
            </div>
        );
    }
}

export default connect(
    state => ({ author: state.author })
)(Home)