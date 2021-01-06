<template>
  <div class="hello">
    <canvas id="myChart1"></canvas>
  </div>
</template>

<script>
import Chart from "chart.js";
import requests from "axios";

function getRandomColor() {
  var letters = "0123456789ABCDEF".split("");
  var color = "#";
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

export default {
  chart: null,
  mounted() {
    chart = new Chart(document.getElementById("myChart1"), {
      type: "line",
      data: {
        datasets: [
          {
            label: "1",
            data: [0, 20, 40, 50],
            borderColor: getRandomColor(),
          },
          {
            label: "2",
            data: [50, 40, 20, 0],
            borderColor: getRandomColor(),
          },
        ],
        labels: ["January", "February", "March", "April"],
      },
      options: {
        tooltips: {
          mode: "index",
          intersect: false,
        },
        events: ["touchstart", "touchmove", "touchend"],
        onHover: (event) => {},
      },
    });
  },

  name: "HelloWorld",
  props: [],
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
