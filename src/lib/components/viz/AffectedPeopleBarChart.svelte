<script lang="ts">
	import * as d3 from "d3";

	export let breachData; // Selected breach
	export let dataset; // Full dataset

	// Helper function for formatting numbers
	const formatNumber = new Intl.NumberFormat("en-US", {
		style: "decimal",
	});

	// Helper function to calculate the median
	function calculateMedianAffected(filterFn: (entry: any) => boolean): number {
		const filteredData = dataset
			.filter(filterFn)
			.map((entry) => (typeof entry.Affected === "number" ? entry.Affected : 0))
			.filter((value) => value > 0);

		if (!filteredData.length) return 0;

		const sorted = filteredData.sort((a, b) => a - b);
		const mid = Math.floor(sorted.length / 2);

		return sorted.length % 2 === 0
			? (sorted[mid - 1] + sorted[mid]) / 2
			: sorted[mid];
	}

	// Compute data for the bar chart
	const barData = [
		{
			label: "Specific Case",
			value: typeof breachData.Affected === "number" ? breachData.Affected : 0,
			color: "#FF5722",
		},
		{
			label: "Breach Type Median",
			value: calculateMedianAffected((entry) =>
				entry.Type.some((type) => breachData.Type.includes(type))
			),
			color: "#2196F3",
		},
		{
			label: "Industry Median",
			value: calculateMedianAffected((entry) => entry.Industry === breachData.Industry),
			color: "#4CAF50",
		},
	];

	// Chart dimensions
	const margin = { top: 50, right: 30, bottom: 100, left: 60 };
	const width = 800 - margin.left - margin.right;
	const height = 500 - margin.top - margin.bottom;

	// D3 Scales
	$: xScale = d3
		.scaleBand()
		.domain(barData.map((d) => d.label))
		.range([0, width])
		.padding(0.3);

	$: yScale = d3
		.scaleLinear()
		.domain([0, d3.max(barData, (d) => d.value) || 0])
		.range([height, 0]);

	// Tooltip
	let tooltip = { visible: false, x: 0, y: 0, text: "", color: "" };

	function showTooltip(event: MouseEvent, value: number, color: string) {
		tooltip = {
			visible: true,
			x: event.pageX,
			y: event.pageY - 40,
			text: `${formatNumber.format(value)} People`, // Use formatted value
			color,
		};
	}

	function hideTooltip() {
		tooltip.visible = false;
	}
</script>

<svg
	class="h-full w-full"
	viewBox={`0 0 ${width + margin.left + margin.right} ${height + margin.top + margin.bottom}`}
>
	<g transform={`translate(${margin.left},${margin.top})`}>
		<!-- Bars -->
		{#each barData as { label, value, color }}
			<rect
				role="graphics-symbol"
				aria-label={`Bar representing ${label}: ${value.toFixed(0)} people affected`}
				x={xScale(label) ?? 0}
				y={yScale(value) ?? 0}
				width={xScale.bandwidth()}
				height={height - (yScale(value) ?? 0)}
				fill={color}
				on:mouseenter={(e) => showTooltip(e, value, color)}
				on:mouseleave={hideTooltip}
			/>
		{/each}

		<!-- X-Axis -->
		<g>
			{#each xScale.domain() as label}
				<text
					x={(xScale(label) ?? 0) + xScale.bandwidth() / 2}
					y={height + 30}
					text-anchor="middle"
					class="axis-label"
				>
					{label}
				</text>
			{/each}
		</g>

		<!-- Y-Axis -->
		{#each yScale.ticks(5) as tick}
			<g>
				<line x1="0" x2={width} y1={yScale(tick)} y2={yScale(tick)} class="stroke-gray-300" />
				<text x="-10" y={yScale(tick)} text-anchor="end" dy="0.32em" class="axis-label">
					{tick}
				</text>
			</g>
		{/each}
	</g>
</svg>

{#if tooltip.visible}
	<div
		class="absolute rounded bg-gray-800 p-2 text-white shadow"
		style="top: {tooltip.y}px; left: {tooltip.x}px"
	>
		<div class="flex items-center gap-2">
			<div class="h-4 w-4 rounded" style="background-color: {tooltip.color}"></div>
			<span>{tooltip.text}</span>
		</div>
	</div>
{/if}

<style>
	text.axis-label {
		font-size: 14px;
		font-family: sans-serif;
		fill: white; /* Ensures white labels */
	}

	.stroke-gray-300 {
		stroke: #ccc;
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
</style>
