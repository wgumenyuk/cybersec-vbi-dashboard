<script lang="ts">
	import { Chart } from "chart.js/auto";
	import { onMount } from "svelte";

	onMount(() => {
		new Chart("affectedSectorsChart", {
			type: "bar",
			data: {
				labels: [
					"Finance",
					"Healthcare",
					"Retail",
					"Education",
					"Government"
				],
				datasets: [
					{
						label: "Malware",
						data: [50, 70, 30, 20, 40]
					},
					{
						label: "Phishing",
						data: [60, 50, 40, 30, 50]
					},
					{
						label: "DDoS",
						data: [30, 20, 10, 10, 25]
					}
				]
			},
			options: {
				responsive: true,
				scales: {
					x: {
						stacked: true
					},
					y: {
						stacked: true
					}
				}
			}
		});
	});
</script>

<canvas id="affectedSectorsChart"></canvas>
