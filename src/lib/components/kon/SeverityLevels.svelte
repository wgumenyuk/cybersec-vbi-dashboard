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
						data: [30, 50, 20, 10],
						backgroundColor: "rgba(54, 162, 235, 0.8)"
					},
					{
						label: "Phishing",
						data: [20, 40, 30, 10],
						backgroundColor: "rgba(255, 99, 132, 0.8)"
					},
					{
						label: "DDoS",
						data: [10, 30, 50, 20],
						backgroundColor: "rgba(75, 192, 192, 0.8)"
					}
				]
			},
			options: {
				plugins: {
					title: {
						display: true,
						text: "Wie tragen Angriffsmethoden zu den Schweregraden bei?"
					}
				},
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
