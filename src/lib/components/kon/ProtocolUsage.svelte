<script lang="ts">
	import { Chart } from "chart.js/auto";

	new Chart("protocolUsageChart", {
		type: "bar",
		data: {
			labels: ["HTTP", "HTTPS", "DNS", "FTP", "ICMP"],
			datasets: [
				{
					label: "Requests",
					data: [150, 120, 100, 80, 60],
					backgroundColor: "rgba(54, 162, 235, 0.5)",
					borderColor: "rgba(54, 162, 235, 1)",
					borderWidth: 1
				},
				{
					label: "Responses",
					data: [130, 110, 90, 70, 50],
					backgroundColor: "rgba(75, 192, 192, 0.5)",
					borderColor: "rgba(75, 192, 192, 1)",
					borderWidth: 1
				},
				{
					label: "Errors",
					data: [20, 10, 10, 10, 10],
					backgroundColor: "rgba(255, 99, 132, 0.5)",
					borderColor: "rgba(255, 99, 132, 1)",
					borderWidth: 1
				}
			]
		},
		options: {
			responsive: true,
			plugins: {
				title: {
					display: true,
					text: "Protokollnutzung: Anfragen, Antworten und Fehler"
				},
				legend: {
					display: true,
					position: "top"
				}
			},
			scales: {
				x: {
					stacked: true,
					title: {
						display: true,
						text: "Protokolle"
					}
				},
				y: {
					stacked: true,
					title: {
						display: true,
						text: "Anzahl"
					}
				}
			}
		}
	});
</script>

<canvas id="protocolUsageChart"></canvas>
