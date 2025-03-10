async function fetchAllEnergyData() {
    try {
        // Fetch Energy Averages
        const energyResponse = await fetch('/api/energy-averages/');
        const energyData = await energyResponse.json();

        // Fetch Production Consumption Breakdown
        const productionResponse = await fetch('/api/production_consumption_source/');
        const productionData = await productionResponse.json();

        if (energyData.error || productionData.error) {
            console.error("Error fetching energy data");
            return;
        }

        // **Line Chart Data (Fossil-Free, Production, Consumption)**
        const labels = energyData.map(entry => entry.date);
        const fossilFreeValues = energyData.map(entry => entry.avg_fossil_free);
        const productionValues = energyData.map(entry => entry.avg_production);
        const consumptionValues = energyData.map(entry => entry.avg_consumption);

        // **Pie Chart Data (Energy Breakdown)**
        const pieLabels = [
            "Nuclear", "Geothermal", "Biomass", "Coal", "Wind", 
            "Solar", "Hydro", "Gas", "Oil"
        ];
        const pieValues = [
            productionData.nuclear_consumption,
            productionData.geothermal_consumption,
            productionData.biomass_consumption,
            productionData.coal_consumption,
            productionData.wind_consumption,
            productionData.solar_consumption,
            productionData.hydro_consumption,
            productionData.gas_consumption,
            productionData.oil_consumption
        ];
        const pieColors = [
            "#4B0082", "#FF5733", "#228B22", "#696969", "#87CEEB", 
            "#FFD700", "#1E90FF", "#A52A2A", "#000000"
        ];

        // **Chart 1: Fossil-Free Percentage**
        const ctx1 = document.getElementById('fossilFreeChart').getContext('2d');
        new Chart(ctx1, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Fossil-Free Percentage',
                    data: fossilFreeValues,
                    borderColor: 'green',
                    borderWidth: 2,
                    fill: false
                }]
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

        // **Chart 3: Energy Production Breakdown (Pie Chart)**
        const ctx3 = document.getElementById('energyPieChart').getContext('2d');
        new Chart(ctx3, {
            type: 'pie',
            data: {
                labels: pieLabels,
                datasets: [{
                    label: 'Energy Sources Breakdown',
                    data: pieValues,
                    backgroundColor: pieColors
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { position: 'right' }
                }
            }
        });

    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

// Load all charts when the page loads
window.onload = fetchAllEnergyData;
