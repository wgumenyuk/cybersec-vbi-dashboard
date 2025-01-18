<script lang="ts">
	import { theme } from "$lib/theme.svelte";
	import { Chart } from "chart.js/auto";
	import { onMount } from "svelte";

	let canvas: HTMLCanvasElement;

	onMount(() => {
		new Chart(canvas, {
			type: "bar",
			data: {
				labels: ["Malware", "Phishing", "DDoS", "Ransomware"],
				datasets: [
					{
						label: "Anzahl der Angriffe",
						data: [13307, 13428, 13265, 13265],
						backgroundColor: [
							"rgba(255, 99, 132, 0.5)",
							"rgba(54, 162, 235, 0.5)",
							"rgba(75, 192, 192, 0.5)",
							"rgba(255, 206, 86, 0.5)",
							"rgba(153, 102, 255, 0.5)"
						],
						borderColor: [
							"rgba(255, 99, 132, 1)",
							"rgba(54, 162, 235, 1)",
							"rgba(75, 192, 192, 1)",
							"rgba(255, 206, 86, 1)",
							"rgba(153, 102, 255, 1)"
						],
						borderWidth: 1
					}
				]
			},
			options: {
				plugins: {
					legend: {
						display: false
					}
				},
				indexAxis: "y",
				scales: {
					x: {
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
