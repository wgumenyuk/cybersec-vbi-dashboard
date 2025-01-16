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
						data: [4.5, 3.8, 4.2, 3.6, 4.1],
						backgroundColor: "rgba(54, 162, 235, 0.2)",
						borderColor: "rgba(54, 162, 235, 1.0)",
						borderWidth: 2,
						pointBackgroundColor: "rgba(54, 162, 235, 1.0)",
						pointRadius: 5
					}
				]
			},
			options: {
				plugins: {
					title: {
						display: true,
						text: "Anomalie-Scores nach Angriffstyp (Radar Chart)"
					},
					tooltip: {
						callbacks: {
							label: function (tooltipItem) {
								return `${tooltipItem.label}: ${tooltipItem.raw}`;
							}
						}
					}
				},
				scales: {
					r: {
						angleLines: {
							display: true
						},
						suggestedMin: 0,
						suggestedMax: 5,
						ticks: {
							stepSize: 1
						}
					}
				}
			}
		});
	});
</script>

<canvas id="anomalyScoresChart"></canvas>
