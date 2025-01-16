<script lang="ts">
	import { Chart } from "chart.js/auto";
	import { onMount } from "svelte";

	onMount(() => {
		new Chart("bubbleChart", {
			type: "bubble",
			data: {
				datasets: [
					{
						label: "HTTP",
						data: [{ x: 1, y: 100, r: 15 }],
						backgroundColor: "rgba(54, 162, 235, 0.8)"
					},
					{
						label: "DNS",
						data: [{ x: 2, y: 150, r: 20 }],
						backgroundColor: "rgba(255, 99, 132, 0.8)"
					},
					{
						label: "FTP",
						data: [{ x: 3, y: 50, r: 10 }],
						backgroundColor: "rgba(75, 192, 192, 0.8)"
					}
				]
			},
			options: {
				plugins: {
					title: {
						display: true,
						text: "Wie nutzen Angriffe verschiedene Protokolle?"
					}
				},
				scales: {
					x: {
						title: {
							display: true,
							text: "Protokoll-Komplexität (Skala)"
						}
					},
					y: {
						title: {
							display: true,
							text: "Anzahl der Angriffe"
						}
					}
				}
			}
		});
	});
</script>

<canvas id="bubbleChart"></canvas>
