import React, { Component } from 'react';
import logo from './logo.svg';

import './App.css';
import PerformanceDemo from "./chart/PerformanceDemo";

class Wave extends Component {
  render() {
     return (<PerformanceDemo  words = {this.props.words} ></PerformanceDemo>);
   }




}


export default Wave;
