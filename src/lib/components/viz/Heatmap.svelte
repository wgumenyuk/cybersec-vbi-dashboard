<script lang="ts">
	import { onMount } from "svelte";
	import * as d3 from "d3";

	import data from "$lib/data/breaches_symbols.json";

	const calculatePercentageChange = (
		before: number,
		after: number
	): number => {
		return ((after - before) / before) * 100;
	};

	// Generate heatmap data
	const heatmapData = (() => {
		const impacts: Record<string, Record<string, number[]>> = {};

		data.forEach((d) => {
			const stockPriceBefore = parseFloat(d["Pre"]);
			const stockPriceAfter = parseFloat(d["Post"]);
			const industry = d.Industry;
			const types = d.Type;

			if (
				!isNaN(stockPriceBefore) &&
				!isNaN(stockPriceAfter) &&
				stockPriceBefore !== 0
			) {
				const percentageChange = calculatePercentageChange(
					stockPriceBefore,
					stockPriceAfter
				);

				types.forEach((type: string) => {
					if (!impacts[type]) impacts[type] = {};
					if (!impacts[type][industry]) impacts[type][industry] = [];
					impacts[type][industry].push(percentageChange);
				});
			}
		});

		// Calculate averages and include all combinations
		const allTypes = Array.from(new Set(data.flatMap((d) => d.Type)));
		const allIndustries = Array.from(new Set(data.map((d) => d.Industry)));

		const allCombinations = allTypes.flatMap((type) =>
			allIndustries.map((industry) => ({
				type,
				industry,
				impact:
					impacts[type]?.[industry]?.reduce(
						(acc, cur) => acc + cur,
						0
					) / (impacts[type]?.[industry]?.length || 1) || null // Assign null for missing data
			}))
		);

		return allCombinations;
	})();

	let svg: SVGSVGElement | null = null;

	const margin = { top: 20, right: 20, bottom: 40, left: 120 };
	const width = 800 - margin.left - margin.right;
	const height = 500 - margin.top - margin.bottom;

	let tooltip = { visible: false, x: 0, y: 0, text: "", color: "" };

	function showTooltip(event: MouseEvent, text: string, sliceColor: string) {
		const container = document.querySelector(".heatmap-container")!;
		const containerRect = container.getBoundingClientRect();
		const tooltipX =
			event.clientX - containerRect.left + container.scrollLeft;
		const tooltipY =
			event.clientY - containerRect.top + container.scrollTop;

		tooltip = {
			visible: true,
			x: tooltipX,
			y: tooltipY,
			text,
			color: sliceColor
		};
	}

	function hideTooltip() {
		tooltip.visible = false;
	}

	onMount(() => {
		const svgEl = d3
			.select(svg)
			.attr("width", width + margin.left + margin.right)
			.attr("height", height + margin.top + margin.bottom)
			.append("g")
			.attr("transform", `translate(${margin.left},${margin.top})`);

		const types = Array.from(new Set(heatmapData.map((d) => d.type)));
		const industries = Array.from(
			new Set(heatmapData.map((d) => d.industry))
		);

		const x = d3
			.scaleBand()
			.domain(industries)
			.range([0, width])
			.padding(0.05);
		const y = d3.scaleBand().domain(types).range([0, height]).padding(0.05);

		const color = d3
			//.scaleSequential(d3.interpolateRdYlGn)
			.scaleLinear()
			.domain([
				d3.min(heatmapData, (d) => d.impact) || -100,
				d3.max(heatmapData, (d) => d.impact) || 100
			])
			// @ts-expect-error Keine Ahnung, warum hier ein Fehler auftaucht -- funktioniert hervorragend.
			.range(["#f43f5e", "#10b981"]);

		//const fallbackColor = "#444444";
		const fallbackColor = "#302F31";

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

		svgEl
			.selectAll()
			.data(heatmapData)
			.join("rect")
			.attr("x", (d) => x(d.industry) ?? 0)
			.attr("y", (d) => y(d.type) ?? 0)
			.attr("width", x.bandwidth())
			.attr("height", y.bandwidth())
			.style("fill", (d) =>
				d.impact != null ? color(d.impact) : fallbackColor
			)
			.style("stroke", "white")
			.on("mouseenter", (event, d) => {
				if (d.impact != null) {
					showTooltip(
						event,
						`${d.impact.toFixed(2)}% change`,
						color(d.impact).toString()
					);
				}
			})
			.on("mouseleave", hideTooltip);
	});
</script>

<div class="heatmap-container relative">
	<svg bind:this={svg}></svg>

	<!-- Tooltip -->
	{#if tooltip.visible}
		<div
			class="absolute rounded bg-gray-800 p-2 text-white shadow"
			style="top: {tooltip.y}px; left: {tooltip.x}px; transform: translate(-50%, -100%);"
		>
			<div class="flex items-center gap-2">
				<div
					class="h-4 w-4 rounded"
					style="background-color: {tooltip.color}"
				></div>
				<span>{tooltip.text}</span>
			</div>
		</div>
	{/if}
</div>

<style>
	.heatmap-container {
		display: flex;
		justify-content: center;
		align-items: center;
	}

	.relative {
		position: relative;
	}

	svg {
		font-family: sans-serif;
	}

	.absolute {
		position: absolute;
	}

	.bg-gray-800 {
		background-color: #2d3748;
	}

	.text-white {
		color: white;
	}

	.rounded {
		border-radius: 0.25rem;
	}

	.shadow {
		box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
	}

	.flex {
		display: flex;
	}

	.items-center {
		align-items: center;
	}

	.gap-2 {
		gap: 0.5rem;
	}

	.w-4 {
		width: 1rem;
	}

	.h-4 {
		height: 1rem;
	}

	.p-2 {
		padding: 0.5rem;
	}
</style>
