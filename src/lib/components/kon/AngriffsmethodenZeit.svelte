<script lang="ts">
	import { theme } from "$lib/theme.svelte";
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
						data: [5533, 5545, 4558, 3792],
						backgroundColor: "rgba(75, 192, 192, 0.5)",
						borderColor: "rgba(75, 192, 192, 1)",
						borderWidth: 1
					},
					{
						label: "Intrusion",
						data: [4551, 4575, 3563, 2676],
						backgroundColor: "rgba(54, 162, 235, 0.5)",
						borderColor: "rgba(54, 162, 235, 1)",
						borderWidth: 1
					},
					{
						label: "Malware",
						data: [5489, 5518, 4629, 3671],
						backgroundColor: "rgba(255, 99, 132, 0.5)",
						borderColor: "rgba(255, 99, 132, 1)",
						borderWidth: 1
					},
					{
						label: "Ransomware",
						data: [2523, 2561, 1610, 1200],
						backgroundColor: "rgba(153, 102, 255, 0.5)",
						borderColor: "rgba(153, 102, 255, 1)",
						borderWidth: 1
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
