let xValues = ["Openness", "Conscientiousness", "Extroversion", "Agreeableness", "Neuroticism"];
const barColors = ["red", "green", "blue", "orange", "brown"];

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
    legend: { display: false },
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
    legend: { display: false },
    title: {
      display: true,
      text: "OCEAN Personality Result"
    }
  }
});

let cxValues = ["Self-Efficacy", "Orderliness", "Dutifulness", "Achievement-Striving", "Self-Discipline", "Cautiousness"];
new Chart("cChart", {
  type: "bar",
  data: {
    labels: cxValues,
    datasets: [{
      backgroundColor: barColors,
      data: c
    }]
  },
  options: {
    legend: { display: false },
    title: {
      display: true,
      text: "OCEAN Personality Result"
    }
  }
});
let exValues = ["Friendliness", "Gregariousness", "Assertiveness", "Activity-Level", "Excitement-Seeking", "Cheerfulness"];
new Chart("eChart", {
  type: "bar",
  data: {
    labels: exValues,
    datasets: [{
      backgroundColor: barColors,
      data: e
    }]
  },
  options: {
    legend: { display: false },
    title: {
      display: true,
      text: "OCEAN Personality Result"
    }
  }
});

let axValues = ["Trust", "Morality", "Altruism", "Cooperation", "Modesty", "Sympathy"];
new Chart("aChart", {
  type: "bar",
  data: {
    labels: axValues,
    datasets: [{
      backgroundColor: barColors,
      data: a
    }]
  },
  options: {
    legend: { display: false },
    title: {
      display: true,
      text: "OCEAN Personality Result"
    }
  }
});
let nxValues = ["Anxiety", "Anger", "Depression", "Self-Consciousness", "Immoderation", "Vulnerability"];
new Chart("nChart", {
  type: "bar",
  data: {
    labels: nxValues,
    datasets: [{
      backgroundColor: barColors,
      data: n
    }]
  },
  options: {
    legend: { display: false },
    title: {
      display: true,
      text: "OCEAN Personality Result"
    }
  }
});