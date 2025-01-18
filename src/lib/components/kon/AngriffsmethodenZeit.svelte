<script lang="ts">
	import { Chart } from "chart.js/auto";
	import { onMount } from "svelte";

	let canvas: HTMLCanvasElement;

	onMount(() => {
		new Chart(canvas, {
			type: "bar",
			data: {
				labels: ["2020", "2021", "2022", "2023"],
				datasets: [
					{
						label: "DDoS",
						data: [3533, 3545, 3558, 2792],
						backgroundColor: "rgba(75, 192, 192, 0.5)",
						borderColor: "rgba(75, 192, 192, 1)",
						borderWidth: 1
					},
					{
						label: "Intrusion",
						data: [3551, 3475, 3563, 2676],
						backgroundColor: "rgba(54, 162, 235, 0.5)",
						borderColor: "rgba(54, 162, 235, 1)",
						borderWidth: 1
					},
					{
						label: "Malware",
						data: [3489, 3518, 3629, 2671],
						backgroundColor: "rgba(255, 99, 132, 0.5)",
						borderColor: "rgba(255, 99, 132, 1)",
						borderWidth: 1
					}
				]
			},
			options: {
				responsive: true,
				scales: {
					x: {
						stacked: true,
						title: {
							display: true,
							text: "Jahre"
						}
					},
					y: {
						stacked: true,
						title: {
							display: true,
							text: "Anzahl der Angriffe"
						}
					}
				},
				plugins: {
					legend: {
						position: "top"
					},
					title: {
						display: true,
						text: "Cybersecurity-Angriffe pro Jahr"
					}
				}
			}
		});
	});
</script>

<canvas bind:this={canvas}></canvas>
