import React from 'react';
//import ReactDOM from 'react-dom';
//import logo from './logo.svg';
import './Home.css';

//Form component
class NewProjectForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: ''
    };

    this.handleChange = this.handleInputChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }
  
  handleInputChange(event) {
    //const target = event.target;
    //const value = target.type === 'checkbox' ? target.checked : target.value;
    //const name = target.name;
    
    this.setState({name:event.target.value});
  }

  handleSubmit(event) {
	console.log('Saving Project '+ this.state.name);
	fetch("/api/home/project", {
        method:"POST",
        cache: "no-cache",
        headers:{
            "content_type":"application/json",
        },
        body:JSON.stringify(this.state.name)
        }
    ).then(response => {
    if(response.ok){
    console.log(response.json())
    return response.json();}
  }).then(json => {
  console.log(json)
  this.setState({name:json})})
    alert('A form was submitted: ' + this.state.name);
    event.preventDefault();
  }

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit} action="http://localhost:5000/api/home/project/" method="POST">
          <div className="Home-Grp">
            <label htmlFor="nameImput">Project Name</label>
            <input type="text" name="name" value={this.state.name} onChange={this.handleChange} className="Home-control" id="nameImput" placeholder="Project Name" />
          </div>
          <input type="submit" value="+CreateNewProject" className="btn btn-primary" />
        </form>
      </div>
    )
  }
}

class MainTitle extends React.Component {
  render(){
    return(
      <h1>Integra Code Test</h1>
    )
  }
}

class Home extends React.Component {
  render(){
    return(
      <div>
        <MainTitle/>
        <NewProjectForm/>
      </div>
    )
  }
}

export default Home;