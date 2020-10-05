import React, { Component } from "react";
import { NavLink, Route, Switch } from 'react-router-dom'
import Home from './Home'
import LibraryList from '../containers/LibraryList'

class App extends Component {
    render() {
        return (
            <div className="App">
                <div className="App-header">
                    <h1>Library Release Checker</h1>
                </div>
                <div className="content-wrapper">
                    <ul>
                        <li><NavLink exact to="/">Home</NavLink></li>
                        <li><NavLink to="/libraries/">Libraries</NavLink></li>
                    </ul>
                    <Switch>
                        <Route exact path="/libraries/" component={LibraryList}/>
                        <Route exact path="/" component={Home}/>
                    </Switch>
                </div>
            </div>
        )
    }
}

export default App;