import React from 'react';
// import logo from './logo.svg';
import './App.css';
import VolunteerForm from './VolunteerForm'

function App() {
  function alertFunction(name) {

    console.log(name)

  }
  return (
    <div className="App">
      <header className="App-header">
        <VolunteerForm alert={(name) => alertFunction(name)} />
      </header>
    </div>
  );
}

export default App;
