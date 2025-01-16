<script lang="ts">
	import { Chart } from "chart.js/auto";
	import { onMount } from "svelte";

	onMount(() => {
		new Chart("bubbleChart", {
			type: "bubble",
			data: {
				datasets: [
					{
						label: "HTTP",
						data: [{ x: 1, y: 100, r: 15 }]
					},
					{
						label: "DNS",
						data: [{ x: 2, y: 150, r: 20 }]
					},
					{
						label: "FTP",
						data: [{ x: 3, y: 50, r: 10 }]
					}
				]
			},
			options: {
				scales: {
					x: {
						title: {
							display: true,
							text: "Protocol Complexity"
						}
					},
					y: {
						title: {
							display: true,
							text: "# of Attacks"
						},
						suggestedMin: 0
					}
				}
			}
		});
	});
</script>

<canvas id="bubbleChart"></canvas>
