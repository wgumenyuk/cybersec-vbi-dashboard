<script lang="ts">
	import { Chart } from "chart.js/auto";
	import { onMount } from "svelte";

	onMount(() => {
		new Chart("anomalyScoresChart", {
			type: "radar",
			data: {
				labels: [
					"Malware",
					"DDoS",
					"Intrusion",
					"Phishing",
					"Ransomware"
				],
				datasets: [
					{
						label: "Anomalie-Scores",
						data: [50.13, 50.24, 49.98, 0, 0],
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
						text: "Anomalie-Scores nach Angriffstyp"
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
						suggestedMax: 60,
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
