import React, { Component } from 'react';
import logo from './img/wave.png';
import spectrogram from './img/spectrogram.png';
import './App.css';
import soundfile from './sound/SI1027.mp3'

import Players from './Players'
import WordsBar from './WordsBar'
import Wave from './Wave'
import PerformanceDemo from "./chart/PerformanceDemo";
import Search from './Search'


class App extends Component {
  constructor() {
    super();
    this.state = {
      name: '',
      id:1,           // audio record id
      record:[],      // audo record info
      words:[]
    }
    this.handleClick = this.handleClick.bind(this);
    this.LoadWord = this.LoadWord.bind(this);
    this.LoadPhn = this.LoadPhn.bind(this);
    this.chart = React.createRef();
    this.handleWordClick = this.handleWordClick.bind(this);
    this.handleRecordClick = this.handleRecordClick.bind(this);

}

LoadWord() {

    fetch("/word?id="+this.state.id)
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({ words : result});
            this.chart.current.updateWords(result);
          console.log(result.length)
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
           console.log("get one error", error)
        }
      )
  }


  LoadPhn() {

      fetch("/phn?id="+this.state.id)
        .then(res => res.json())
        .then(
          (result) => {
              this.chart.current.AddPhonemes(this.state.words, result);

          },
          // Note: it's important to handle errors here
          // instead of a catch() block so that we don't swallow
          // exceptions from actual bugs in components.
          (error) => {
             console.log("get one error", error)
          }
        )
    }


 handleClick(e) {
    let audio = new Audio();
    let url = "https://audio2timit.s3-us-west-1.amazonaws.com" + this.state.record[3] + ".mp3"
    console.log(url)
    audio.src = url

    audio.currentTime = 0.1
    audio.play()
    setTimeout(function(){
    audio.pause();
    console.log("Audio Stop Successfully");
    },
    10000);
  }

  word3dSpectrogram(index) {

          let word = this.state.words[index]

          let url = "test2.html?path=xxx&start="+parseInt(word[0]/160)+"&end="+parseInt(word[1]/160)
          window.open(url)
  }


   handleWordClick(index) {
     let word = this.state.words[index]
      console.log(index, word);

      let audio = new Audio(soundfile);
      audio.currentTime = word[0]/16000
      audio.play()
      setTimeout(function(){
      audio.pause();

      },
      (word[1] - word[0])/16);  // millsecond
    }


    handleRecordClick(record) {
      this.setState({ id : record[0], record: record});
      this.chart.current.drawChart(record[0])
      this.LoadWord()

     }


    render() {

         return (
      <div className="App">
        <header className="App-header">
           <Search  onRecordClick={this.handleRecordClick}  ></Search>
          <PerformanceDemo ref = {this.chart}></PerformanceDemo>

         <WordsBar words = {this.state.words} onWordClick={this.handleWordClick}  ></WordsBar>
         <button  className="App-button" onClick={this.handleClick}>
           player
         </button>
         <button  className="App-button" onClick={this.LoadWord}>
           LoadWord
         </button>

         <button  className="App-button" onClick={this.LoadPhn}>
           LoadPhoneme
         </button>


        </header>
      </div>
    );

    }

}

export default App;
