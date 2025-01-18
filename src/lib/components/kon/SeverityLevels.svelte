<script lang="ts">
	import { Chart } from "chart.js/auto";
	import { onMount } from "svelte";

	let canvas: HTMLCanvasElement;

	onMount(() => {
		new Chart(canvas, {
			type: "bar",
			data: {
				labels: ["Low", "Medium", "High"], // Schweregrade aus dem Dataset
				datasets: [
					{
						label: "Malware",
						data: [4359, 4516, 4432], // Daten für Malware
						backgroundColor: "rgba(255, 99, 132, 0.5)",
						borderColor: "rgba(255, 99, 132, 1)",
						borderWidth: 1
					},
					{
						label: "Phishing",
						data: [0, 0, 0], // Keine Phishing-Daten im Dataset
						backgroundColor: "rgba(54, 162, 235, 0.5)",
						borderColor: "rgba(54, 162, 235, 1)",
						borderWidth: 1
					},
					{
						label: "DDoS",
						data: [4450, 4455, 4523], // Daten für DDoS
						backgroundColor: "rgba(75, 192, 192, 0.5)",
						borderColor: "rgba(75, 192, 192, 1)",
						borderWidth: 1
					},
					{
						label: "Intrusion",
						data: [4374, 4464, 4427], // Daten für Intrusion
						backgroundColor: "rgba(153, 102, 255, 0.5)",
						borderColor: "rgba(153, 102, 255, 1)",
						borderWidth: 1
					}
				]
			},
			options: {
				responsive: true,
				plugins: {
					title: {
						display: true,
						text: "Schweregrade der Angriffe nach Typ"
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
							text: "Schweregrad"
						}
					},
					y: {
						stacked: true,
						title: {
							display: true,
							text: "Anzahl der Vorfälle"
						}
					}
				}
			}
		});
	});
</script>

<canvas bind:this={canvas}></canvas>
