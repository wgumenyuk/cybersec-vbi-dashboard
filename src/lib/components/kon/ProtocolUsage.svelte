<script lang="ts">
	import { Chart } from "chart.js/auto";

	new Chart("protocolUsageChart", {
		type: "bar",
		data: {
			labels: ["HTTP", "HTTPS", "DNS", "FTP", "ICMP"],
			datasets: [
				{
					label: "Requests",
					backgroundColor: "rgba(54, 162, 235, 0.8)",
					data: [150, 120, 100, 80, 60]
				},
				{
					label: "Responses",
					backgroundColor: "rgba(54, 162, 235, 0.6)",
					data: [130, 110, 90, 70, 50]
				},
				{
					label: "Errors",
					backgroundColor: "rgba(54, 162, 235, 0.4)",
					data: [20, 10, 10, 10, 10]
				}
			]
		},
		options: {
			plugins: {
				title: {
					display: true,
					text: "Häufigkeit der verwendeten Protokolle (Anfragen, Antworten, Fehler)"
				}
			},
			responsive: true,
			scales: {
				x: {
					stacked: true
				},
				y: {
					stacked: true
				}
			}
		}
	});
</script>

<canvas id="protocolUsageChart"></canvas>
