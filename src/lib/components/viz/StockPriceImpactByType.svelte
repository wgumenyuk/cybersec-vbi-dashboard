<script lang="ts">
	import { isNumber } from "mathjs";
	import * as d3 from "d3";

	// Dataset
	import data from "$lib/data/breaches_symbols.json";

	// Helper function to calculate percentage change
	const calculatePercentageChange = (
		before: number,
		after: number
	): number => {
		return ((after - before) / before) * 100;
	};

	// Calculate average stock price impact by breach type
	const impactData = (() => {
		const impacts: Record<string, number[]> = {};

		data.forEach((d) => {
			const stockPriceBefore = d.Pre
				? parseFloat(d.Pre.toString())
				: null;
			const stockPriceAfter = d.Post
				? parseFloat(d.Post.toString())
				: null;
			const types = d.Type;

			if (
				isNumber(stockPriceBefore) &&
				isNumber(stockPriceAfter) &&
				stockPriceBefore !== 0
			) {
				const percentageChange = calculatePercentageChange(
					stockPriceBefore,
					stockPriceAfter
				);

				// Ensure `types` is valid and iterate over it
				if (Array.isArray(types)) {
					types.forEach((type) => {
						if (type) {
							// Ensure type is defined and non-empty
							if (!impacts[type]) impacts[type] = [];
							impacts[type].push(percentageChange);
						}
					});
				}
			}
		});

		return Object.entries(impacts).map(([type, changes]) => ({
			type: type.replace(/breach/i, "").trim(),
			impact: changes.reduce((acc, cur) => acc + cur, 0) / changes.length
		}));
	})();

	let svg;
	const margin = { top: 60, right: 20, bottom: 140, left: 60 };
	const width = 800 - margin.left - margin.right;
	const height = 800 - margin.top - margin.bottom;
	let tooltip = { visible: false, x: 0, y: 0, text: "", color: "" };

	$: x = d3
		.scaleBand()
		.domain(impactData.map((d) => d.type))
		.range([0, width])
		.padding(0.5);

	$: y = d3
		.scaleLinear()
		.domain([
			Math.min(0, Math.floor(d3.min(impactData, (d) => d.impact) || 0)),
			Math.ceil(d3.max(impactData, (d) => d.impact) || 0)
		])
		.range([height, 0]);

	function showTooltip(event: MouseEvent, impact: number, color: string) {
		tooltip = {
			visible: true,
			x: event.pageX,
			y: event.pageY - 40,
			text: `${impact.toFixed(2)}%`,
			color
		};
	}

	function hideTooltip() {
		tooltip.visible = false;
	}
</script>

<svg
	class="h-full w-full"
	bind:this={svg}
	viewBox={`0 0 ${width + margin.left + margin.right} ${height + margin.top + margin.bottom}`}
>
	<g transform={`translate(${margin.left},${margin.top})`}>
		<!-- Horizontal Background Lines -->
		{#each y.ticks(10) as tick}
			<line
				x1={0}
				x2={width}
				y1={y(tick)}
				y2={y(tick)}
				class="stroke-dasharray stroke-gray-700"
			></line>
		{/each}

		<!-- Bars -->
		{#each impactData as { type, impact }}
			<rect
				role="graphics-symbol"
				aria-label={`Bar representing an impact of ${impact.toFixed(2)}%`}
				x={x(type) ?? 0}
				y={Math.min(y(impact), y(0))}
				width={x.bandwidth() ?? 0}
				height={Math.abs((y(impact) ?? 0) - (y(0) ?? 0))}
				class={impact > 0
					? "fill-emerald-600 dark:fill-emerald-500"
					: "fill-rose-600 dark:fill-rose-500"}
				on:mouseenter={(e) =>
					showTooltip(e, impact, impact > 0 ? "#10b981" : "#f43f5e")}
				on:mouseleave={hideTooltip}
			/>
		{/each}

		<!-- X-Axis Labels -->
		<g class="x-axis">
			{#each x.domain() as type}
				<text
					x={(x(type) ?? 0) + (x.bandwidth() ?? 0) / 2}
					y={height + 30}
					transform={`translate(-10, 0) rotate(45 ${(x(type) ?? 0) + (x.bandwidth() ?? 0) / 2} ${height + 30})`}
					text-anchor="start-label"
					class="text-label italic"
				>
					{type}
				</text>
			{/each}
		</g>

		<!-- Y-Axis Labels -->
		<g class="y-axis">
			{#each y.ticks(10) as tick}
				<text
					x={-10}
					y={y(tick)}
					text-anchor="end"
					dy=".35em"
					class="text-label"
				>
					{tick}%
				</text>
			{/each}
		</g>

		<!-- X-Axis Title -->
		<text
			x={width / 2}
			y={height + margin.bottom + 35}
			text-anchor="middle"
			class="axis-title"
		>
			Breach Type
		</text>

		<!-- Y-Axis Title -->
		<text
			x={-margin.left + 20}
			y={-45}
			text-anchor="start"
			class="axis-title"
		>
			Stock Price Impact (%)
		</text>
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

<style lang="postcss">
	text {
		font-size: 18px;
		font-family: sans-serif;
		fill: white;
	}

	.axis-title {
		font-size: 20px;
		font-weight: bold;
	}

	:global(html[data-theme="dark"]) {
		.axis-title,
		.text-label {
			fill: rgba(255, 255, 255, 0.5);
		}

		.stroke-gray-700 {
			stroke: rgba(255, 255, 255, 0.25);
		}
	}

	:global(html[data-theme="light"]) {
		.axis-title,
		.text-label {
			fill: rgba(0, 0, 0, 0.5);
		}

		.stroke-gray-700 {
			stroke: rgba(0, 0, 0, 0.25);
		}
	}

	.stroke-dasharray {
		stroke-dasharray: 4, 4;
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
