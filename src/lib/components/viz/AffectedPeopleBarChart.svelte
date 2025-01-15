<script lang="ts">
	import { onMount } from "svelte";
	import { Chart } from "chart.js/auto";
	import { mean } from "mathjs";

	// Dataset
	import data from "$lib/data/breaches_symbols.json";

	let {
		breachID
	}: {
		breachID: number;
	} = $props();

	// Helper function for formatting numbers
	const { format: formatNumber } = new Intl.NumberFormat("en-US", {
		notation: "compact"
	});

	// Helper function to calculate the median
	function calculateMedianAffected(
		filterFn: (entry: (typeof data)[0]) => boolean
	) {
		const filteredData = data
			.filter(filterFn)
			.map((entry) =>
				typeof entry.Affected === "number" ? entry.Affected : 0
			)
			.filter((value) => value > 0);

		if (!filteredData.length) return 0;

		const sorted = filteredData.toSorted((a, b) => a - b);

		return mean(sorted);
	}

	type Bar = {
		label: string;
		value: number;
	};

	let canvas: HTMLCanvasElement;

	let theme = $state(document.documentElement.dataset.theme);
	let barData = $state<Bar[]>([]);

	onMount(() => {
		const breach = data.find((breach) => breach.ID === breachID);

		if (!breach) {
			return;
		}

		// Compute data for the bar chart
		barData = [
			{
				label: "Specific Case",
				value: typeof breach.Affected === "number" ? breach.Affected : 0
			},
			{
				label: "Breach Type Median",
				value: calculateMedianAffected((entry: typeof breach) =>
					entry.Type.some((type) => breach.Type.includes(type))
				)
			},
			{
				label: "Industry Median",
				value: calculateMedianAffected(
					(entry) => entry.Industry === breach.Industry
				)
			}
		];

		new Chart(canvas, {
			type: "bar",
			data: {
				labels: barData.map((d) => d.label),
				datasets: [
					{
						label: "Comparison",
						data: barData.map((d) => d.value),
						backgroundColor: ["#36a2eb", "#ff6384", "#ff9f40"]
					}
				]
			},
			options: {
				plugins: {
					legend: {
						display: false
					}
				},
				scales: {
					y: {
						grid: {
							color:
								theme === "dark"
									? "rgba(255, 255, 255, 0.25)"
									: "rgba(0, 0, 0, 0.25)"
						},
						ticks: {
							callback: (value) => formatNumber(value as number)
						}
					}
				}
			}
		});
	});
</script>

<canvas bind:this={canvas}></canvas>
