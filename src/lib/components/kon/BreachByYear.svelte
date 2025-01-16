<script lang="ts">
	import { onMount } from "svelte";
	import { Chart } from "chart.js/auto";

	onMount(() => {
		new Chart("breachByYearChart", {
			type: "line",
			data: {
				labels: ["2018", "2019", "2020", "2021", "2022"],
				datasets: [
					{
						label: "Malware",
						data: [120, 150, 140, 160, 200],
						fill: false
					},
					{
						label: "Phishing",
						data: [100, 120, 110, 130, 140],
						fill: false
					}
				]
			},
			options: {
				scales: {
					y: {
						suggestedMin: 0
					}
				}
			}
		});
	});
</script>

<canvas id="breachByYearChart"></canvas>
