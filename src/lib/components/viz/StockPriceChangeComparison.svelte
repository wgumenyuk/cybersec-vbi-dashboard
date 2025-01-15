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

	function calculateMeanChange(
		filterFn: (entry: (typeof data)[0]) => boolean
	): number {
		const filteredData = data
			.filter(filterFn)
			.map((entry) => entry["Stock Change"] || 0)
			.filter((value) => !isNaN(value));

		if (!filteredData.length) return 0;

		const sorted = filteredData.toSorted((a, b) => a - b);

		return mean(sorted);
	}

	type StockChange = {
		label: string;
		value: number;
	};

	let canvas: HTMLCanvasElement;

	let theme = $state(document.documentElement.dataset.theme);
	let stockChangeData = $state<StockChange[]>([]);

	onMount(() => {
		const breach = data.find((breach) => breach.ID === breachID);

		if (!breach) {
			return;
		}

		stockChangeData = [
			{
				label: "Specific Case",
				value: breach["Stock Change"] || 0
			},
			{
				label: "Breach Type Mean",
				value: calculateMeanChange((entry) =>
					entry.Type.some((type: string) =>
						breach.Type.includes(type)
					)
				)
			},
			{
				label: "Industry Mean",
				value: calculateMeanChange(
					(entry) => entry.Industry === breach.Industry
				)
			}
		];

		new Chart(canvas, {
			type: "bar",
			data: {
				labels: stockChangeData.map((d) => d.label),
				datasets: [
					{
						label: "Comparison",
						data: stockChangeData.map((d) => d.value),
						backgroundColor: ["#36a2eb", "#ff6384", "#ff9f40"]
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
							label: (ctx) =>
								`${ctx.label}: ${ctx.parsed.y.toFixed(2)}%`
						}
					}
				},
				scales: {
					y: {
						ticks: {
							callback: (value) => `${value}%`
						},
						grid: {
							color: (ctx) => {
								if (theme === "light") {
									return ctx.tick.value === 0
										? "rgba(0, 0, 0, 0.5)"
										: "rgba(0, 0, 0, 0.25)";
								}

								return ctx.tick.value === 0
									? "rgba(255, 255, 255, 0.5)"
									: "rgba(255, 255, 255, 0.25)";
							},
							lineWidth: (ctx) => (ctx.tick.value === 0 ? 2 : 1)
						}
					}
				}
			}
		});
	});
</script>

<canvas bind:this={canvas}></canvas>
