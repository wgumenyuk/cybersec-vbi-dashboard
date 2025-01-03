<script lang="ts">
	import { onMount } from "svelte";
	import * as d3 from "d3";

	// Dataset
	import data from "$lib/data/breaches_symbols.json";

	// Helper function to calculate percentage change
	const calculatePercentageChange = (before: number, after: number): number => {
		return ((after - before) / before) * 100;
	};

	// Prepare data for the heatmap
	const heatmapData = (() => {
		const impacts: Record<string, Record<string, number[]>> = {};

		data.forEach((d) => {
			const stockPriceBefore = parseFloat(d["Pre-Attack Stock Price"]);
			const stockPriceAfter = parseFloat(d["Post-Attack Stock Price"]);
			const industry = d.Industry;
			const types = d.Type;

			if (!isNaN(stockPriceBefore) && !isNaN(stockPriceAfter) && stockPriceBefore !== 0) {
				const percentageChange = calculatePercentageChange(stockPriceBefore, stockPriceAfter);

				types.forEach((type: string) => {
					if (!impacts[type]) impacts[type] = {};
					if (!impacts[type][industry]) impacts[type][industry] = [];
					impacts[type][industry].push(percentageChange);
				});
			}
		});

		// Calculate averages
		return Object.entries(impacts).map(([type, industries]) => {
			return Object.entries(industries).map(([industry, changes]) => ({
				type,
				industry,
				impact: changes.reduce((acc, cur) => acc + cur, 0) / changes.length,
			}));
		}).flat();
	})();

	let svg: SVGSVGElement | null = null;

	const margin = { top: 20, right: 20, bottom: 40, left: 120 };
	const width = 800 - margin.left - margin.right;
	const height = 500 - margin.top - margin.bottom;

	onMount(() => {
		const svgEl = d3
			.select(svg)
			.attr("width", width + margin.left + margin.right)
			.attr("height", height + margin.top + margin.bottom)
			.append("g")
			.attr("transform", `translate(${margin.left},${margin.top})`);

		// Extract unique breach types and industries
		const types = Array.from(new Set(heatmapData.map((d) => d.type)));
		const industries = Array.from(new Set(heatmapData.map((d) => d.industry)));

		// Define scales
		const x = d3.scaleBand().domain(industries).range([0, width]).padding(0.05);
		const y = d3.scaleBand().domain(types).range([0, height]).padding(0.05);
		const color = d3
			.scaleSequential(d3.interpolateRdYlGn)
			.domain(d3.extent(heatmapData, (d) => d.impact) as [number, number]);

		// Add axes
		svgEl
			.append("g")
			.attr("transform", `translate(0,${height})`)
			.call(d3.axisBottom(x).tickSize(0))
			.select(".domain")
			.remove();

		svgEl
			.append("g")
			.call(d3.axisLeft(y).tickSize(0))
			.select(".domain")
			.remove();

        // Add heatmap rectangles
        svgEl
            .selectAll()
            .data(heatmapData, (d: any) => `${d.type}:${d.industry}`)
            .join("rect")
            .attr("x", (d) => x(d.industry) ?? 0) // Ensure fallback to 0
            .attr("y", (d) => y(d.type) ?? 0)     // Ensure fallback to 0
            .attr("width", x.bandwidth())
            .attr("height", y.bandwidth())
            .style("fill", (d) => color(d.impact))
            .style("stroke", "white");

	});
</script>

<div class="heatmap-container">
	<svg bind:this={svg}></svg>
</div>

<style>
	.heatmap-container {
		display: flex;
		justify-content: center;
		align-items: center;
	}
	svg {
		font-family: sans-serif;
	}
</style>
