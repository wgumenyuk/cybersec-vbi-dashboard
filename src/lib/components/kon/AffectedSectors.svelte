<script lang="ts">
	import { Chart } from "chart.js/auto";
	import { onMount } from "svelte";

	onMount(() => {
		new Chart("affectedSectorsChart", {
			type: "bar",
			data: {
				labels: [
					"Finance",
					"Healthcare",
					"Retail",
					"Education",
					"Government"
				],
				datasets: [
    {
        label: "Malware",
        data: [14.3, 15.2, 13.8, 14.5, 15.0, 14.7, 15.1, 14.9],
        backgroundColor: "rgba(54, 162, 235, 0.8)"
    },
    {
        label: "Phishing",
        data: [12.4, 12.0, 12.7, 12.3, 12.5, 12.8, 12.6, 12.2],
        backgroundColor: "rgba(255, 99, 132, 0.8)"
    },
    {
        label: "DDoS",
        data: [8.5, 8.3, 8.2, 8.4, 8.1, 8.3, 8.2, 8.0],
        backgroundColor: "rgba(75, 192, 192, 0.8)"
    }
]

			},
			options: {
				plugins: {
					title: {
						display: true,
						text: "Wie sind Branchen von Angriffstypen betroffen?"
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
	});
</script>

<canvas id="affectedSectorsChart"></canvas>
