import React, { Component } from 'react';
import { connect } from 'react-redux';
import Library from '../components/Library';
import { fetchLibrary } from '../actions/index';

class LibraryList extends Component {
    componentDidMount() {
        this.props.fetchLibrary();
    }

    renderLibrary() {
        return this.props.libraryList.map((library) => {
            return <li key={library.id}><Library libraryData={library}/></li>
        })
    }

    render () {
        return (
            <div>
                <h2>Library List</h2>
                <ul>
                    {this.renderLibrary()}
                </ul>
            </div>
        )
    }
}

export default connect((state) => {
    return {
        libraryList: state.lists.libraryList
    };
}, { fetchLibrary })(LibraryList);