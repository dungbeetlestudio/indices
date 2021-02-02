<template>
  <div class="home">
    <div>
      <canvas id="上证指数"></canvas>
    </div>
    <div>
      <canvas id="深证成份指数"></canvas>
    </div>
    <div>
      <canvas id="香港恒生指数"></canvas>
    </div>
    <div>
      <canvas id="日经225指数"></canvas>
    </div>
    <div>
      <canvas id="道琼斯工业平均指数"></canvas>
    </div>
    <div>
      <canvas id="纳斯达克综合指数"></canvas>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Chart from "chart.js";
import requests from "axios";

export default {
  name: "Home",
  components: {},
  timer: null,
  charts: null,
  async updated() {},
  async mounted() {
    this.charts = [
      {
        name: "上证指数",
        color: "Red",
        chart: null
      },
      {
        name: "深证成份指数",
        color: "Blue",
        chart: null
      },
      {
        name: "香港恒生指数",
        color: "Yellow",
        chart: null
      },
      {
        name: "日经225指数",
        color: "Green",
        chart: null
      },
      {
        name: "道琼斯工业平均指数",
        color: "Purple",
        chart: null
      },
      {
        name: "纳斯达克综合指数",
        color: "Orange",
        chart: null
      }
    ];

    for (let obj of this.charts) {
      obj.chart = new Chart(document.querySelector(`#${obj.name}`), {
        type: "line",
        data: {
          labels: [],
          datasets: [
            {
              label: obj.name,
              data: [],
              borderColor: obj.color,
              pointRadius: 0,
              borderWidth: 1
            }
          ]
        },
        options: {
          maintainAspectRatio: true,
          tooltips: {
            mode: "index",
            intersect: false
          },
          events: [
            "touchstart",
            "touchmove",
            "touchend",
            "mousemove",
            "mouseout",
            "click"
          ],
          onHover: event => {}
        }
      });

      // document.querySelector('#indices').style.height = '300px'
    }

    let syncData = async () => {
      console.log("1");
      for (let obj of this.charts) {
        try {
          let r = await requests.get(
            `http://dungbeetles.xyz:8888/indices-realtime?name=${obj.name}`
          );
          if (r.data.err) throw r.data.err;

          obj.chart.data.labels.length = 0;
          obj.chart.data.datasets[0].data.length = 0;

          for (let data of r.data.val) {
            obj.chart.data.labels.push(data[0].substring(5));
            obj.chart.data.datasets[0].data.push(data[1]);
          }

          obj.chart.update();
        } catch (e) {
          return;
        }
      }
    };

    await syncData();
    this.timer = setInterval(syncData, 1 * 60 * 1000);
  },
  async destory() {
    console.log('destory')
    clearInterval(this.timer);
  }
};
</script>
