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
							{ from: "Malware", to: "Finance", flow: 50 },
							{ from: "Malware", to: "Healthcare", flow: 70 },
							{ from: "Phishing", to: "Retail", flow: 40 },
							{ from: "DDoS", to: "Government", flow: 30 },
							{ from: "Ransomware", to: "Education", flow: 20 }
						],
						colorFrom: () => "rgba(54, 162, 235, 1)",
						colorTo: () => "rgba(255, 99, 132, 1)",
						colorMode: "gradient"
					}
				]
			}
		});
	});
</script>

<canvas id="sankeyChart"></canvas>
