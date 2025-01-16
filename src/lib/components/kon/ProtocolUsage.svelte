<script lang="ts">
	import { Chart } from "chart.js/auto";

	new Chart("protocolUsageChart", {
		type: "bar",
		data: {
			labels: ["HTTP", "HTTPS", "DNS", "FTP", "ICMP"],
			datasets: [
				{
					label: "Requests",
					data: [150, 120, 100, 80, 60]
				},
				{
					label: "Responses",
					data: [130, 110, 90, 70, 50]
				},
				{
					label: "Errors",
					data: [20, 10, 10, 10, 10]
				}
			]
		},
		options: {
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
