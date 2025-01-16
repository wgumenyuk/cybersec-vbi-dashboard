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
						pointRadius: 5
					}
				]
			},
			options: {
				plugins: {
					legend: {
						display: false
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
