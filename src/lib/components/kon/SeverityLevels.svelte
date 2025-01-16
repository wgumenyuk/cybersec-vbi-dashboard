<script>
	import { Chart } from "chart.js/auto";
	import { onMount } from "svelte";

	onMount(() => {
		new Chart("severityLevelsChart", {
			type: "bar",
			data: {
				labels: ["Low", "Medium", "High", "Critical"],
				datasets: [
					{
						label: "Malware",
						data: [30, 50, 20, 10]
					},
					{
						label: "Phishing",
						data: [20, 40, 30, 10]
					},
					{
						label: "DDoS",
						data: [10, 30, 50, 20]
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

<canvas id="severityLevelsChart"></canvas>
