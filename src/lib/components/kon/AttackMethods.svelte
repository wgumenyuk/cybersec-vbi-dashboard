<script lang="ts">
	import { Chart } from "chart.js/auto";

	new Chart("attackMethodsChart", {
		type: "bar",
		data: {
			labels: ["Malware", "Phishing", "DDoS", "Ransomware", "Intrusion"],
			datasets: [
				{
					backgroundColor: [
						"rgba(54, 162, 235, 0.8)",
						"rgba(54, 162, 235, 0.6)",
						"rgba(54, 162, 235, 0.4)",
						"rgba(54, 162, 235, 0.2)",
						"rgba(54, 162, 235, 1.0)"
					],
					data: [120, 90, 150, 60, 30]
				}
			]
		},
		options: {
			plugins: {
				title: {
					display: true,
					text: "Häufigkeit der Angriffsmethoden"
				}
			},
			indexAxis: "y"
		}
	});
</script>

<canvas id="attackMethodsChart"></canvas>
