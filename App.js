import React from 'react';
import axios from 'axios';
//const {Axios} = pkg;


class Display extends React.Component{
  constructor(props){
    super(props)
    this.state = {
      questions: [],
      dataLoaded: false
    }
  }
  


  
  componentDidMount(){
    // todo: figure out how to get a specific amount of elements to display
    var numberOfElements = '3';

    axios.get('/Questions/' + (numberOfElements))
    .then(res => {
      this.setState(
        {
          questions: res,
          dataLoaded: true
        }
      );
      console.log(res.data[0].postId);
    })
    .catch(err =>{
      console.log(err);
    })
  }
  getCardArray = () =>{
    const array = [];

    for (var i = 0; i< (this.state.questions.data.length); i++){
      var postTitle = (this.state.questions.data[i].postTitle);
      var postBody = (this.state.questions.data[i].postBody);
      var userName = (this.state.questions.data[i].userName);
      
      array.push( <Card postTitle = {postTitle} postBody = {postBody} userName= {userName}></Card>);
    }

    return array
  }
  
  
  
  render(){
    // this.requestData();
    
    if (!this.state.dataLoaded) return (<div>
    <h1> Pleses wait some time.... </h1> </div>) ;

    
    return(
      <div>
        <h1>hello world</h1>


        {this.getCardArray()}

        

      </div>
      
    )
  }

}

class Card extends React.Component{
  constructor(props){
    super(props)
  }
  
  render(){
    var textTitle = this.props.postTitle;
    var textBody = this.props.postBody;
    var userName = this.props.userName;
    return(
      <div>
      <h1>{textTitle}</h1>
      <h2>{textBody}</h2>
      <h2>user name: {userName}</h2>
      </div>
      
    );
  }
    
    
}

class CreateQuestion extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      postTitleValue: '',
      postBodyValue: '',
      userNameValue: '',
      classValue: ''
    };
    this.handleTitleChange = this.handleTitleChange.bind(this);
    this.handleBodyChange = this.handleBodyChange.bind(this);
    this.handleNameChange = this.handleNameChange.bind(this);
    this.handleClassChange = this.handleClassChange.bind(this);
    
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleTitleChange(event) {
    this.setState({postTitleValue: event.target.value});
  }

  handleBodyChange(event) {
    this.setState({postBodyValue: event.target.value});
  }

  handleNameChange(event) {
    this.setState({userNameValue: event.target.value});
  }

  handleClassChange(event) {
    this.setState({classValue: event.target.value});
  }



  handleSubmit(event) {
    console.log(this.state.postTitleValue);

    axios.put('Questions/0',  {
      'postTitle': this.state.postTitleValue,
      'postBody' : this.state.postBodyValue,
      'userName' : this.state.userNameValue,
      'className' : this.state.classValue,

    })
    .then(res => {
      console.log(res);
    })
    .catch(err =>{
      console.log(err);
    })


    alert('A name was submitted: ' + this.state.postTitleValue);
    //event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Post Title:
          <input type="text" value={this.state.postTitleValue} onChange={this.handleTitleChange} />
        </label>

        <label>
          Post Body:
          <input type="text" value={this.state.postBodyValue} onChange={this.handleBodyChange} />
        </label>


        <label>
          User Name:
          <input type="text" value={this.state.userNameValue} onChange={this.handleNameChange} />
        </label>


        <label>
          Class:
          <input type="text" value={this.state.classValue} onChange={this.handleClassChange} />
        </label>


        <input type="submit" value="Submit" />
      </form>
    );
  }
}


function App() {
  return (
    <div className="App">
      <Display />
      <CreateQuestion />
    </div>
  );
}

export default App;
