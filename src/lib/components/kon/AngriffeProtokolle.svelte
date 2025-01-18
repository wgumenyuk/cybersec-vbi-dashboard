<script lang="ts">
	import { Chart } from "chart.js/auto";
	import { onMount } from "svelte";
	import { theme } from "$lib/theme.svelte";

	let canvas: HTMLCanvasElement;

	onMount(() => {
		new Chart(canvas, {
			type: "bubble",
			data: {
				datasets: [
					{
						label: "HTTP",
						data: [
							{ x: 1, y: 5000, r: 30 },
							{ x: 2, y: 5200, r: 35 },
							{ x: 3, y: 5400, r: 40 }
						],
						backgroundColor: "rgba(255, 99, 132, 0.5)"
					},
					{
						label: "DNS",
						data: [
							{ x: 2, y: 6000, r: 35 },
							{ x: 3, y: 6500, r: 40 },
							{ x: 4, y: 7000, r: 45 }
						],
						backgroundColor: "rgba(54, 162, 235, 0.5)"
					},
					{
						label: "FTP",
						data: [
							{ x: 3, y: 3000, r: 20 },
							{ x: 4, y: 3500, r: 25 },
							{ x: 5, y: 4000, r: 30 }
						],
						backgroundColor: "rgba(75, 192, 192, 0.5)"
					},
					{
						label: "HTTPS",
						data: [
							{ x: 1, y: 5500, r: 28 },
							{ x: 2, y: 5700, r: 32 },
							{ x: 3, y: 5900, r: 38 }
						],
						backgroundColor: "rgba(255, 206, 86, 0.5)"
					},
					{
						label: "SMTP",
						data: [
							{ x: 2, y: 4000, r: 20 },
							{ x: 3, y: 4300, r: 22 },
							{ x: 4, y: 4600, r: 24 }
						],
						backgroundColor: "rgba(153, 102, 255, 0.5)"
					},
					{
						label: "ICMP",
						data: [
							{ x: 3, y: 3500, r: 18 },
							{ x: 4, y: 3700, r: 20 },
							{ x: 5, y: 3900, r: 22 }
						],
						backgroundColor: "rgba(201, 203, 207, 0.5)"
					}
				]
			},
			options: {
				scales: {
					x: {
						title: {
							display: true,
							text: "Attack Complexity"
						},
						grid: {
							color:
								theme === "dark"
									? "rgba(255, 255, 255, 0.25)"
									: "rgba(0, 0, 0, 0.25)"
						}
					},
					y: {
						title: {
							display: true,
							text: "# of Attacks"
						},
						grid: {
							color:
								theme === "dark"
									? "rgba(255, 255, 255, 0.25)"
									: "rgba(0, 0, 0, 0.25)"
						},
						suggestedMin: 0,
						suggestedMax: 8000
					}
				}
			}
		});
	});
</script>

<canvas bind:this={canvas}></canvas>
