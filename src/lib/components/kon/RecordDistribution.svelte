<script lang="ts">
	import { Chart } from "chart.js/auto";
	import { onMount } from "svelte";

	onMount(() => {
		new Chart("recordDistributionChart", {
			type: "pie",
			data: {
				labels: ["<1k", "1k-10k", "10k-50k", "50k-100k", ">100k"],
				datasets: [
					{
						label: "Records Affected",
						data: [50, 120, 200, 100, 50],
						backgroundColor: [
							"rgba(54, 162, 235, 0.8)",
							"rgba(54, 162, 235, 0.6)",
							"rgba(54, 162, 235, 0.4)",
							"rgba(54, 162, 235, 0.2)",
							"rgba(54, 162, 235, 1.0)"
						]
					}
				]
			},
			options: {
				plugins: {
					title: {
						display: true,
						text: "Verteilung der betroffenen Datensätze (Sunburst-Visualisierung)"
					}
				}
			} // Schließt die options-Konfiguration
		}); // Schließt die Chart-Initialisierung
	});
</script>

<canvas id="recordDistributionChart"></canvas>
