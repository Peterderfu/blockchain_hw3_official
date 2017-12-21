//Flot Moving Line Chart

$(function() {

  var container = $("#kapelx-background-overlay");

  // Determine how many data points to keep based on the placeholder's initial size;
  // this gives us a nice high-res plot while avoiding more than one point per pixel.

  var maximum = container.outerWidth() / 2 || 300;

  //

  var data = [];

  function getRandomData() {

      if (data.length) {
          data = data.slice(1);
      }

      while (data.length < maximum) {
          var previous = data.length ? data[data.length - 1] : 50;
          var y = previous + Math.random() * 10 - 5;
          data.push(y < 0 ? 0 : y > 100 ? 100 : y);
      }

      // zip the generated y values with the x values

      var res = [];
      for (var i = 0; i < data.length; ++i) {
          res.push([i, data[i]])
      }

      return res;
  }

  //

  series = [{
      data: getRandomData(),
      lines: {
          fill: true
      }
  }];

  //

  var plot = $.plot(container, series, {
      grid: {
          borderWidth: 0,
          orderMargin: 0,
          labelMargin: 0,
          margin: {
              top: 0,
              bottom: 0,
              left: 0
          },
          markings: function(axes) {
              var markings = [];
              var xaxis = axes.xaxis;
              for (var x = Math.floor(xaxis.min); x < xaxis.max; x += xaxis.tickSize * 2) {
                  markings.push({
                      xaxis: {
                          from: x,
                          to: x + xaxis.tickSize
                      },
                      color: "rgba(232, 232, 255, 0.2)"
                  });
              }
              return markings;
          }
      },
      xaxis: {
          show: false,
          tickFormatter: function() {
              return "";
          }
      },
      yaxis: {
          show: false,
          min: 0,
          max: 110
      },
      legend: {
          show: false
      }
  });

  // Update the random dataset at 25FPS for a smoothly-animating chart

  setInterval(function updateRandom() {
      series[0].data = getRandomData();
      plot.setData(series);
      plot.draw();
  }, 40);

});