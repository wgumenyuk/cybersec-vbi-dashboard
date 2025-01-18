<script lang="ts">
	import { onMount } from "svelte";
	import { Chart } from "chart.js/auto";
	import { Flow, SankeyController } from "chartjs-chart-sankey";

	Chart.register(SankeyController, Flow);

	onMount(() => {
		new Chart("sankeyChart", {
			type: "sankey",
			data: {
				datasets: [
					{
						data: [
							{ from: "Malware", to: "Finance", flow: 5000 },
							{ from: "Malware", to: "Healthcare", flow: 4000 },
							{ from: "Phishing", to: "Retail", flow: 3000 },
							{ from: "Phishing", to: "Finance", flow: 3500 },
							{ from: "DDoS", to: "Government", flow: 2500 },
							{ from: "DDoS", to: "Retail", flow: 2000 },
							{ from: "Malware", to: "Retail", flow: 3000 },
							{ from: "Phishing", to: "Education", flow: 1500 },
							{ from: "Ransomware", to: "Education", flow: 2000 },
							{ from: "Ransomware", to: "Healthcare", flow: 3500 }
						],
						colorFrom: () => "rgba(54, 162, 235, 1)",
						colorTo: () => "rgba(255, 99, 132, 1)",
						colorMode: "gradient"
					}
				]
			},
			options: {
				plugins: {
					title: {
						display: true,
						text: "Cyberangriffe nach Typ und Zielsektor"
					},
					tooltip: {
						callbacks: {
							label: function (context) {
								return `${context.raw.from} → ${context.raw.to}: ${context.raw.flow}`;
							}
						}
					}
				}
			}
		});
	});
</script>

<canvas id="sankeyChart"></canvas>
