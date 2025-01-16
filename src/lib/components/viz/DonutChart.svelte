<script lang="ts">
	import { onMount } from "svelte";
	import { browser } from "$app/environment";
	import { mean } from "mathjs";
	import { Chart } from "chart.js/auto";

	// Dataset
	import data from "$lib/data/breaches_symbols.json";

	/**
		Enthält die durchscnittliche Anzahl von Betroffenen pro Branche.
	*/
	const processedData = (() => {
		const impacts: Record<string, number[]> = {};

		for (const d of data) {
			const affected = Number(d.Affected);
			const types = d.Type;

			if (isNaN(affected)) {
				continue;
			}

			for (const type of types) {
				impacts[type] = impacts[type] || [];
				impacts[type].push(affected);
			}
		}

		return Object.entries(impacts)
			.map(([type, affected]) => ({
				type,
				average: mean(affected.reduce((acc, cur) => acc + cur, 0))
			}))
			.sort((a, z) => z.average - a.average);
	})();

	const { format: formatNumber } = new Intl.NumberFormat("en-US", {
		notation: "compact"
	});

	let canvas: HTMLCanvasElement;

	onMount(() => {
		if (!browser) {
			return;
		}

		new Chart(canvas, {
			type: "doughnut",
			data: {
				labels: processedData.map((d) => d.type),
				datasets: [
					{
						data: processedData.map((d) => d.average)
					}
				]
			},
			options: {
				plugins: {
					legend: {
						position: "bottom",
						labels: {
							color: "#ffffff"
						}
					},
					tooltip: {
						callbacks: {
							label: (ctx) => formatNumber(ctx.parsed)
						}
					}
				}
			}
		});
	});
</script>

<canvas bind:this={canvas}></canvas>
