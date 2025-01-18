<script lang="ts">
	import { onMount } from "svelte";
	import { Chart } from "chart.js/auto";
	import { Flow, SankeyController } from "chartjs-chart-sankey";

	Chart.register(SankeyController, Flow);

	let canvas: HTMLCanvasElement;

	onMount(() => {
		new Chart(canvas, {
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
					tooltip: {
						callbacks: {
							label: function (context) {
								return `${context.parsed._custom.from.key} → ${context.parsed._custom.to.key}: ${context.parsed._custom.flow}`;
							}
						}
					}
				}
			}
		});
	});
</script>

<canvas bind:this={canvas}></canvas>
