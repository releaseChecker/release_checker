import React from 'react';
import './App.css';
import axios from 'axios';
import { Link, Route, BrowserRouter as Router } from "react-router-dom"
import Home from './containers/home/HomeComponent';
import Login from './containers/login/LoginComponent';

class App extends React.Component {
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
      <div className="App">
        <Router>
          <header>
            <Link to="/">
              <button>Home</button>
            </Link>
            <Link to="/libraries">
              <button>Libraries</button>
            </Link>
          </header>
          <main>
            <Route exact path="/" component={Home} />
            <Route path="/libraries" component={Login} />
          </main>
        </Router>
      </div>
    )
  }
}

class LibraryTable extends React.Component {
  render() {
    return (
      <div className="LibraryTable">
        {this.props.libraries.map(item => (
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

export default App;
