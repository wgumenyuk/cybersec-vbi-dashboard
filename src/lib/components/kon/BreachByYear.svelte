<script lang="ts">
	import { theme } from "$lib/theme.svelte";
	import { Chart } from "chart.js/auto";
	import { onMount } from "svelte";

	//visualisierung kann ich löschen!!!

	let canvas: HTMLCanvasElement;

	onMount(() => {
		new Chart(canvas, {
			type: "line",
			data: {
				labels: ["2018", "2019", "2020", "2021", "2022"],
				datasets: [
					{
						label: "Malware",
						data: [120, 150, 140, 160, 200],
						fill: false,
						borderColor: "rgba(255, 99, 132, 1)",
						backgroundColor: "rgba(255, 99, 132, 0.5)"
					},
					{
						label: "Phishing",
						data: [100, 120, 110, 130, 140],
						fill: false,
						borderColor: "rgba(54, 162, 235, 1)",
						backgroundColor: "rgba(54, 162, 235, 0.5)"
					}
				]
			},
			options: {
				plugins: {
					title: {
						display: true,
						text: "Cyberangriffe pro Jahr"
					},
					legend: {
						display: true,
						position: "top"
					}
				},
				scales: {
					y: {
						suggestedMin: 0,
						title: {
							display: true,
							text: "Anzahl der Angriffe"
						},
						grid: {
							color:
								theme === "dark"
									? "rgba(255, 255, 255, 0.25)"
									: "rgba(0, 0, 0, 0.25)"
						}
					},
					x: {
						title: {
							display: true,
							text: "Jahre"
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
