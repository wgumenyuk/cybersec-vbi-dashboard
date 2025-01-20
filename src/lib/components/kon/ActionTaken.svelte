<script lang="ts">
	import { Chart } from "chart.js/auto";
	import { onMount } from "svelte";

	let canvas: HTMLCanvasElement;

	onMount(() => {
		new Chart(canvas, {
			type: "bar",
			data: {
				labels: ["Malware", "DDoS", "Phishing", "Ransomware"],
				datasets: [
					{
						label: "Logged",
						data: [3500, 2700, 2200, 2000],
						backgroundColor: "rgba(54, 162, 235, 0.5)",
						borderColor: "rgba(54, 162, 235, 1)",
						borderWidth: 1
					},
					{
						label: "Blocked",
						data: [4200, 3203, 4350, 1500],
						backgroundColor: "rgba(75, 192, 192, 0.5)",
						borderColor: "rgba(75, 192, 192, 1)",
						borderWidth: 1
					},
					{
						label: "Ignored",
						data: [800, 600, 930, 500],
						backgroundColor: "rgba(255, 99, 132, 0.5)",
						borderColor: "rgba(255, 99, 132, 1)",
						borderWidth: 1
					}
				]
			},
			options: {
				responsive: true,
				plugins: {
					title: {
						display: true,
						text: "Actions Taken per Attack Type"
					},
					legend: {
						position: "top"
					}
				},
				scales: {
					x: {
						stacked: true,
						title: {
							display: true,
							text: "Attack Types"
						}
					},
					y: {
						stacked: true,
						title: {
							display: true,
							text: "Number of Actions"
						}
					}
				}
			}
		});
	});
</script>

<canvas bind:this={canvas}></canvas>
