let xValues = ["Openness", "Conscientiousness", "Extroversion", "Agreeableness", "Neuroticism"];
const barColors = ["red", "green","blue","orange","brown"];

new Chart("myChart", {
  type: "bar",
  data: {
    labels: xValues,
    datasets: [{
      backgroundColor: barColors,
      data: oceanvalue
    }]
  },
  options: {
    legend: {display: false},
    title: {
      display: true,
      text: "OCEAN Personality Result"
    }
  }
});

let oxValues = ["Imagination", "Artistic Interest", "Emotionality", "Adventurousness", "Intellect", "Liberalism"];
new Chart("oChart", {
    type: "bar",
    data: {
      labels: oxValues,
      datasets: [{
        backgroundColor: barColors,
        data: o
      }]
    },
    options: {
      legend: {display: false},
      title: {
        display: true,
        text: "OCEAN Personality Result"
      }
    }
  });