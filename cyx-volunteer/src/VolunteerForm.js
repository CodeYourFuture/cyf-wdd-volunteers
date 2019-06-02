import React from 'react';
// import logo from './logo.svg';
import './App.css';

class VolunteerForm extends React.Component {
  constructor(props) {
    super(props);

    this.alertFunction = this.alertFunction.bind(this);
  }

  alertFunction(event) {
    event.preventDefault()
    console.log(event)
  }
  render() {
    return (
      <form onSubmit={this.alertFunction}>
        <label for="name">Name</label>
        <input type="text" id="name"/>
        <label for="surname">Surname</label>
        <input type="text" id="surname"/>
        <label for="cyf-city">City</label>
        <input type="text" id="cyf-city"/>
        <label for="email">Email</label>
        <input type="text" id="email"/>
        <input type="submit" value="Submit"/>
      </form>
    );
  }
}

export default VolunteerForm;
