import React, { Component } from 'react';
import logo from './logo.svg';




class Word extends Component {

  constructor() {
    super()
}

handleClick(value) {

    console.log('this is:',value);
    this.props.click(value)
 }


  render() {
      let offset = this.props.index%3;
      if(offset == 0){
         return (<span className="word1"  value="even" onClick={this.handleClick.bind(this, this.props.index)}>{this.props.word[2]}</span>);
      }else if (offset ==1 ){
         return (<span className="word2"  value="even" onClick={this.handleClick.bind(this, this.props.index)}>{this.props.word[2]}</span>);
      }else{
         return (<span className="word3"  value="even" onClick={this.handleClick.bind(this, this.props.index)}>{this.props.word[2]}</span>);
      }


     }




}


export default Word;
