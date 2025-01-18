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
						data: [50, 120, 200, 100, 50],
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
				responsive: true,
				plugins: {
					title: {
						display: true,
						text: "Verteilung der betroffenen Datensätze"
					},
					legend: {
						display: true,
						position: "top"
					}
				}
			}
		});
	});
</script>

<canvas id="recordDistributionChart"></canvas>
