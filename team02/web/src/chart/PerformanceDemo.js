import React, { Component } from 'react';
import CanvasJSReact from '../assets/canvasjs.react';
var CanvasJSChart = CanvasJSReact.CanvasJSChart;

var data = [];
var dataPoints = [];
var dataSeries = { type: "line" };
var startTime = 0, endTime = 0;
class PerformanceDemo extends Component {

   constructor() {
     super()
     this.drawChart = this.drawChart.bind(this);
   }


  	componentDidMount() {
		endTime = new Date();

    console.log(this)
    this.drawChart(1)



	}

  drawChart(id){
    data = []
    dataPoints = [];

    fetch("/wave?id="+id)
     .then(res => res.json())
     .then(
       (result) => {

         console.log(this.chart)
         console.log(result)
         var limit = result[0].length;
         var y = 100;
         let xx = result[0]
         let yy = result[1]


         for (var i = 0; i < limit; i += 1) {
           dataPoints.push({
             x: xx[i],
             y: yy[i]
           });
         }
         dataSeries.dataPoints = dataPoints;
         data.push(dataSeries);



         this.chart.data = data;
         this.chart.render();
    	//document.getElementById("timeToRender").innerHTML = "Time to Render: " + (endTime - startTime) + "ms";
         console.log("refresh done")


       },
       // Note: it's important to handle errors here
       // instead of a catch() block so that we don't swallow
       // exceptions from actual bugs in components.
       (error) => {
          console.log("get one error", error)
       }
     )

  }




  updateWords(words){



    var stripLines2 = [];
     words.forEach(function(word){
       let data2 = {}
       data2.value = word[1]/16000;
       data2.label =  word[2];
       data2.labelFontColor = "#808080"
       data2.labelAlign = "near";
       stripLines2.push(data2);

     })

    this.chart.options.axisX = {
   title: "",
   stripLines: stripLines2
    }

    console.log(stripLines2)
    console.log(this.chart.options.axisX)

    this.chart.render();

  }


  AddPhonemes(words, phonemes){



    var stripLines2 = [];
     words.forEach(function(word){
       let data2 = {}
       data2.value = word[1]/16000;
       data2.label =  "___" + word[2];
       data2.labelFontColor = "#808080"
       data2.labelAlign = "near";
       stripLines2.push(data2);

     })


     phonemes.forEach(function(word){
       let data2 = {}
       data2.value = word[1]/16000;
       data2.label =  word[2];
       data2.labelFontColor = "#ff0000"
       data2.labelAlign = "near";
       stripLines2.push(data2);

     })


    this.chart.options.axisX = {
   title: "",
   stripLines: stripLines2
    }

    console.log(stripLines2)
    console.log(this.chart.options.axisX)

    this.chart.render();

  }

	render() {
		var limit = 50000;
		var y = 100;



		// for (var i = 0; i < limit; i += 1) {
		// 	y += Math.round(Math.random() * 10 - 5);
		// 	dataPoints.push({
		// 		x: i,
		// 		y: y
		// 	});
		// }
		 dataSeries.dataPoints = dataPoints;
		 data.push(dataSeries);

		const spanStyle = {
			fontSize: '20px',
			fontWeight: 'bold',
			backgroundColor: '#d85757',
			padding: '2px 4px',
			color: '#ffffff'
		}

    const chartStyle = {
      width : '1000px'
    }

		const options = {
			zoomEnabled: true,
			animationEnabled: true,
			title: {
				text: "Sound Wave"
			},

			axisY: {
				includeZero: false
			},
			data: data  // random data
		}

		startTime = new Date();
//		<span id="timeToRender" style={spanStyle}></span>
		return (
		<div style={chartStyle} >
			<CanvasJSChart options = {options}
				 onRef={ref => this.chart = ref}
			/>
			{/*You can get reference to the chart instance as shown above using onRef. This allows you to access all chart properties and methods*/}

		</div>
		);
	}
}

export default PerformanceDemo;
