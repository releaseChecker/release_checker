import React from 'react';
import './App.css';
import axios from 'axios';

class App extends React.Component {
  state = {
    libraries: []
  };

  loadItem = () => {
    axios.get("http://127.0.0.1:8000/libraries/")
    .then(({data}) => {
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

export default App;
