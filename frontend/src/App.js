import React from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';

var test = () => {
  axios.get("http://127.0.0.1:8000/libraries/")
    .then(res => alert(res.data))
    .catch(err => console.log(err));
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <button id="test-btn" onClick={() => test()}>Test</button>
      </header>
    </div>
  );
}

export default App;
