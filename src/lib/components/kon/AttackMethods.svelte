<script lang="ts">
	import { Chart } from "chart.js/auto";
	import { onMount } from "svelte";

	let canvas: HTMLCanvasElement;

	onMount(() => {
		new Chart(canvas, {
			type: "bar",
			data: {
				labels: [
					"Malware",
					"Phishing",
					"DDoS",
					"Ransomware",
					"Intrusion"
				],
				datasets: [
					{
						data: [120, 90, 150, 60, 30]
					}
				]
			},
			options: {
				plugins: {
					legend: {
						display: false
					}
				},
				indexAxis: "y"
			}
		});
	});
</script>

<canvas bind:this={canvas}></canvas>
