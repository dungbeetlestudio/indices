<template>
  <div class="home">
    <canvas id="indices" ></canvas>
  </div>
</template>

<script>
// @ is an alias to /src
import Chart from "chart.js";
import requests from "axios";

function getRandomColor() {
  var letters = "0123456789ABCDEF".split("");
  var color = "#";
  for (var i = 0; i < 6; i++)  {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

export default {
  name: "Home",
  components: {},
  chart: null,
  mounted() {
    this.chart = new Chart(document.querySelector("#indices"), {
      type: "line",
      data: {
        datasets: [          {
            label: "上证",
            data: [0, 20, 40, 50],
            borderColor: getRandomColor(),
          },          {
            label: "上证",
            data: [0, 20, 40, 50],
            borderColor: getRandomColor(),
          },          {
            label: "上证",
            data: [0, 20, 40, 50],
            borderColor: getRandomColor(),
          }
        ],
        labels: ["1", "2", "3", "4"],
      },
      options: {
        maintainAspectRatio:false,
        tooltips: {
          mode: "index",
          intersect: false,
        },
        events: ["touchstart", "touchmove", "touchend"],
        onHover: (event) => {},
      },
    });

    document.querySelector('#indices').style.height = '300px'
  },
};
</script>
