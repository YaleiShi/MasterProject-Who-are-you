import React, { Component } from 'react';
import logo from './logo.svg';
import './WordsBar.css';
import Word from './Word'



class WordsBar extends Component {

  constructor() {
    super()
    this.state = {
      word: ['then', 0],
    }

    this.handleClick = this.handleClick.bind(this)
}

 handleClick(value) {

     console.log('this is:',value);
     console.log(this)
     if(typeof this.props.onWordClick === 'function'){
       this.props.onWordClick(value)
     }
  }


  render() {

       return (<div className="wordsbar" >
      {this.props.words.map((key, index) => <Word  word={key} index={index} key={index} click={this.handleClick} >{key[2]}</Word>)}


      </div>);
     }



  }


export default WordsBar;
