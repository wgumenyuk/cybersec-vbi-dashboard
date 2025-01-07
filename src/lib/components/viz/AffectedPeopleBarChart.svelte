<script lang="ts">
	/* eslint-disable @typescript-eslint/no-explicit-any */
	import * as d3 from "d3";

	// Dataset
	import data from "$lib/data/breaches_symbols.json";
	import { onMount } from "svelte";

	let {
		breachID
	}: {
		breachID: number;
	} = $props();

	// Helper function for formatting numbers
	const { format: formatNumber } = new Intl.NumberFormat("en-US", {
		style: "decimal"
	});

	// Helper function to calculate the median
	function calculateMedianAffected(
		filterFn: (entry: any) => boolean
	): number {
		const filteredData = data
			.filter(filterFn)
			.map((entry) =>
				typeof entry.Affected === "number" ? entry.Affected : 0
			)
			.filter((value) => value > 0);

		if (!filteredData.length) return 0;

		const sorted = filteredData.sort((a, b) => a - b);
		const mid = Math.floor(sorted.length / 2);

		return sorted.length % 2 === 0
			? (sorted[mid - 1] + sorted[mid]) / 2
			: sorted[mid];
	}

	// Chart dimensions
	const margin = { top: 50, right: 30, bottom: 100, left: 60 };
	const width = 800 - margin.left - margin.right;
	const height = 500 - margin.top - margin.bottom;

	let barData = $state<any[]>([]);
	let x = $state<any>();
	let y = $state<any>();
	/* eslint-enable @typescript-eslint/no-explicit-any */

	onMount(() => {
		const breach = data.find((breach) => breach.ID === breachID);

		if (!breach) {
			return;
		}

		// Compute data for the bar chart
		barData = [
			{
				label: "Specific Case",
				value:
					typeof breach.Affected === "number" ? breach.Affected : 0,
				color: "#FF5722"
			},
			{
				label: "Breach Type Median",
				value: calculateMedianAffected((entry: typeof breach) =>
					entry.Type.some((type) => breach.Type.includes(type))
				),
				color: "#2196F3"
			},
			{
				label: "Industry Median",
				value: calculateMedianAffected(
					(entry) => entry.Industry === breach.Industry
				),
				color: "#4CAF50"
			}
		];

		// D3 Scales
		x = d3
			.scaleBand()
			.domain(barData.map((d) => d.label))
			.range([0, width])
			.padding(0.3);

		y = d3
			.scaleLinear()
			.domain([0, d3.max(barData, (d) => d.value) || 0])
			.range([height, 0]);
	});

	// Tooltip
	let tooltip = $state({ visible: false, x: 0, y: 0, text: "", color: "" });

	function showTooltip(event: MouseEvent, value: number, color: string) {
		tooltip = {
			visible: true,
			x: event.pageX,
			y: event.pageY - 40,
			text: `${formatNumber(value)} People`, // Use formatted value
			color
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
				x={x(label) ?? 0}
				y={y(value) ?? 0}
				width={x.bandwidth()}
				height={height - (y(value) ?? 0)}
				fill={color}
				onmouseenter={(e) => showTooltip(e, value, color)}
				onmouseleave={hideTooltip}
			/>
		{/each}

		<!-- X-Axis -->
		<g>
			{#if x}
				{#each x.domain() as label}
					<text
						x={(x(label) ?? 0) + x.bandwidth() / 2}
						y={height + 30}
						text-anchor="middle"
						class="axis-label"
					>
						{label}
					</text>
				{/each}
			{/if}
		</g>

		<!-- Y-Axis -->
		{#if y}
			{#each y.ticks(5) as tick}
				<g>
					<line
						x1="0"
						x2={width}
						y1={y(tick)}
						y2={y(tick)}
						class="stroke-gray-300"
					/>
					<text
						x="-10"
						y={y(tick)}
						text-anchor="end"
						dy="0.32em"
						class="axis-label"
					>
						{tick}
					</text>
				</g>
			{/each}
		{/if}
	</g>
</svg>

{#if tooltip.visible}
	<div
		class="absolute rounded bg-gray-800 p-2 text-white shadow"
		style="top: {tooltip.y}px; left: {tooltip.x}px"
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
