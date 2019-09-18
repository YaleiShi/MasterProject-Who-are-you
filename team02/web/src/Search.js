import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';


class Search extends React.Component {
  constructor() {
    super();
    this.state = {
      todos: ['a','b','c','d','e','f','g','h','i','j','k'],
      currentPage: 1,
      todosPerPage: 50,
      value :1
    };
    this.handleClick = this.handleClick.bind(this);
    this.selectChange = this.selectChange.bind(this)
    this.updateRegion = this.updateRegion.bind(this)
    this.handleRecordClick = this.handleRecordClick.bind(this)
    this.updateRegion(1)
  }

  handleClick(event) {
    this.setState({
      currentPage: Number(event.target.id)
    });
  }

  handleRecordClick(e) {
    fetch("/recordInfo?id="+e.target.value)
      .then(res => res.json())
      .then(
        (result) => {
           this.setState({ record : result});
          //   this.chart.current.updateWords(result);
            if(typeof this.props.onRecordClick === 'function'){
              this.props.onRecordClick(result)
            }

        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
           console.log("get one error", error)
        }
      )




  };


  updateRegion(region){
    this.setState({value: region});

    fetch("/record?region=" + region)
      .then(res => res.json())
      .then(
        (result) => {
        //  this.setState({ words : result});
          //  this.chart.current.updateWords(result);
            this.setState({todos: result});
            this.setState({currentPage: 1});
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

  selectChange(e){
    this.updateRegion(e.target.value)

  }



  render() {
    const { todos, currentPage, todosPerPage } = this.state;

    // Logic for displaying current todos
    const indexOfLastTodo = currentPage * todosPerPage;
    const indexOfFirstTodo = indexOfLastTodo - todosPerPage;
    const currentTodos = todos.slice(indexOfFirstTodo, indexOfLastTodo);

    const renderTodos = currentTodos.map((todo, index) => {
      return  <tr><td><button  value={todo[0]} onClick={this.handleRecordClick}>{todo[0]}</button></td>
      <td align="left">{todo[1]}</td>
              </tr>;
    });

    // Logic for displaying page numbers
    const pageNumbers = [];
    for (let i = 1; i <= Math.ceil(todos.length / todosPerPage); i++) {
      pageNumbers.push(i);
    }

    const renderPageNumbers = pageNumbers.map(number => {
      return (
        <li
          key={number}
          id={number}
          onClick={this.handleClick}
        >
          {number}
        </li>
      );
    });

    return (

      <div className="search">
  <label>region</label> &nbsp; &nbsp;
  <select value={this.state.value} onChange={this.selectChange}>
  <option value="1">New England</option>
  <option value="2">Northern</option>
  <option value="3">North Midland</option>
  <option value="4">South Midland</option>
  <option value="5">Southern</option>
  <option value="6">New York City</option>
  <option value="7">Western</option>
  <option value="8">Army Brat</option>

</select>
        <table className="table">
        <thead>
          <tr>

            <th scope="col"  width="10%" className="text-center" >ID</th>
            <th scope="col" width="90%" className="text-center" >Content</th>

          </tr>
        </thead>
         <tbody>
          {renderTodos}
           </tbody>
        </table>
        <ul id="page-numbers">
          {renderPageNumbers}
        </ul>
      </div>
    );
  }
}


export default Search;
