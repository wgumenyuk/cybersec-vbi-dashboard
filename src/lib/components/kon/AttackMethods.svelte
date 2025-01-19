<script lang="ts">
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
						label: "Gesamthäufigkeit der Angriffe (2020–2023)",
						data: [19307, 18000, 19428, 7894],
						backgroundColor: [
							"rgba(255, 99, 132, 0.5)",
							"rgba(54, 162, 235, 0.5)",
							"rgba(75, 192, 192, 0.5)",
							"rgba(153, 102, 255, 0.5)"
						],
						borderColor: [
							"rgba(255, 99, 132, 1)",
							"rgba(54, 162, 235, 1)",
							"rgba(75, 192, 192, 1)",
							"rgba(153, 102, 255, 1)"
						],
						borderWidth: 1
					}
				]
			},
			options: {
				plugins: {
					title: {
						display: true,
						text: "Gesamthäufigkeit der Angriffe nach Typ (2020–2023)"
					},
					legend: {
						display: true
					}
				},
				indexAxis: "y",
				scales: {
					x: {
						title: {
							display: true,
							text: "Gesamthäufigkeit der Angriffe"
						}
					},
					y: {
						title: {
							display: true,
							text: "Angriffsarten"
						}
					}
				}
			}
		});
	});
</script>

<canvas bind:this={canvas}></canvas>
