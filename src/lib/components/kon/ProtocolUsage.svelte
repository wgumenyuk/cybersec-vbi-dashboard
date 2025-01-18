<script lang="ts">
	import { theme } from "$lib/theme.svelte";
	import { Chart } from "chart.js/auto";
	import { onMount } from "svelte";

	let canvas: HTMLCanvasElement;

	onMount(() => {
		new Chart(canvas, {
			type: "bar",
			data: {
				labels: ["HTTP", "HTTPS", "DNS", "FTP", "ICMP"],
				datasets: [
					{
						label: "Requests",
						data: [150, 120, 100, 80, 60],
						backgroundColor: "rgba(54, 162, 235, 0.5)",
						borderColor: "rgba(54, 162, 235, 1)",
						borderWidth: 1
					},
					{
						label: "Responses",
						data: [130, 110, 90, 70, 50],
						backgroundColor: "rgba(75, 192, 192, 0.5)",
						borderColor: "rgba(75, 192, 192, 1)",
						borderWidth: 1
					},
					{
						label: "Errors",
						data: [20, 10, 10, 10, 10],
						backgroundColor: "rgba(255, 99, 132, 0.5)",
						borderColor: "rgba(255, 99, 132, 1)",
						borderWidth: 1
					}
				]
			},
			options: {
				responsive: true,
				plugins: {
					legend: {
						display: true
					}
				},
				scales: {
					x: {
						stacked: true
					},
					y: {
						stacked: true,
						title: {
							display: true,
							text: "# of Interactions"
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
