import React, { Component } from 'react'
import axios from 'axios'
import { connect } from 'react-redux'

class LibraryTable extends Component {
    state = {
        libraries: []
    };

    loadItem = () => {
        axios.get("/libraries/")
            .then(({ data }) => {
                this.setState({
                    libraries: data
                })
            })
            .catch(err => console.log(err));
    }

    componentDidMount() {
        this.loadItem()
    }

    render() {
        return (
            <div className="LibraryTable">
                {this.state.libraries.map(item => (
                    <div key={item.id}>
                        <div key={item.id}>
                            <h1>{item.name}</h1>
                            <span>{item.version}</span>
                        </div>
                    </div>
                ))}
            </div>
        )
    }
}

export default connect()(LibraryTable)