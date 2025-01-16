<script lang="ts">
	import { Chart } from "chart.js/auto";
	import { Flow } from "chartjs-chart-sankey";
	import { SankeyController } from "chartjs-chart-sankey";
	import { onMount } from "svelte";

	Chart.register(SankeyController, Flow);

	onMount(() => {
		new Chart("sankeyChart", {
			type: "sankey",
			data: {
				datasets: [
					{
						label: "Angriffsmethoden -> Branchen",
						data: [
							{ from: "Malware", to: "Finance", flow: 50 },
							{ from: "Malware", to: "Healthcare", flow: 70 },
							{ from: "Phishing", to: "Retail", flow: 40 },
							{ from: "DDoS", to: "Government", flow: 30 },
							{ from: "Ransomware", to: "Education", flow: 20 }
						],
						colorFrom: () => "rgba(54, 162, 235, 0.8)",
						colorTo: () => "rgba(255, 99, 132, 0.8)",
						colorMode: "gradient"
					}
				]
			},
			options: {
				plugins: {
					title: {
						display: true,
						text: "Wie beeinflussen Angriffsmethoden verschiedene Branchen?"
					}
				}
			}
		});
	});
</script>

<canvas id="sankeyChart"></canvas>
