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
		notation: "compact"
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
	const margin = { top: 50, right: 30, bottom: 100, left: 80 };
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
</script>

<svg
	class="h-full w-full"
	viewBox={`0 0 ${width + margin.left + margin.right} ${height + margin.top + margin.bottom}`}
	style="font-family: Arial, sans-serif;"
>
	<g transform={`translate(${margin.left},${margin.top})`}>
		<!-- Bars -->
		{#each barData as { label, value, color }}
			<rect
				role="graphics-symbol"
				aria-label={`Bar representing ${label}: ${value.toFixed(0)} people affected`}
				x={x(label) ?? 0}
				y={y(value) ?? 0}
				width={x.bandwidth() * 0.4}
				height={height - (y(value) ?? 0)}
				fill={color}
			/>
		{/each}

		<!-- X-Axis -->
		<g>
			{#if x}
				{#each x.domain() as label}
					<text
						x={(x(label) ?? 0) + x.bandwidth() / 2}
						y={height + 25}
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
						x="-15"
						y={y(tick)}
						text-anchor="end"
						dy="0.32em"
						class="axis-label"
					>
						{formatNumber(tick)}
					</text>
				</g>
			{/each}

			<!-- Y-Axis Label -->
			<text
				transform="rotate(-90)"
				x={-height / 2}
				y={-margin.left + 10}
				text-anchor="middle"
				class="axis-label"
			>
				People Affected (in Millions)
			</text>
		{/if}
	</g>
</svg>

<style lang="postcss">
	text.axis-label {
		font-size: 12px;
		fill: #ccc;
	}

	:global(html[data-theme="dark"]) {
		.stroke-gray-300 {
			stroke: rgba(255, 255, 255, 0.25);
		}

		.axis-label {
			font-size: 12px;
			stroke: rgba(255, 255, 255, 0.25);
		}
	}

	:global(html[data-theme="light"]) {
		.stroke-gray-300 {
			stroke: rgba(0, 0, 0, 0.25);
		}

		.axis-label {
			font-size: 12px;
			stroke: rgba(0, 0, 0, 0.25);
		}
	}
</style>
