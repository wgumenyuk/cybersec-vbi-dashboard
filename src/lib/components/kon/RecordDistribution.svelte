<script lang="ts">
	import { Chart } from "chart.js/auto";
	import { onMount } from "svelte";

	onMount(() => {
		new Chart("recordDistributionChart", {
			type: "doughnut",
			data: {
				labels: ["<1k", "1k-10k", "10k-50k", "50k-100k", ">100k"],
				datasets: [
					{
						label: "Records Affected",
						data: [50, 120, 200, 100, 50]
					}
				]
			}
		});
	});
</script>

<canvas id="recordDistributionChart"></canvas>
