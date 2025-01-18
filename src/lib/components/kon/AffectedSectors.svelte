<script lang="ts">
	import { Chart } from "chart.js/auto";
	import { onMount } from "svelte";

	let canvas: HTMLCanvasElement;

	onMount(() => {
		new Chart(canvas, {
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
						data: [2650, 2670, 2650, 2650, 2680],
						backgroundColor: "rgba(255, 99, 132, 0.5)",
						borderColor: "rgba(255, 99, 132, 1)",
						borderWidth: 1
					},
					{
						label: "Phishing",
						data: [2685, 2665, 2660, 2660, 2675],
						backgroundColor: "rgba(54, 162, 235, 0.5)",
						borderColor: "rgba(54, 162, 235, 1)",
						borderWidth: 1
					},
					{
						label: "DDoS",
						data: [2640, 2635, 2650, 2630, 2610],
						backgroundColor: "rgba(75, 192, 192, 0.5)",
						borderColor: "rgba(75, 192, 192, 1)",
						borderWidth: 1
					}
				]
			},
			options: {
				responsive: true,
				plugins: {
					title: {
						display: true,
						text: "Betroffene Sektoren nach Angriffstyp"
					},
					legend: {
						display: true,
						position: "top"
					}
				},
				scales: {
					x: {
						stacked: true,
						title: {
							display: true,
							text: "Sektoren"
						}
					},
					y: {
						stacked: true,
						title: {
							display: true,
							text: "Anzahl der Vorfälle"
						},
						suggestedMax: 14000
					}
				}
			}
		});
	});
</script>

<canvas bind:this={canvas}></canvas>
