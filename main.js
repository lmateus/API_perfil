const url = 'http://localhost:4000/products'

const CHART = document.getElementById('lineChart')
function plot (distancia,elevacion) {
  let lineChart = new Chart(CHART, {
    type: 'line',
    data: {
      labels: distancia,
      datasets: [
        {
          label: 'Perfil',
          backgroundColor: 'rgb(255, 99, 132)',
          borderColor: 'rgb(255, 99, 132)',
          data: elevacion
        }
      ]
    },
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: 'Axis Center Positioning'
        }
      },
      scales: {

        y: {
          min: 2506.5,
          max: 2606.5,
        }
      }
    }
  })
}

fetch(url, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin':	'*',

  },
  body: JSON.stringify({
    "Punto_inicial": [-74.179157, 4.611494 ],
  "Punto_final":[-74.177870, 4.611686]
  })  
}) 
.then(response => response.json())
.then(data => plot(data.distancia_x,data.elevacion))






