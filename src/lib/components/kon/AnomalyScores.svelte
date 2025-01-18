<script lang="ts">
	import { Chart } from "chart.js/auto";
	import { onMount } from "svelte";
	import { theme } from "$lib/theme.svelte";

	let canvas: HTMLCanvasElement;

	onMount(() => {
		new Chart(canvas, {
			type: "radar",
			data: {
				labels: [
					"Malware",
					"DDoS",
					"Intrusion",
					"Phishing",
					"Ransomware"
				],
				datasets: [
					{
						data: [50.13, 50.24, 49.85, 47.92, 45.67],
						pointRadius: 5,
						backgroundColor: "rgba(54, 162, 235, 0.2)",
						borderColor: "rgba(54, 162, 235, 1)"
					}
				]
			},
			options: {
				plugins: {
					legend: {
						display: false
					}
				},
				scales: {
					r: {
						angleLines: {
							display: true
						},
						suggestedMin: 0,
						suggestedMax: 60,
						ticks: {
							stepSize: 10
						},
						grid: {
							color:
								theme === "dark"
									? "rgba(255, 255, 255, 0.25)"
									: "rgba(0, 0, 0, 0.25)"
						}
					}
				}
			}
		});
	});
</script>

<canvas bind:this={canvas}></canvas>
