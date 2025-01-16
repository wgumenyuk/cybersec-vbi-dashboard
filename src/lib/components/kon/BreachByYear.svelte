<script lang="ts">
	import { Chart } from "chart.js/auto";
	import { onMount } from "svelte";

	onMount(() => {
		new Chart("breachByYearChart", {
			type: "line",
			data: {
				labels: ["2018", "2019", "2020", "2021", "2022"],
				datasets: [
					{
						label: "Malware",
						data: [120, 150, 140, 160, 200],
						borderColor: "rgba(54, 162, 235, 1.0)",
						fill: false
					},
					{
						label: "Phishing",
						data: [100, 120, 110, 130, 140],
						borderColor: "rgba(255, 99, 132, 1.0)",
						fill: false
					}
				]
			},
			options: {
				plugins: {
					title: {
						display: true,
						text: "Wie haben Sicherheitsverletzungen nach Angriffstyp zugenommen?"
					}
				}
			}
		});
	});
</script>

<canvas id="breachByYearChart"></canvas>
