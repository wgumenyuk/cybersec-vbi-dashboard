<script lang="ts">
	import { Chart } from "chart.js/auto";
	import { onMount } from "svelte";

	let canvas: HTMLCanvasElement;

	onMount(() => {
		new Chart(canvas, {
			type: "bar",
			data: {
				labels: ["2018", "2019", "2020", "2021", "2022"], // Jahre auf der x-Achse
				datasets: [
					{
						label: "Malware",
						data: [50, 70, 0, 0, 0], // Häufigkeiten pro Jahr
						backgroundColor: "rgba(54, 162, 235, 0.8)"
					},
					{
						label: "Phishing",
						data: [0, 0, 40, 0, 0],
						backgroundColor: "rgba(255, 99, 132, 0.8)"
					},
					{
						label: "DDoS",
						data: [0, 0, 0, 30, 0],
						backgroundColor: "rgba(75, 192, 192, 0.8)"
					},
					{
						label: "Ransomware",
						data: [0, 0, 0, 0, 20],
						backgroundColor: "rgba(153, 102, 255, 0.8)"
					}
				]
			},
			options: {
				plugins: {
					title: {
						display: true,
						text: "Wie variieren Angriffsmethoden über die Zeit?"
					}
				},
				responsive: true,
				scales: {
					x: {
						stacked: true, // Gestapelte Balken
						title: {
							display: true,
							text: "Jahr"
						}
					},
					y: {
						stacked: true, // Gestapelte Balken
						title: {
							display: true,
							text: "Häufigkeit"
						}
					}
				}
			}
		});
	});
</script>

<canvas bind:this={canvas}></canvas>
