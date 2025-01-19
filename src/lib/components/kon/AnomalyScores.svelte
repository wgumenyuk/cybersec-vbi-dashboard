<script lang="ts">
	import { Chart } from "chart.js/auto";
	import { onMount } from "svelte";

	onMount(() => {
		new Chart("anomalyScoresChart", {
			type: "radar",
			data: {
				labels: ["Malware", "DDoS", "Phishing", "Ransomware"],
				datasets: [
					{
						label: "Anomalie-Scores (2020–2023)",
						data: [54.13, 49.24, 37.92, 43.67],
						pointRadius: 5,
						backgroundColor: "rgba(54, 162, 235, 0.2)",
						borderColor: "rgba(54, 162, 235, 1)"
					}
				]
			},
			options: {
				plugins: {
					title: {
						display: true,
						text: "Anomalie-Scores nach Angriffstyp (2020–2023)"
					},
					legend: {
						display: true,
						position: "top"
					}
				},
				scales: {
					r: {
						angleLines: {
							display: true
						},
						suggestedMin: 0,
						suggestedMax: 60, // Angepasst an die Skala der Scores
						ticks: {
							stepSize: 10
						}
					}
				}
			}
		});
	});
</script>

<canvas id="anomalyScoresChart"></canvas>
