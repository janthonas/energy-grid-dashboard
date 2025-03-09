async function fetchEnergyData() {
    try {
        const response = await fetch('api/energy-averages/');
        const data = await response.json();

        const labels = data.map(entry => entry.date);
        const fossilFreeValues = data.map(entry => entry.avg_fossil_free);
        const productionValues = data.map(entry => entry.avg_production);
        const consumptionValues = data.map(entry => entry.avg_consumption);

        // **Chart 1: Fossil-Free Percentage**
        const ctx1 = document.getElementById('fossilFreeChart').getContext('2d');
        new Chart(ctx1, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [
                    {
                        label: 'Fossil-Free Percentage',
                        data: fossilFreeValues,
                        borderColor: 'green',
                        borderWidth: 2,
                        fill: false
                    }
                ]
            },
            options: {
                responsive: true,
                scales: {
                    y: { beginAtZero: true }
                }
            }
        });

        // **Chart 2: Production vs Consumption**
        const ctx2 = document.getElementById('prodConsChart').getContext('2d');
        new Chart(ctx2, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [
                    {
                        label: 'Average Production',
                        data: productionValues,
                        borderColor: 'blue',
                        borderWidth: 2,
                        fill: false
                    },
                    {
                        label: 'Average Consumption',
                        data: consumptionValues,
                        borderColor: 'red',
                        borderWidth: 2,
                        fill: false
                    }
                ]
            },
            options: {
                responsive: true,
                scales: {
                    y: { beginAtZero: true }
                }
            }
        });

    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

window.onload = fetchEnergyData;

