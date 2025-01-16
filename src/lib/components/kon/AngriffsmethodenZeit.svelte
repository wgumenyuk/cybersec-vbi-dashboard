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
						data: [50, 70, 0, 0, 0] // Häufigkeiten pro Jahr
					},
					{
						label: "Phishing",
						data: [0, 0, 40, 0, 0]
					},
					{
						label: "DDoS",
						data: [0, 0, 0, 30, 0]
					},
					{
						label: "Ransomware",
						data: [0, 0, 0, 0, 20]
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
						stacked: true,
						title: {
							display: true,
							text: "# of Attacks"
						}
					}
				}
			}
		});
	});
</script>

<canvas bind:this={canvas}></canvas>
