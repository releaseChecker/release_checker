import React, { Component } from 'react';
import './App.css';
import { Route, BrowserRouter as Router, Switch, Redirect } from "react-router-dom"
import Home from './containers/HomeComponent';
import Login from './containers/LoginComponent';
import { connect } from 'react-redux';
import PrivateRoute from './components/PrivateRoute'
import LibraryTable from './containers/LibraryTable'

class App extends Component {
  render() {
    return (
      <div className="App">
        <Router>
          <Switch>
            <PrivateRoute exact path="/" component={Home} />
            <PrivateRoute path="/libraries" component={LibraryTable} />
            <Route path="/login" component={Login} />
            <Redirect from="*" to="/" />
          </Switch>
        </Router>
      </div>
    )
  }
}

export default connect()(App);
